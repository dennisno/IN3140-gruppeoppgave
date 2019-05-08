#!/usr/bin/env python


import rospy
import time

from std_msgs.msg import Bool


def spin_start(self, event):
	#After this launch function make shure the object points to the correct spin function
	self.spin = spin
	self.publish(event.angles)
	self.delta_time += event.delta

	#Send start to player --> Rethink right syncing?
<<<<<<< HEAD
	rospy.Publisher('StartMusic', Bool, queue_size=1).publish(True);
>>>>>>> 05cae01a03e2ae51aa1dc4a44061e860b909010f
def spin(self, event):
	while rospy.get_rostime() < self.delta_time:
		time.sleep(self.delta_time - rospy.get_rostime())
	self.publish(event.angles)
	self.delta_time += event.delta

class timed_q(object):
	def __init__(self):
		self.delta_time = rospy.get_rostime()
		self.spin = spin_start
		self.publish = rospy.Publisher('MultiControllerState', Bool, queue_size=1).publish   #--> make it publish the right message!
		

def create_queue():
    rospy.init_node('timed_queue', anonymous=True)
<<<<<<< HEAD
    obj = timed_q()
    rospy.Subscriber('/Next_joint_angle', DeltaAngles, obj.spin)
>>>>>>> 05cae01a03e2ae51aa1dc4a44061e860b909010f
    rospy.spin()

if __name__ == '__main__':
	try:
		create_queue()
	except rospy.ROSInterruptException:
		pass
