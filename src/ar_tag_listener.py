#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import String#기본 메시지 파일 불러오기 
from ar_track_alvar_msgs.msg import AlvarMarkers

def callback(data):
      if len(data.markers)==0:#ar_tag의 값은 리스트로 나오므로, 아무것도 없을 시에는 처리 x
	      rospy.loginfo("NO_AR_TAG")
      if len(data.markers)==1:#ar_tag가 하나 인식될시 처리 
	      id_num=str(data.markers).split('\n')[6]#ar_pose_marker을 문자열 형식으로 변환 후 슬라이싱
      	      rospy.loginfo(id_num)
      else:
	      pass
def listener():
      rospy.init_node('listener',anonymous=True) #노드명 초기화 

      rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback)

      rospy.spin()

if __name__=='__main__':
      listener()



