from naoqi import ALProxy
import time
import json
import rospy
import numpy as np
from std_msgs.msg import String

#
#
#
#
# robotIP = "192.168.0.108"
# ip = "192.168.0.108"
#
# port = 9559
#
# # tts = ALProxy("ALTextToSpeech", ip, port)
# # tts.say("hopa, keren, hopa, keren, hopa, hey hey hey")
# # tts.say("hi")
# #
# motionProxy = ALProxy("ALMotion", ip, port)
# posture = ALProxy("ALRobotPosture", ip, port)
# tracker = ALProxy("ALTracker", ip, port)
# # motionProxy.rest()
# motionProxy.wakeUp()
#
# fractionmaxspeed = 0.1
# use = True
# vect = [3.0, 1, 0]
# print tracker
#
#
# tracker.lookAt(vect, fractionmaxspeed, use)
# motionProxy.openHand('RHand')
#
# effector = "RArm"
# # mode = tracker.getMode()
# # print mode
# #tracker.track('LandMark')


# for z in range(3, 8, 1):
#     for y in range(-5, 0, 1):
#         vect = [0.2, y / 100, z / 100]
#         tracker.pointAt(effector, vect, fractionmaxspeed, use)
#         vect2 = [0.2, (y) / 100, (z) / 100]
#         tracker.lookAt(vect2, fractionmaxspeed, use)
#         time.sleep(0.2)
#         print (y, z)

#motionProxy.openHand('RHand')


#time.sleep(3)
#motionProxy.rest()

# motionProxy = ALProxy("ALMotion", robotIP, port)
#
# pTargetAngles = [0.0,0.0]
# pMaxSpeedFraction = 0.1
# pNames=('HeadPitch','HeadYaw')
# motionProxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)



class StoryTellerNode():

    def __init__(self):
        print("init story_teller")
        self.robot_publisher = rospy.Publisher('to_nao', String, queue_size=10)
        rospy.init_node('story_teller_node') #init a listener:
        rospy.Subscriber('nao_state', String, self.callback_nao_state)
        self.proceed=True

        #rospy.spin() #spin() simply keeps python from exiting until this node is stopped


    def read_page(self):
        print("read_page")
        message = {'action': 'wake_up'}
        self.robot_publisher.publish(json.dumps(message))

        message = '{\"action\":\"open_hand\", \"parameters\":[\"RHand\"]}'
        self.robot_publisher.publish(message)
        effector = 'RArm'
        fractionmaxspeed = 0.01
        use = True
        y_vec = np.linspace(0.20,-0.20,num=10)
        z_vec = np.linspace(0.20,0.10,num=10)
        for z in z_vec:
            for y in y_vec:
                vect = [0.25, y, z]
                #tracker.pointAt(effector, vect, fractionmaxspeed, use)
                message = {'action': 'point_at', 'parameters': [vect, fractionmaxspeed, use]}
                self.robot_publisher.publish(json.dumps(message))
                vect2 = [0.25, y, z]
                message = {'action': 'look_at', 'parameters': [vect2, fractionmaxspeed, use]}
                self.robot_publisher.publish(json.dumps(message))
                #tracker.lookAt(vect2, fractionmaxspeed, use)

                self.proceed=False
                time.sleep(0.2)
                while not self.proceed:
                    pass

                print (y,z)
        message = {'action': 'rest'}
        self.robot_publisher.publish(json.dumps(message))

    def callback_nao_state(self,data):
        try:
            message=json.loads(data.data)
            if 'look_at' in message:
                self.proceed = True
        except:
               print("callback_nao_state", data.data)



if __name__ == '__main__':
    try:
        story_teller_node =  StoryTellerNode ()
        time.sleep(4)
        story_teller_node.read_page()
    except rospy.ROSInterruptException,e:
        print "Error was: ", e
