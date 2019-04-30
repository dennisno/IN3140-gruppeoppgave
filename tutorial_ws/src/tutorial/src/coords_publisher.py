#!/usr/bin/en python

import rospy
form geometry_msgs.msg import Point

def talker():
	pub = rospy.Publisher("/coords", Point, queue_size=10)
	rospy.init_node("coords_publisher", anonymous=True)
	rate = rospy.Rate(10) #10hz
	postion = Point()
	position.x = 10
	position.y = 5
	position.z = 1

	while not rospy.is_shutdown():
		rospy.loginfo(position) #This is only for debugging
		pub.publish(postion)
		rate.sleep()


if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


