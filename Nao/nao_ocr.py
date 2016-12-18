import rospy
from sensor_msgs.msg import Image
import pyocr
import numpy as np
import sys


class NaoOCR:

    def __init__(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        self.tool = tools[0]

        self.nao_front_camera_listener()
        self.txt = None
        self.word_boxes = None
        self.line_and_word_boxes = None

    def process_ocr(self, data):
        img_arr = np.fromstring(data.data, np.uint8)
        img_mat = np.reshape(img_arr, (data.height, data.width, 3))    # TODO: data.width, data.height
        img_pil = Image.fromarray(img_mat)

        self.txt = self.tool.image_to_string(
            img_pil,
            lang="eng",
            builder=pyocr.builders.TextBuilder()
        )

        self.word_boxes = self.tool.image_to_string(
            img_pil,
            lang="eng",
            builder=pyocr.builders.WordBoxBuilder()
        )

        self.line_and_word_boxes = self.tool.image_to_string(
            img_pil,
            lang="eng",
            builder=pyocr.builders.LineBoxBuilder()
        )

    def nao_front_camera_listener(self):
        rospy.init_node('nao_ocr')
        rospy.Subscriber("nao_robot/camera/front/image_raw", Image, self.process_ocr)
        rospy.spin()

nao_ocr = NaoOCR()
