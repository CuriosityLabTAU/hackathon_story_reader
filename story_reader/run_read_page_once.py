import os

os.system('rostopic pub --once /interaction std_msgs/String \"read_page\"')