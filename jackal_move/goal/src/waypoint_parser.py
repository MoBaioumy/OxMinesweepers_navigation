#!/usr/bin/env python

import rospy
import os
from set_goal import set_goal

def parser(path_name):
	file_obj=open(path_name,"r")
	for coord in file_obj:
		pose=coord.split()
		print(pose)
		set_goal(float(pose[0]),float(pose[1]),float(pose[2]))

if __name__ == '__main__':
    rospy.init_node('waypoint_parser')
    #Enter the full path of the coordinates
    #Coordinates must be in the format
    #x y arg
    input_file = rospy.get_param("/waypoint_parser/waypoints_file")
    parser(input_file)
