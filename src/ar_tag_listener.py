#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import String#기본 메시지 파일 불러오기 
from ar_track_alvar_msgs.msg import AlvarMarkers

def callback(data):
      rospy.loginfo(data)

def listener():
      rospy.init_node('listener',anonymous=True) #노드명 초기화 

      rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback)

      rospy.spin()

if __name__=='__main__':
      listener()



