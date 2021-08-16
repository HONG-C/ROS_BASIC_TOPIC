/* 
 * rosserial::std_msgs::Float64 Test
 * Receives a Float64 input, subtracts 1.0, and publishes it
 */

#include <ros.h>
#include <std_msgs/Int64.h>
#include <Servo.h>//include servo headerfile

//To communicate with ros system,setting an nodehandle
ros::NodeHandle nh;
Servo servo;//using Servo class, make servo object

std_msgs::Int64 test;
void messageCb( const std_msgs::Int64& msg)
{
  test.data = msg.data;
  
}


ros::Subscriber<std_msgs::Int64> s("your_topic", &messageCb);


void setup()
{
  servo.attach(7);
  nh.initNode();
  nh.subscribe(s);
  Serial.begin(57600);
}

void loop()
{
  
  if(test.data==250)
  {
    Serial.println("ok");
  }
  else
  {
    Serial.println("not ok");
    //Serial.println(test.data);
  }

  servo.write(test.data);
  //function for starting callback function
  //when message is subscribed, start callback function
  nh.spinOnce();
  
  delay(60);
}
