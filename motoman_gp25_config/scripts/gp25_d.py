#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from std_msgs.msg import String

def gp25_python_interface():

  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('gp25_python_interface', anonymous=True)

  robot = moveit_commander.RobotCommander()

  scene = moveit_commander.PlanningSceneInterface()

  brazo = moveit_commander.MoveGroupCommander("Motoman")

  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

  print "============ Esperando a que RVIZ se abra ..."
  rospy.sleep(1)

  print "============ Reference frame: %s" % brazo.get_planning_frame()

  print "============ Reference frame: %s" % brazo.get_end_effector_link()
  
  print "============ Robot Groups:"
  print robot.get_group_names()

  print "============ Printing robot state"
  print robot.get_current_state()
  print "============"


  ## PLANNING TO A POSE GOAL
  ## ^^^^^^^^^^^^^^^^^^^^^^^
  ## We can plan a motion for this group to a desired pose for the end-effector
  
  print "============ Generating plan 1"
  pose_target = geometry_msgs.msg.Pose()
  pose_target.orientation.w = 0.6878
  pose_target.position.x = 0.752
  pose_target.position.y = -0.895
  pose_target.position.z = 0.354
  brazo.set_pose_target(pose_target)
	
  ## Now, we call the planner to compute the plan and visualize it if successful
  plan1 = brazo.plan()

  print "============ Waiting while RVIZ displays plan1"
  rospy.sleep(2)

  print "============ Visualizing plan1"
  display_trajectory = moveit_msgs.msg.DisplayTrajectory()

  display_trajectory.trajectory_start = robot.get_current_state()
  display_trajectory.trajectory.append(plan1)
  display_trajectory_publisher.publish(display_trajectory);

  print "============ Waiting while plan1 for left arm is visualized again"
  rospy.sleep(2)

if __name__=='__main__':
  try:
    gp25_python_interface()
  except rospy.ROSInterruptException:
    pass








