#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
      rospy.loginfo(data.linear)

def listener_test():
      rospy.init_node('listener_test',anonymous=True)

      #rospy.Subscriber("chatter", String, callback)
      rospy.Subscriber("turtle1/cmd_vel",Twist, callback)
      rospy.spin()

if __name__=='__main__':
      listener_test()



