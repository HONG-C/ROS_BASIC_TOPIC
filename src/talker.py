#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy	#ros 내에서 파이썬 사용을 위한 파일 
from std_msgs.msg import String#기본 메시지 파일 불러오기 

def talker():
      pub = rospy.Publisher('chatter',String,queue_size=10)
      rospy.init_node('talker', anonymous = True)
      rate = rospy.Rate(10) #10hz
      while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()

if __name__=='__main__':
      try:
            talker()
      except rospy.ROSInterruptException:
            pass

