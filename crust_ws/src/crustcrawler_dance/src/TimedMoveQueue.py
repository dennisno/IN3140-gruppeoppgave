#!/usr/bin/env python


import rospy
import time

from std_msgs.msg import Bool
from crustcrawler_dance.msg import DeltaAngles

func = None
wait_time = 0
DeltaAnglesPublish = rospy.Publisher('MultiControllerState', DeltaAngles, queue_size=1).publish

def callback(event):
    global func
    func(event)

def spin_start(event):
    #After this launch function make shure the object points to the correct spin function
    global DeltaAnglesPublish, wait_time, func
    func = spin
    rospy.sleep(5)
    DeltaAnglesPublish(event)
    wait_time = event.delta + (rospy.get_time() * 100)
    
    #Send start to player --> Rethink right syncing?
    rospy.Publisher('StartMusic', Bool, queue_size=1).publish(True);

def spin(event):
    global DeltaAnglesPublish, wait_time

    while (100 * rospy.get_time()) < wait_time:
        rospy.sleep((wait_time/100) - rospy.get_time())
    rospy.loginfo("Event sendt to controller!")
    DeltaAnglesPublish(event)
    wait_time += event.delta

# ----------- INIT FUNCTION -----------
def create_queue():
    global func
    func = spin_start
    rospy.Subscriber('/Next_joint_angle', DeltaAngles, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('timed_queue', anonymous=True)
        create_queue()
    except rospy.ROSInterruptException:
        pass
