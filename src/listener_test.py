#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
      rospy.loginfo(rospy.get_caller_id() + "I heard %f",data.linear.x)

def listener_test():
      rospy.init_node('listener_test',anonymous=True)

      rospy.Subscriber("turtle1/cmd_vel",Twist, callback)

      rospy.spin()

if __name__=='__main__':
      listener_test()



