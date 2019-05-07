# To add:
# - Dependencies
#     - Dennis sin publisher
#     - Ros
# -

#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def publish_new_message(data):
    pub = rospy.Publisher("/Next_point_channel", Int32, queue_size = 10)

def calculate_new_destination(data):
    rospy.loginfo("Recieved: %s", data.data)


def listener():
    rospy.init_node("point_to_point_mapper")
    sub = rospy.Subscriber("/BeatPlanPub", Int32, calculate_new_destination)
    rospy.spin()
