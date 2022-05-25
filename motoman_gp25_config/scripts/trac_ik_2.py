#!/usr/bin/env python

from trac_ik_python.trac_ik import IK

ik_solver = IK("torso_lift_link",
               "r_wrist_roll_link")

seed_state = [0.0] * ik_solver.number_of_joints

ik_solver.get_ik(seed_state,
                0.45, 0.1, 0.3,
                0.0, 0.0, 0.0, 1.0,
                0.01, 0.01, 0.01,  # X, Y, Z bounds
                0.1, 0.1, 0.1)  # Rotation X, Y, Z bounds
                )
# Returns:
# (0.5646018385887146,
#  0.04759637706046231,
#  0.026629718805901908,
#  -1.5106828886580062,
#  2.5541685245726535,
#  -1.4663448384900402,
#  -3.104163452483634)
