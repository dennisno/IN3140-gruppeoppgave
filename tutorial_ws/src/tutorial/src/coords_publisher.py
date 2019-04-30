#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Point
from tutorial_msgs.msg import RobotPos

def talker():
	#pub = rospy.Publisher("/coords", Point, queue_size=10)
	pub = rospy.Publisher("/coords", RobotPos, queue_size=10) 
	rospy.init_node("coords_publisher", anonymous=True)
	rate = rospy.Rate(10) #10hz
	#position = Point()
	#position.x = 10
	#position.y = 5
	#position.z = 1
	position = RobotPos()
	position.name = "Spiderman dies in Infinity War"
	position.pos.x = 10
	position.pos.y = 5
	position.pos.z = 1

	ctr = 0
	while not rospy.is_shutdown():
		position.pos.x = math.cos(ctr)
		position.pos.y = math.sin(ctr)		
		ctr += 0.2		
		rospy.loginfo(position) #This is only for debugging
		pub.publish(position)
		rate.sleep()
		

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


