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
current_state = "up"

def publish_new_message(xyz_list, delta_time):

    p2p.x = xyz_list[0]
    p2p.y = xyz_list[1]
    p2p.z = xyz_list[2]
    p2p.delta = delta_time

    pub = rospy.Publisher("/Next_point_channel", Float32, queue_size = 10)
    rospy.init_node('next_point', anonymous = True)
    rospy.loginfo("next_point")
    pub.publish(p2p)

def calculate_new_destination(delta_time):
    global LINK1, LINK2, LINK3, LINK4, FULL_HEIGHT, PI, ROTATION_AMOUNT, INITIAL_STATE, current_angle, current_state

    rospy.loginfo("Recieved: %s", beat_timing.data)
    #Rotate around link 1:
    current_angle += ROTATION_AMOUNT
    if (current_angle >= 2*PI):
        current_angle = 0

    #Move up/down
    #Currently changes between "full length" and "full length" but 0.9 in x/y dir and higher
    if (current_state == "up"):
        current_state = "down"
        new_position = [INITIAL_STATE[0]*math.cos(current_angle), INITIAL_STATE[1]*math.sin(current_angle), INITIAL_STATE[2]]
    else:
        current_state = "up"
        new_position = [0.9*INITIAL_STATE[0]*math.cos(current_angle), 0.9*INITIAL_STATE[1]*math.sin(current_angle), INITIAL_STATE[2]+math.sqrt(1-0.(9**2))]

    publish_new_message(new_position, delta_time)


def listener():
    rospy.init_node("point_to_point_mapper")
    sub = rospy.Subscriber("BeatPlanPub", Float32, calculate_new_destination)
    rospy.spin()
