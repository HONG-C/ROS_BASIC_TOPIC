#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 
from ros_basic_topic.msg import Num#직접 만든 메시지 파일 불러오기(ros_basic_topic패키지에 메시지 파일 있고,Num파일을 임포트) 


def callback(data):
      rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.angle)
      rospy.loginfo(rospy.get_caller_id() + "I heard %d", data.speed)

def print_angle():
      rospy.init_node('steering_speed_result',anonymous=True) #노드명 초기화 

      rospy.Subscriber("car_data", Num, callback)

      rospy.spin()

if __name__=='__main__':
      print_angle()



