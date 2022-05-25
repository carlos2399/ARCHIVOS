#!/usr/bin/env python

from trac_ik_python.trac_ik import IK

# Get your URDF from somewhere
urdf_str = rospy.get_param('/robot_description')

ik_solver = IK("torso_lift_link",
               "r_wrist_roll_link",
               urdf_string=urdf_str)
