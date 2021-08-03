#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 

def read_angle():
      pub = rospy.Publisher('angle',Int64,queue_size=10)
      rospy.init_node('steering_angle', anonymous = True)
      rate = rospy.Rate(10) #10hz
      while not rospy.is_shutdown():
      	    angle=input("조향각 얼마?:")
            rospy.loginfo(angle)
            pub.publish(angle)
            rate.sleep()

if __name__=='__main__': #이 구문은 뭘까?import된 경우가 아니라 인터프리터에서 직접 실행된 경우만 if문 이하 실행하기!
      try:
            read_angle()
      except rospy.ROSInterruptException:
            pass

