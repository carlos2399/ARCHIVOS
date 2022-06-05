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
	
def main():
	print("hello")
	respuesta = int(input("Dígame su respuesta: "))
	flag=1
    	if respuesta == 1:
        	#q_1 = 2.029271364212036
		#print("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '["+str(q_1)+", 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")
		while 1==1:

			x = 0
		    	y = 0
		    	z = 0

			q_1_min = 1.3029271364212036
			q_1_max = 2.1799113750457764
			
			data.pose.position.x = 0			
			data.pose.position.x = 0
			data.pose.position.x = 0	
		
			q_1_min = 1.3029271364212036
			q_1_max = 2.1799113750457764

		    	A=np.array([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]) 
		    	B=np.array([[data.pose.position.x],[data.pose.position.y],[data.pose.position.z],[1]])
		    	m_1 = np.dot(A,B)  	
			print("Punto inicial del robot imaginario= ", m_1)
	
			m_1[0] = 297.8461147631*m_1[0]+1.04685057
			m_1[1] = 297.8461147631*m_1[1]+1.04685057
			m_1[2] = 297.8461147631*m_1[2]+1.04685057

			m_1[0] = 0.3
			m_1[1] = 2

			print("Punto inicial del robot real= ", m_1)
	
			#CALCULO Q1
		    	if m_1[0] == 0:

				q_1 = pi/2
		    	else:

				q_1 = np.arctan(m_1[1]/m_1[0])
				print("Punto q_1= ",q_1[0])

			if q_1_min <= q_1[0] <= q_1_max:
			os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '["+str(q_1)+", 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")
			
		
 	else:
		print("ROBOT ACTIVO")
		print("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[2.1799113750457764, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")
		#os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[2.1799113750457764, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

if __name__ == '__main__':
	main()    	
	

