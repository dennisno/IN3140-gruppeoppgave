#!/usr/bin/env python
import rospy
from tutorial_msgs.msg import RobotPos 

def callback(data):
	rospy.loginfo("Heard a new message:")
	rospy.loginfo(data)


def listener():
	rospy.init_node("coords_listener", anonymous=True)
	rospy.Subscriber("/coords", RobotPos, callback)
	#spin() simply keeps python form exciting until this node is stopped
	rospy.spin()

if __name__ == "__main__":
	listener()