#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 

def callback(data):
      rospy.loginfo(rospy.get_caller_id() + "모터값 출력: %d", data.data)

def print_angle():
      rospy.init_node('steering_result',anonymous=True) #노드명 초기화 

      rospy.Subscriber("angle", Int64, callback)

      rospy.spin()

if __name__=='__main__':
      print_angle()



