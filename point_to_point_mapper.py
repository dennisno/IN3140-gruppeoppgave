# To add:
# - Dependencies
#     - Dennis sin publisher
#     - Ros
# -

#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

LINK1 = 11.0
LINK2 = 22.3
LINK3 = 17
LINK4 = 8
FULL_HEIGHT = LINK1 + LINK2 + LINK3 + (math.sin(PI/4)*LINK4)
PI = math.pi
ROTATION_AMOUNT = 2*PI/20
INITIAL_STATE = [LINK2+LINK3, 0, LINK1]
current_angle = 0

def publish_new_message(data):
    pub = rospy.Publisher("/Next_point_channel", Float32, queue_size = 10)

def calculate_new_destination(beat_timing):
    global LINK1, LINK2, LINK3, LINK4, FULL_HEIGHT, PI, ROTATION_AMOUNT, INITIAL_STATE, current_angle

    rospy.loginfo("Recieved: %s", beat_timing.data)
    #Rotate around link 1:
    current_angle += ROTATION_AMOUNT
    if (current_angle >= 2*PI):
        current_angle = 0

    new_postiton = [INITIAL_STATE[0]*math.cos(current_angle), INITIAL_STATE[1]*math.sin(current_angle), INITIAL_STATE[2]]

    #Move



def listener():
    rospy.init_node("point_to_point_mapper")
    sub = rospy.Subscriber("/BeatPlanPub", Float32, calculate_new_destination)
    rospy.spin()
