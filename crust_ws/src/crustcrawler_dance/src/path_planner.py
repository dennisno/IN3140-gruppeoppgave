#!/usr/bin/env python

"""
This node is designed to take in a circle drawing description and perform
the necessary calculations and commands to draw the circle using the
Crustcrawler platform
"""

from __future__ import print_function
from std_msgs.msg import UInt32
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryGoal
from control_msgs.msg import JointTolerance
from trajectory_msgs.msg import JointTrajectoryPoint
from crustcrawler_dance.msg import DeltaAngles
import actionlib
import numpy as np
import rospy
from InverseKinematic import inverse



def create_trajectory_point(position, seconds):
    """
    Create a JointTrajectoryPoint

    :param position: Joint positions
    :param seconds: Time from start in seconds
    :returns: JointTrajectoryPoint
    """
    point = JointTrajectoryPoint()
    point.positions.extend(position)
    point.time_from_start = rospy.Duration(seconds)
    return point

class trajectoryObject():
    def __init__(self):
        self.time = 0.
        self.point_counter = 0
        self.max_messages = 100
        self.movement = FollowJointTrajectoryGoal()
        self.movement.trajectory.joint_names.extend(['joint_1', 'joint_2', 'joint_3'])
        self.movement.goal_tolerance.extend([
            JointTolerance('joint_1', 0.1, 0., 0.),
            JointTolerance('joint_2', 0.1, 0., 0.),
            JointTolerance('joint_3', 0.1, 0., 0.)])
        self.movement.goal_time_tolerance = rospy.Duration(0.5)
	
	def set_point_cap(self, int_msg):
		rospy.loginfo("Trajectory Planner: Got number of trajectory points: %s", int_msg.data)
		self.max_messages = int_msg.data

    def add_point(self, delta_angles_message):
        self.time += delta_angles_message.delta
        self.movement.trajectory.points.append(create_trajectory_point(delta_angles_message.angles, self.time))
        self.point_counter += 1
        if (self.point_counter >= self.max_messages):
            self.create_joint_trajectory()


    def create_joint_trajectory(self):
        rospy.loginfo("Now ready to move the arm!")
        client = actionlib.SimpleActionClient(
                '/crustcrawler/controller/follow_joint_trajectory',
                FollowJointTrajectoryAction)
		
        client.wait_for_server()
        #Send start to player --> Rethink right syncing?
        rospy.Publisher('/player/start_music', Bool, queue_size=1).publish(True);
      
        # Send goal
        client.send_goal(self.movement)
        # Wait for arm to perform our movement
        client.wait_for_result()
        # Finally print status of arm, did it work or not?
        result = client.get_result()
        if not result.error_code:
            print("Crustcrawler done!")
        else:
            print("Crustcrawler failed due to: '{!s}'({!s})"
                  .format(result.error_string, result.error_code))
        return result.error_code

myTrajectory = trajectoryObject()
def get_max_msg(int_msg):
	global myTrajectory
	myTrajectory.set_point_cap(int_msg)
	
def set_point(DA_msg):
	global myTrajectory
	myTrajectory.add_point(DA_msg)


# -------------- INIT FUNCTION ----------------
def talker(): #point_description
    rospy.Subscriber('/inverse/joint_angles', DeltaAngles, set_point) #myTrajectory.add_point)
    # rospy.Subscriber("MultiControllerState", DeltaAngles, myTrajectory.add_point) #--By passing Timed Move Queue, as the entire path is compiled at once!
    rospy.Subscriber("/planner/controller_max_points", UInt32, get_max_msg)
    rospy.spin()



if __name__ == '__main__':
    try:
        rospy.init_node("Path_planner")
        talker()
    except rospy.ROSInterruptException:
        sys.exit("Program aborted during movement")
