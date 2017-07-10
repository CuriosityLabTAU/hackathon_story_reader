import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
import json
from google.cloud import vision
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import io


class OCRnode():

    def __init__(self):
        rospy.init_node('ocr_node')
        rospy.Subscriber('ocr_get_image', Image, callback=self.process_image)
        self.pub = rospy.Publisher('ocr_data', String, queue_size=10)

        rospy.spin()

    def process_image(self, data):
        img = data.data

        img_arr = np.fromstring(img, np.uint8)
        if img_arr.shape[0] == (480*640*3):
            img_mat = np.reshape(img_arr,(480,640,3))
        else:
            # img_mat = np.reshape(img_arr,(240,320,3))
            img_mat = np.reshape(img_arr,(1280,960,3))

        vision_client = vision.Client(project='reading books')

        scipy.misc.imsave('tempfile.jpg', img_mat)
        with io.open('tempfile.jpg', 'rb') as image_file:
            content = image_file.read()

        image = vision_client.image(content=content)

        texts = image.detect_text()
        if len(texts) <= 0:
            print('No text in image')
        else:

            print('Texts:')
            msg_dict = {}
            msg_dict['text'] = texts[0].description
            msg_dict['bounds'] = str(texts[0].bounds.vertices[0]) + ',' + \
                str(texts[0].bounds.vertices[1]) + ',' + \
                str(texts[0].bounds.vertices[2]) + ',' + \
                str(texts[0].bounds.vertices[3])

            msg_dict['words'] = []
            for i in range(1, len(texts)):
                word_dict = {}
                word_dict['text'] = texts[i].description
                word_dict['bounds'] = str(texts[i].bounds.vertices[0]) + ',' + \
                    str(texts[i].bounds.vertices[1]) + ',' + \
                    str(texts[i].bounds.vertices[2]) + ',' + \
                    str(texts[i].bounds.vertices[3])
                msg_dict['words'].append(word_dict)

            self.pub.publish(json.dumps(msg_dict))
        # plt.imshow(img_mat)
        # plt.show()


node = OCRnode()