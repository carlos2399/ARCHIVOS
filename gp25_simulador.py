#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time
import commands
import os

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

from sensor_msgs.msg import JointState
from std_msgs.msg import String,Float64MultiArray

def my_publisher():
   
    rospy.init_node('my_publisher_control')
    #control_publisher = rospy.Publisher('/joint_states', JointState,queue_size=10)

    while not rospy.is_shutdown():
	msg = JointState()
	msg.header.stamp = rospy.Time.now()
	msg.header.frame_id = ''
	msg.name = ['joint_1_s', 'joint_2_l', 'joint_3_u', 'joint_4_r', 'joint_5_b', 'joint_6_t']
	#msg.position = [pi/2, pi/6, 9.50609628111124e-05, 1.5707001586970428, -2.1052583260461685e-05, 1.0471617598412262]
	msg.position = [1.3029271364212036, 0.9076073169708252, 0.08343759924173355, -0.08227870613336563, -0.6823441386222839, 3.2574872970581055]
	msg.velocity = []
	msg.effort = []

	time.sleep(1)

    	control_publisher.publish(msg)

	rospy.loginfo("PUBLISIHNG DATA")

def main():
	print("hello")
	respuesta = int(input("Dígame su respuesta: "))
	
    	if respuesta == 1:
        	my_publisher()
 	else:
		print("ROBOT ACTIVO")
		os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[2.1799113750457764, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

if __name__ == '__main__':
	main()    	
	
