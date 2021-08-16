#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import Int64#기본 메시지 파일 불러오기 
#float 64형의 경우에는 하위 데이터 data가 있음 

motor_angle=0

def callback(data):
      global motor_angle
      rospy.loginfo(rospy.get_caller_id() + "모터값 출력: %d", data.data)
      motor_angle=data.data

def print_angle():
      global motor_angle
      rospy.init_node('steering_result_pub',anonymous=True) #노드명 초기화 
      pub = rospy.Publisher('your_topic',Int64,queue_size=10)
      rospy.Subscriber("angle", Int64, callback)
      pub.publish(motor_angle)
      rospy.spin()

if __name__=='__main__':
      print_angle()



