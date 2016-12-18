import rospy
# from skeleton_markers.msg import Skeleton
# from kinect_pos import KinectPose
from std_msgs.msg import String
from sensor_msgs.msg import Image,CompressedImage
import matplotlib.pyplot as plt
import numpy as np
import cv2

# import nao_robot/camera/front/image_raw.msg
class NaoListener():

    def __init__(self):
        # self.nao_frontcamera_listener()
        self.nao_frontcamera_depth_listener()
    def callback(self, data):
        # nao_png_string = np.fromstring(data.data, np.uint8)
        nao_png_string = data.data
        pub = rospy.Publisher('nao_png_string',String)
        rospy.loginfo(nao_png_string)
        pub.publish(nao_png_string)
        # np_img = np.reshape(nao_png_string,(data.height,data.width,3))
        # plt.imshow(np_img)

    def nao_frontcamera_listener(self):
        #init a listener to kinect and
        rospy.init_node('nao_frontcamera_listener')
        rospy.Subscriber("nao_robot/camera/front/image_raw", Image, self.callback)
        rospy.spin()

    def nao_frontcamera_depth_listener(self):
        #init a listener to kinect and
        rospy.init_node('nao_front_camera_depth_listener')
        rospy.Subscriber("nao_robot/camera/bottom/image_raw/compressedDepth", CompressedImage, self.callback)
        rospy.spin()

    def string_to_png(self,img_str):
        img_arr = np.fromstring(img_str, np.uint8)
        img_mat = np.reshape(img_arr,(240,320,3))




print ("rinat")
l = NaoListener()
