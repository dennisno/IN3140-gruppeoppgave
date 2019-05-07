import numpy as np
import warnings
warnings.filterwarnings("error")
L1 = 100.9
L2 = 222.1
L3 = 136.2
PI = np.pi

def forwardMatrix(angle1, angle2, angle3):
    """returns the transformation-matrix from p (the tip) to B (base)"""
    T_ptoB = np.array([[np.cos(angle2 + angle3)*np.cos(angle1), -np.sin(angle2+angle3)*np.cos(angle1), np.sin(angle1), np.cos(angle1)*(L3*np.cos(angle2+angle3) + L2*np.cos(angle2))],
    [np.cos(angle2 + angle3)*np.sin(angle1), -np.sin(angle2+angle3)*np.sin(angle1), -np.cos(angle1), np.sin(angle1)*(L3*np.cos(angle2+angle3) + L2*np.cos(angle2))],
    [np.sin(angle2 + angle3), np.cos(angle2 + angle3), 0, L1 + L3*np.sin(angle2 + angle3) + L2*np.sin(angle2)],
    [0, 0, 0, 1]])
    return T_ptoB

def forward(joint_angles):
    """returns cart_cord"""
    angle1 = joint_angles[0]
    angle2 = joint_angles[1]
    angle3 = joint_angles[2]

    T_ptoB = forwardMatrix(angle1, angle2, angle3)
    cart_cord = T_ptoB[:,-1]
    return cart_cord


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
    return joint_angles

def hovedprogram():
    #Oppgave c:
    print("\n\nOppgave c")
    inputPosition1 = -100
    inputPosition2 = 100
    inputPosition3 = -200

    print("Inverskinematikk, så foroverkinematikk på [" + str(inputPosition1), inputPosition2, str(inputPosition3) + "]\nForventer 4 svar:")
    inverseKin = inverse([inputPosition1, inputPosition2, inputPosition3])
    for solution in inverseKin:
        forwardKin = forward(solution)
        print(np.round(forwardKin, 4))


    inputPosition1 = 0
    inputPosition2 = 0
    inputPosition3 = 200

    print("Inverskinematikk, så foroverkinematikk på [" + str(inputPosition1), inputPosition2, str(inputPosition3) + "]\nForventer å få ett svar:")
    inverseKin = inverse([inputPosition1, inputPosition2, inputPosition3])
    for solution in inverseKin:
        forwardKin = forward(solution)
        print(np.round(forwardKin, 4))

    inputPosition1 = L2+L3
    inputPosition2 = 0
    inputPosition3 = L1

    print("Inverskinematikk, så foroverkinematikk på [L2+L3", inputPosition2, "L1]\nForventer å få 2 svar:")
    inverseKin = inverse([inputPosition1, inputPosition2, inputPosition3])
    for solution in inverseKin:
        forwardKin = forward(solution)
        print(np.round(forwardKin, 4))


    #Oppgave d
    print("\n\nOppgave d")
    print("Forventer å få i hvert fall:", np.round([-PI/2, PI/6, -PI/4], 4))

    inputPosition1 = 0
    inputPosition2 = -323.9033
    inputPosition3 = 176.6988

    print("Faktisk resultat")
    inverseKin = inverse([inputPosition1, inputPosition2, inputPosition3])
    for solution in inverseKin:
        print(np.round(solution, 4))

hovedprogram()
