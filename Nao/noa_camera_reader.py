import rospy
# from skeleton_markers.msg import Skeleton
# from kinect_pos import KinectPose
from std_msgs.msg import String
from sensor_msgs.msg import Image


# import nao_robot/camera/front/image_raw.msg
class NaoListener():

    def __init__(self):
        self.nao_frontcamera_listener()

    def callback(self, data):
        # get the data (name, position):  the data is the massage
        # kid_pose = KinectPose()
        # kid_pose.update_position(data.position)
        # message = str(kid_pose.poses_satisfied)
        # pub = rospy.Publisher ('kinect_poses', String)
        # #rospy.init_node('kinect_poses_publisher')
        # rospy.loginfo(message)
        # pub.publish(message)
        # print(message)
        print("type", type(data))
        print(data)

    # def kinect_listener():
    #     #init a listener to kinect and
    #     rospy.init_node('kinect_listener')
    #     rospy.Subscriber("skeleton", Skeleton, callback)
    #     rospy.spin()

    def nao_frontcamera_listener(self):
        #init a listener to kinect and
        rospy.init_node('nao_frontcamera_listener')
        rospy.Subscriber("nao_robot/camera/front/image_raw", Image, self.callback)
        rospy.spin()

print ("rinat")
l = NaoListener()
