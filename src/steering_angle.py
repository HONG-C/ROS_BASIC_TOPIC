#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 

def talker():
      pub = rospy.Publisher('angle',Int64,queue_size=10)
      rospy.init_node('steering_angle', anonymous = True)
      rate = rospy.Rate(10) #10hz
      while not rospy.is_shutdown():
      	    angle=input("조향각 얼마?:")
            rospy.loginfo(angle)
            pub.publish(angle)
            rate.sleep()

if __name__=='__main__':
      try:
            talker()
      except rospy.ROSInterruptException:
            pass

