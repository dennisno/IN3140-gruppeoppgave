#!/usr/bin/env python

import math
from math import pi as PI
import rospy
from std_msgs.msg import Float32
from crustcrawler_dance.msg import DeltaPoint

LINK1 = 11.0
LINK2 = 22.3
LINK3 = 17
LINK4 = 8
FULL_HEIGHT = LINK1 + LINK2 + LINK3 + (math.sin(PI/4)*LINK4)
ROTATION_AMOUNT = 2*PI/20
INITIAL_STATE = [LINK2+LINK3, 0, LINK1]
current_angle = 0
current_state = "up"

DeltaPointPublish = rospy.Publisher("/mapper/point_delta", DeltaPoint, queue_size = 10).publish

def publish_new_message(xyz_list, delta_time):
    global DeltaPointPublish
    msg = DeltaPoint()
    msg.point = xyz_list
    msg.delta = delta_time
    rospy.loginfo("next_point: %s", xyz_list)
    DeltaPointPublish(msg)

def calculate_new_destination(delta_time):
    global LINK1, LINK2, LINK3, LINK4, FULL_HEIGHT, ROTATION_AMOUNT, INITIAL_STATE, current_angle, current_state

    #rospy.loginfo("Recieved: %s", delta_time.data)
    #Rotate around link 1:
    current_angle += ROTATION_AMOUNT
    if (current_angle >= 2*PI):
        current_angle = 0

    #Move up/down
    #Currently changes between "full length" and "full length" but 0.9 in x/y dir and higher
    x, y, z, = INITIAL_STATE[0], INITIAL_STATE[1], INITIAL_STATE[2]
    if (current_state == "up"):
        current_state = "down"
        new_position = [ x * math.cos(current_angle), y * math.sin(current_angle), z]
    else:
        current_state = "up"
        new_position = [0.9 * x * math.cos(current_angle), 0.9 * y * math.sin(current_angle), z + math.sqrt(1 - (0.9**2))]

    publish_new_message(new_position, delta_time.data)

# ----------- INIT FUNCTION -----------
def listener():
    rospy.Subscriber("/planner/delta_beat", Float32, calculate_new_destination)
    rospy.spin()



if __name__ == '__main__':
    try:
		rospy.init_node("point_to_point_mapper")
		listener()
    except rospy.ROSInterruptException:
        pass
