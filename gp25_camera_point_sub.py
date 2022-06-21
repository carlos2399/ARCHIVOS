#!/usr/bin/env python

import rospy
import numpy as np


try:
	from math import pi, tau, dist, fabs, cos
except: 
	from math import pi, fabs, cos, sqrt

from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String,Float64MultiArray

def callback(data):
	rospy.loginfo("POSITION: %s",data.pose.position)
	rospy.loginfo("ORIENTATION: %s",data.pose.orientation)


	x = 0
	y = 2
	z = 0

	# LIMITES DE MOVIMIENTO
	q_1_min = 1.3029271364212036
	q_1_max = 2.1799113750457764

	data.pose.position.x 
	data.pose.position.y 
	data.pose.position.z 

	# CALCULO DE MATRICES
	A=np.array([[-1,0,0,x],[0,-1,0,y],[0,0,1,z],[0,0,0,1]])
	C=np.array([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
	AC = np.dot(A,C)
	B=np.array([[data.pose.position.x],[data.pose.position.y],[data.pose.position.z],[1]])
	m_1 = np.dot(AC,B)
	print("Punto inicial del robot imaginario= ", m_1)

	# CALCULO DE VARIACION DE A DISTANCIA DE LA CAMARA
	#m_1[0] = (102.8637805883*m_1[0]+38.9345353973)*0.01
	#m_1[1] = (-103.9789227986*m_1[1]+38.4841950323)*0.01
	#m_1[2] = (297.8461147631*m_1[2]+1.04685057)*0.01
	#print("Punto inicial del robot real= ", m_1)


	# CALCULO Q1
	if m_1[0] == 0:

		q_1  = pi/2

	else:

		aux_q1 = np.arctan(m_1[1]/m_1[0])
		q_1=aux_q1[0]	

	print("Punto q_1= ",q_1)
	
def listener():

	rospy.init_node('joint_states_listener')

	control_subscriber=rospy.Subscriber('/visp_auto_tracker/object_position', PoseStamped, callback)

	rospy.spin()

if __name__ == '__main__':
    	listener()
    
