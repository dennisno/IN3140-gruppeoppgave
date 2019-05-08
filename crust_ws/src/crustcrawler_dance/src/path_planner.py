#!/usr/bin/env python

"""
This node is designed to take in a circle drawing description and perform
the necessary calculations and commands to draw the circle using the
Crustcrawler platform
"""

from __future__ import print_function
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
        sefl.movement.goal_tolerance.extend([
            JointTolerance('joint_1', 0.1, 0., 0.),
            JointTolerance('joint_2', 0.1, 0., 0.),
            JointTolerance('joint_3', 0.1, 0., 0.)])
        self.movement.goal_time_tolerance = rospy.Duration(0.5)


    def add_point(delta_angles_message):
        self.time += delta_angles_message.delta
        self.movement.trajectory.points.append(create_trajectory_point(delta_angles_message.angles, time))
        self.point_counter += 1
        if (self.point_counter >= self.max_messages):
            create_joint_trajectory():


    def create_joint_trajectory():
        client = actionlib.SimpleActionClient(
                '/crustcrawler/controller/follow_joint_trajectory',
                FollowJointTrajectoryAction)

        client.wait_for_server()
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

def talker(point_description):
    myTrajectory = trajectoryObject()
    rospy.Subscriber("MultiControllerState", DeltaAngles, myTrajectory.add_point)
    rospy.spin()





if __name__ == '__main__':
    try:
        rospy.init_node("Path_planner")
        talker()
    except rospy.ROSInterruptException:
        sys.exit("Program aborted during circle drawing")


        # --- RELIC OF THE PAST ---
        # def draw_circle(origin, radius, num, angle, axis):
        #     """
        #     Draw circle using Crustcrawler
        #
        #     :param origin: 3D point of circle origin
        #     :param radius: Radius of circle in centimeters
        #     :param num: Number of points in circle
        #     :param angle: Angle to rotate circle by
        #     :param axis: Unit vector to rotate circle around
        #     """
        #     # First start by creating action client, this is responsible for passing
        #     # our parameters and monitoring the Crustcrawler during operations
        #     client = actionlib.SimpleActionClient(
        #             '/crustcrawler/controller/follow_joint_trajectory',
        #             FollowJointTrajectoryAction)
        #     # Generate circle path
        #     path = generate_path(origin, radius, num, angle, axis)
        #     # Generate arm movement path
        #     goal = generate_movement(path)
        #     # Wait for arm to respond to action client
        #     client.wait_for_server()
        #     # Send goal
        #     client.send_goal(goal)
        #     # Wait for arm to perform our movement
        #     client.wait_for_result()
        #     # Finally print status of arm, did it work or not?
        #     result = client.get_result()
        #     if not result.error_code:
        #         print("Crustcrawler done!")
        #     else:
        #         print("Crustcrawler failed due to: '{!s}'({!s})"
        #               .format(result.error_string, result.error_code))
        #     return result.error_code


# --- RELIC ---
# def generate_path(origin, radius, num, angle, axis):
#     """
#     Generate path in 3D space of where to draw circle
#
#     :param origin: 3D point of circle origin
#     :param radius: Radius of circle in centimeters
#     :param num: Number of points in circle
#     :param angle: Angle to rotate circle by
#     :param axis: Unit vector to rotate circle around
#     :returns: List of points to draw
#     """
#     path = []
#     distance_between = (2.0 * np.pi) / float(num)
#     for i in range(num + 1):
#         index = i * distance_between
#         path.append(radius * np.array([np.cos(index), np.sin(index), 0.0]))
#
#     # Rotate using the rotation function
#     path = rotate_path(path, angle, axis)
#     # Add origin to path:
#     path = [p + origin for p in path]
#     return path

#Relic from source code, not yet implemented
# def rotate_path(path, angle, axis):
#     """
#     Rotate all elements of a path by angle-axis rotation
#
#     :param path: List of points
#     :param angle: Angle in radians to rotate by
#     :param axis: Unit vector to rotate around
#     :returns: List of rotated points
#     """
#     # TODO: Implement angle-axis rotation
#     return path


# def path_length(path):
#     """
#     Calculate path length in centimeters
#
#     :param path: List of points
#     :returns: Length of path in centimeters
#     """
#     length = 0.0
#     for p1, p0 in zip(path[1:], path):
#         length += np.linalg.norm(p1 - p0)
#     return length

# def inverse_kinematic(position):
#     """
#     Calculate the inverse kinematic of the Crustcrawler
#
#     :param position: Desired end-point position
#     :returns: Three element vector of joint angles
#     """
#     # TODO: Implement inverse kinematics function using your equations from assignment 1 task 5).
#     return inverse(position)


# def generate_path(coordinates):
#     """
#     Generate path in 3D space of where to draw circle
#
#     :param origin: 3D point of circle origin
#     :param radius: Radius of circle in centimeters
#     :param num: Number of points in circle
#     :param angle: Angle to rotate circle by
#     :param axis: Unit vector to rotate circle around
#     :returns: List of points to draw
#     """
#     path = []
#     distance_between = (2.0 * np.pi) / float(num)
#     for i in range(num + 1):
#         index = i * distance_between
#         path.append(radius * np.array([np.cos(index), np.sin(index), 0.0]))
#
#     # Rotate using the rotation function
#     path = rotate_path(path, angle, axis)
#     # Add origin to path:
#     path = [p + origin for p in path]
#     return path

# def generate_movement(path):
#     """
#     Generate Crustcrawler arm movement through a message
#
#     :param path: List of points to draw
#     :returns: FollowJointTrajectoryGoal describing the arm movement
#     """
#     movement = FollowJointTrajectoryGoal()
#     # Names describes which joint is actuated by which element in the coming
#     # matrices
#     movement.trajectory.joint_names.extend(['joint_1', 'joint_2', 'joint_3'])
#     # Goal tolerance describes how much we allow the movement to deviate
#     # from true value at the end
#     movement.goal_tolerance.extend([
#         JointTolerance('joint_1', 0.1, 0., 0.),
#         JointTolerance('joint_2', 0.1, 0., 0.),
#         JointTolerance('joint_3', 0.1, 0., 0.)])
#     # Goal time is how many seconds we allow the movement to take beyond
#     # what we define in the trajectory
#     movement.goal_time_tolerance = rospy.Duration(0.5)  # seconds
#     time = 4.0  # Cumulative time since start in seconds
#     movement.trajectory.points.append(create_trajectory_point([0., 0., np.pi / 2.], time))
#     # Add initial point, also as a large time fraction to avoid jerking
#     time += 4.0
#     movement.trajectory.points.append(
#         create_trajectory_point(inverse_kinematic(path[0]), time))
#     # Calculate total circle length
#     length = path_length(path)
#     # Calculate how much time we have to process each point of the circle
#     time_delta = (length / 2.) / len(path)
#     for point in path[1:]:
#         time += time_delta
#         movement.trajectory.points.append(create_trajectory_point(inverse_kinematic(point), time))
#     time += 4.0
#     movement.trajectory.points.append(create_trajectory_point([0., 0., np.pi / 2.], time))
#     return movement
