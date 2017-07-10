import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
import numpy as np
import matplotlib.pyplot as plt


class InteractionNode():

    def __init__(self):
        self.read_now = False

        rospy.init_node('interaction_node')

        # rospy.Subscriber("nao_robot/camera/bottom/image_raw", Image, self.get_image)
        # rospy.Subscriber("nao_robot/camera/front/image_raw", Image, self.get_image)
        rospy.Subscriber("/usb_cam/image_raw", Image, self.get_image)
        rospy.Subscriber('interaction', String, self.parse_interaction)
        self.ocr_pub = rospy.Publisher('ocr_get_image', Image, queue_size=10)

        rospy.spin()

    def get_image(self, data):
        img_bin = data
        if self.read_now:
            self.read_now = False
            self.ocr_pub.publish(img_bin)

    def parse_interaction(self, data):
        msg = data.data

        if msg == 'read_page':
            self.read_now = True

node = InteractionNode()
