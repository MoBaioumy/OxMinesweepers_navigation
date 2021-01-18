#!/usr/bin/env python

import rospy
import os
from set_goal import set_goal

if __name__ == '__main__':
	rospy.init_node('movebase_client_parser')
	#Enter the full path of the coordinates
	#Coordinates must be in the format
	#x y arg
	input_file="/home/daoxin/OXMinesweeper/src/jackal_move/goal/src/objective.txt"
	file_obj=open(input_file,"r")
	for coord in file_obj:
		pose=coord.split()
		print(pose)
		set_goal(float(pose[0]),float(pose[1]),float(pose[2]))
