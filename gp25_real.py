#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from geometry_msgs.msg import PoseStamped

try:
    	from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    	from math import pi, fabs, cos, sqrt


def callback(data):
	
       	rospy.loginfo("POSITION: %s",data.pose.position)
      	rospy.loginfo("ORIENTATION: %s",data.pose.orientation)

	print("++++++++ BIENVENIDO AL PROGRAMA")
	modo = int(input("+++++++ Seleccione el modo de funcionamiento: "))

    	if modo == 1:
        	
		while 1==1:

			# DISTANCIA CON LA CAMARA
			x = 0
			y = 0
			z = 0

			# LIMITES DE MOVIMIENTO
			q_1_min = 1.3029271364212036
			q_1_max = 2.1799113750457764

			# CALCULO DE MATRICES
			A=np.array([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])
			B=np.array([[data.pose.position.x],[data.pose.position.y],[data.pose.position.z],[1]])
			m_1 = np.dot(A,B)
			print("Punto inicial del robot imaginario= ", m_1)

			# CALCULO DE VARIACION DE A DISTANCIA DE LA CAMARA
			m_1[0] = (102.8637805883*m_1[0]+38.9345353973)*0.01
			m_1[1] = (-103.9789227986*m_1[1]+38.4841950323)*0.01
			m_1[2] = (297.8461147631*m_1[2]+1.04685057)*0.01
			print("Punto inicial del robot real= ", m_1)

			# CALCULO Q1
			if m_1[0] == 0:
				q_1 = pi/2

			else:

				q_1 = np.arctan(m_1[1]/m_1[0])
				print("Punto q_1= ",q_1[0])
			
			# SI EL VALOR DE Q1 ES MENOR QUE EL MINIMO, IR AL MINIMO
			if q_1_min > q_1[0]:
				q_1[0] = 1.3029271364212036
				os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '["+str(q_1)+", 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

			# SI EL VALOR DE Q1 ES MAYOR QUE EL MAXIMO, IR AL MAXIMO
			elif q_1_max < q_1[0]:
				q_1[0] = 2.1799113750457764
				os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '["+str(q_1)+", 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

			# SI EL VALOR ESTA DENTRO DEL RANGO IR AL Q1 CALCULADO
			elif q_1_min =< q_1[0] =< q_1_max
				os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '["+str(q_1)+", 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

			# POR SEGURIDAD IR AL CENTRO
			else
				os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[1.5332036018371582, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")


	else:
		print("ROBOT ACTIVO")
		print("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[2.1799113750457764, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")
		#os.system ("/home/carlos/catkin_ws/src/motoman/motoman_gp25_config_2/scripts/move_to_joint.py '[2.1799113750457764, 0.9076073169708252, 0.08347046375274658, -0.08227870613336563, -0.6823795437812805, 3.2575197219848633]' ")

def listener():

        #rospy.init_node('joint_states_listener')
	print("PULSE ENTER PARA COGER INFORMACION")
	input()

	control_subscriber=rospy.Subscriber('/visp_auto_tracker/object_position', PoseStamped, callback)

	rospy.spin()

if __name__ == '__main__':
	listener()    	
	

