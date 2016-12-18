from game import *
from game.nao_move import *
import random
import time

class Story_Reader:

    def __init__(self):
        self.howie = NaoNode()
        # self.child = ChildKinect()
        # self.pose_selected = None
        # self.hertzel_says = True
        self.list_reader = []

    def robot_performs_action(self):
        # select the pose from the list of poses
        self.pose_selected = random.choice(self.howie.pose_names)
        print('selected: ', self.pose_selected)

        self.howie.move_to_pose(self.howie.poses[self.pose_selected])

time_sleep = 5
story_reader = Story_Reader()
story_reader.howie.play_file('intro.wav')
## base intro pose
time.sleep(time_sleep)
change_page = False
while(~change_page):
    story_reader.howie.play_file('next_page_reminder.wav')
    time.sleep(time_sleep)
    change_page = True
## start reading text


## case end of the page











