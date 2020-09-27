#!/usr/bin/python3.8

import rospy
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from capture import logger

if __name__ == '__main__':

    #Modelo del robot

    radius = 0.035
 
    alpha_1 = 0.0
    beta_1  = np.pi/2
    l_1    = 0.230

    #Rueda Izquierda
    alpha_2 = np.pi/2
    beta_2  = 0
    l_2     = 0.230

    alpha_3 = np.pi
    beta_3  = -np.pi/2 
    l_3     =  0.230

    #Rueda Derecha
    alpha_4 = -np.pi/2
    beta_4  = np.pi 
    l_4     =  0.230


    J1 = np.array( [( np.sin(alpha_1+beta_1), -np.cos(alpha_1+beta_1), -l_1*np.cos(beta_1)),
                    ( np.sin(alpha_2+beta_2), -np.cos(alpha_2+beta_2), -l_2*np.cos(beta_2)),
                    ( np.sin(alpha_3+beta_3), -np.cos(alpha_3+beta_3), -l_3*np.cos(beta_3)),
                    ( np.sin(alpha_4+beta_4), -np.cos(alpha_4+beta_4), -l_4*np.cos(beta_4))])

    J2=radius*np.identity(4)

    Jacobian = np.matmul(np.linalg.pinv(J2),J1)

    print ("J1: \n", J1)
    print ("J2: \n", J2)
    print ("Jacobian: \n", Jacobian)


    #Inicialización ROS

    rospy.init_node('keyboard_node', anonymous=True)
    rospy.loginfo("Node init")

    nameKeyboardTopic = "/keyboard_input"
    nameLeftWheelTopic = "/left_wheel_controller/command"
    nameRightWheelTopic = "/right_wheel_controller/command"

    keyboard_pub = rospy.Publisher(nameKeyboardTopic, Twist, queue_size=10)
    left_wheel_pub = rospy.Publisher(nameLeftWheelTopic, Float64, queue_size=10)
    right_wheel_pub = rospy.Publisher(nameRightWheelTopic, Float64, queue_size=10)

    teclado = logger()

    rate = rospy.Rate(20) # 20 Hz

    while (not rospy.is_shutdown()):

        #Obtener v y w de la entrada del teclado

        x, z = teclado.get_targets()
        print("Velocidad Angular: " + str(z))
        print("Velocidad Lineal: " + str(x))

        vel_msg = Twist()

        vel_msg.linear.x = x
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = z

        keyboard_pub.publish(vel_msg)

        command = np.array([0,0,0] , dtype=np.float)

        command[0] = vel_msg.linear.x 
        command[1] = vel_msg.linear.y 
        command[2] = vel_msg.angular.z 

        result = np.matmul(Jacobian, command)

        # Left Wheel
        msgFloat = Float64()
        msgFloat.data = result[1]
        print("Velocidad rueda izquierda:"+str(msgFloat))
        left_wheel_pub.publish(msgFloat)
        
        # Right Wheel
        msgFloat = Float64()
        msgFloat.data = result[3]
        print("Velocidad rueda derecha:"+str(msgFloat))
        right_wheel_pub.publish(msgFloat)

        rate.sleep()

    rospy.spin()
        
