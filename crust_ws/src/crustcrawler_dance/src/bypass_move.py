#!/usr/bin/env python


import math
from math import sin, cos
from math import pi as PI
import rospy
from std_msgs.msg import Float32
from crustcrawler_dance.msg import DeltaAngles






strech = [
		(3 * PI / 8, 3 * PI / 8),
		(1 * PI / 8, 1 * PI / 8)
		]
i = 0
base_angle = 0.0
angle_increase = PI / 11
publish = rospy.Publisher('/inverse/joint_angles', DeltaAngles, queue_size = 1).publish
def calculate_new_destination(float_package):
	global publish, base_angle, i, strech, angle_increase
	
	#get_new angle:
	base_angle += angle_increase
	if base_angle >= PI or base_angle <= - PI:
		angle_increase = -angle_increase
	
	i = (i + 1) % len(strech) 
		
	msg = DeltaAngles()
	msg.delta = float_package.data
	(link2, link3) = strech[i]
	msg.angles = (base_angle, link2, link3)
	
	publish(msg)
		
	


def listener():
    rospy.Subscriber("/planner/delta_beat", Float32, calculate_new_destination)
    rospy.spin()

if __name__ == '__main__':
    try:
		rospy.init_node("point_bypasser")
		listener()
    except rospy.ROSInterruptException:
        pass
