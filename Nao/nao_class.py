import naoqi
from naoqi import ALProxy
import pyocr


class NaoClass(object):

    def __init__(self, ip, port=9559):
        # port = 9559, ip = "172.16.102.10"
        self.port = port
        self.ip = ip
        self.motion, self.posture, self.tracker, self.tts = self.nao_actions()

    def StiffnessOn(self, proxy, body_part="Body"):
        # body_part is a string with the names of the parts we want stiff
        # We use the "Body" name to signify the collection of all joints
        pNames = body_part
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    def StiffnessOff(self, proxy, body_part="Body"):
        # body_part is a string with the names of the parts we want stiff
        # We use the "Body" name to signify the collection of all joints
        pNames = body_part
        pStiffnessLists = 0.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    def nao_actions(self):
        motion = ALProxy("ALMotion", self.ip, self.port)
        posture = ALProxy("ALRobotPosture", self.ip, self.port)
        tracker = ALProxy("ALTracker", self.ip, self.port)
        tts = ALProxy("ALTextToSpeech", self.ip, self.port)
        return motion, posture, tracker, tts

    def speak(self, text):
        self.tts.say(text)

    def change_resolution(self):
        vision = ALProxy("ALVideoDevice", self.ip, self.port)
        resolution = vision.k4VGA
        colorSpace = vision.kYUVColorSpace
        fps = 20

    #def point(self, ):

cl = NaoClass('192.168.0.103')
cl.change_resolution()