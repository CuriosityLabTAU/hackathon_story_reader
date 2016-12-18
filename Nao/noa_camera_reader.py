import rospy
# from skeleton_markers.msg import Skeleton
# from kinect_pos import KinectPose
from std_msgs.msg import String
from sensor_msgs.msg import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# import nao_robot/camera/front/image_raw.msg
class NaoListener():

    def __init__(self):
        self.nao_frontcamera_listener()

    def callback(self, data):
        nao_png_string = np.fromstring(data.data, np.uint8)
        # np_img = np.reshape(np_arr,(data.height,data.width,3))
        # rospy.init_node('nao_png_publisher')
        pub = rospy.Publisher('nao_png_string',String)
        rospy.loginfo(nao_png_string)
        pub.publish(nao_png_string)

    def nao_frontcamera_listener(self):
        #init a listener to kinect and
        rospy.init_node('nao_frontcamera_listener')
        rospy.Subscriber("nao_robot/camera/front/image_raw", Image, self.callback)
        rospy.spin()

print ("rinat")
l = NaoListener()
