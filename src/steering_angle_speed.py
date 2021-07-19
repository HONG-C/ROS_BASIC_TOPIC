#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 
from ros_basic_topic.msg import Num#직접 만든 메시지 파일 불러오기(ros_basic_topic패키지에 메시지 파일 있고,Num파일을 임포트) 

def read_angle():
      car_data=Num()
      pub = rospy.Publisher('car_data',Num,queue_size=10)
      rospy.init_node('steering_angle_speed', anonymous = True)
      rate = rospy.Rate(10) #10hz
      while not rospy.is_shutdown():
      	    car_data.angle=input("조향각 얼마?:")
      	    car_data.speed=input("속도 얼마?:")
            rospy.loginfo(car_data)
            pub.publish(car_data)
            rate.sleep()

if __name__=='__main__': #이 구문은 뭘까?import된 경우가 아니라 인터프리터에서 직접 실행된 경우만 if문 이하 실행하기!
      try:
            read_angle()
      except rospy.ROSInterruptException:
            pass

