#!/usr/bin/env python

from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool
from DeltaPoint.msg import DeltaPoint
from DeltaAngles.msg import DeltaAngles

import rospy
import pyglet
import numpy as np
import warnings

def inverse(cart_cord):
    """
    Returns all sets of joint_angles as a list of lists.
    If the size of the list is 1, there are infinite solutions
    If the size of the list is 2, there are 2 solutions, both on the border of the workspace.
    If the size of the list is 4, there are 4 solutions, which is the normal case. 
    """
    xbase = cart_cord[0]
    ybase = cart_cord[1]
    zbase = cart_cord[2]
    joint_angles = []
    try:
        if (xbase == 0 and ybase == 0):
            #Håndterer tilfellet der det er uendelig antall løsninger
            angle1 = 0

            D = ((zbase-L1)**2 - L2**2 - L3**2)/(2*L2*L3)
            angle3 = np.arctan2(np.sqrt(1-D**2), D)

            angle2 = np.arctan2(zbase-L1, 0) - np.arctan2(L3*np.sin(angle3), L2 + L3*np.cos(angle3))
            joint_angles = [[angle1, angle2, angle3]]
        else:
            #Hvis lengden på armen er akkurat lik avstanden til punktet, får vi kun 2 løsninger
            if((L2 + L3)**2 == (xbase**2 + ybase**2 + (zbase-L1)**2)):
                angle1_1 = np.arctan2(ybase, xbase)
                angle3_1 = 0
                angle2_1 = np.arctan2(zbase-L1, np.sqrt(xbase**2 + ybase**2))

                angle1_2 = PI + angle1_1
                angle3_2 = 0
                angle2_2 = PI - angle2_1
                joint_angles = [[angle1_1, angle2_1, angle3_1], [angle1_2, angle2_2, angle3_2]]
            else:
                #Angle(vinkelnavn)_(forover eller revers, basert på hvilken vinkel1)(albue-konfigurasjon nummer 1 eller 2)
                #D er et uttrykk til uregning av vinkel 3
                D = (xbase**2 + ybase**2 + (zbase-L1)**2 - L2**2 - L3**2)/(2*L2*L3)

                #Elbow down for normal vinkel1:
                angle1_1 = np.arctan2(ybase, xbase)
                angle3_11 = np.arctan2(np.sqrt(1-D**2), D)
                angle2_11 = np.arctan2(zbase-L1, np.sqrt(xbase**2 + ybase**2)) - np.arctan2(L3*np.sin(angle3_11), L2 + L3*np.cos(angle3_11))

                #Elbow up for normal vinkel1:
                angle3_12 = np.arctan2(-np.sqrt(1-D**2), D)
                angle2_12 = np.arctan2(zbase-L1, np.sqrt(xbase**2 + ybase**2)) - np.arctan2(L3*np.sin(angle3_12), L2 + L3*np.cos(angle3_12))

                #Elbow down for reversert vinkel1:
                angle1_2 = PI + angle1_1
                angle2_21 = PI - angle2_11
                angle3_21 = -angle3_11

                #Elbow up for reversert vinkel1:
                angle2_22 = PI - angle2_12
                angle3_22 = -angle3_12

                joint_angles = [[angle1_1, angle2_11, angle3_11], [angle1_1, angle2_12, angle3_12], [angle1_2, angle2_21, angle3_21], [angle1_2, angle2_22, angle3_22]]

    except RuntimeWarning:
        print("Point outside of work area")
    return joint_angles[0]

def calculate_inverse(data):
    cart_cord = [data.point[0], data.point[1], data.point[2]]
    delta_time = data.delta
    joint_angles = inverse(cart_cord)
    joint_angles.append(delta_time)
    talker(joint_angles)

# ----------- INIT FUNCTION -----------
def listener():
    sub = rospy.Subscriber("/Next_point_channel", DeltaPoint, calculate_inverse)

def talker(joint_angles):
    DeltaAngles.angle[0] = joint_angles[0]
    DeltaAngles.angle[1] = joint_angles[1]
    DeltaAngles.angle[2] = joint_angles[2]
    DeltaAngles.delta = joint_angles[3]
    pub = rospy.Publisher('/Next_joint_angle', DeltaAngles, queue_size = 1)
    #rospy.init_node('joint_angles', anonymous = True)
    rospy.loginfo('joint_angles')
    pub.publish(DeltaPoint)


if __name__ == '__main__':
    try:
		rospy.init_node("Points")
        listener()
    except rospy.ROSInterruptException:
        pass
