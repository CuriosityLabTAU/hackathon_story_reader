from naoqi import ALProxy

ip = "192.168.0.104"
port = 9559

tts = ALProxy("ALTextToSpeech", ip, port)
tts.say("hopa, keren, hopa, keren, hopa, hey hey hey")

# http://doc.aldebaran.com/2-1/naoqi/trackers/altracker-api.html#ALTrackerProxy::lookAt__std::vector:float:CR.iCR.floatCR.bC

motion = ALProxy("ALMotion", ip, port)
posture = ALProxy("ALRobotPosture", ip, port)
tracker = ALProxy("ALTracker", ip, port)

fractionmaxspeed = 0.9
use = True
vect = [1, 0, 0]
# tracker.lookAt(vect, fractionmaxspeed, use)
effector = "RArm"
tracker.pointAt(effector, vect, fractionmaxspeed, use)
