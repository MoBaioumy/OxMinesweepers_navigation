#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def inject_twist(speed, turn ):
    pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('set_jackal_odom', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        custom_twist=Twist()
	custom_twist.linear.x=speed
	custom_twist.angular.z=turn       
	
        pub.publish(custom_twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        inject_twist(-0.5,-0.5)
    except rospy.ROSInterruptException:
        pass
