#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import String#기본 메시지 파일 불러오기 

def callback(data):
      rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
      rospy.init_node('listener',anonymous=True) #노드명 초기화 

      rospy.Subscriber("chatter", String, callback)

      rospy.spin()

if __name__=='__main__':
      listener()



