#!/usr/bin/env python

#This node is disabled

import rospy
import time

from std_msgs.msg import Bool
from std_msgs.msg import Float32
from crustcrawler_dance.msg import DeltaAngles
from queue import LifoQueue

beat_queue = LifoQueue()
def print_queue(float_msg):
	global beat_queue
	if float_msg.data != -1.0:
		beat_queue.put(float_msg.data)
		return
	
	rospy.loginfo("Starting Ticking!")
	state = 0
	msg = (" Tick! | - - - | - - - | - - - ", " - - - | Tock! | - - - | - - - ", " - - - | - - - | Tack! | - - - ", " - - - | - - - | - - - | Wack! ")
	#cached = rospy.get_time()
	while not beat_queue.empty():
		#rospy.sleep(beat_queue.get() + cached - rospy.get_time() )
		#cached = rospy.get_time()
		rospy.sleep(beat_queue.get() - 0.1)
		rospy.loginfo(msg[state])
		state = (state + 1) % 4
		
		

# ----------- INIT FUNCTION -----------
def create_queue():
	rospy.Subscriber('/planner/tick', Float32, print_queue)
	rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('ticker', anonymous=True)
        create_queue()
    except rospy.ROSInterruptException:
        pass
