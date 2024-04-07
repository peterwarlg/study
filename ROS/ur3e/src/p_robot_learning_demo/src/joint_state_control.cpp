#include<iostream> 
#include <string> 
#include <ros/ros.h> 
#include <sensor_msgs/JointState.h> 
#include <robot_state_publisher/robot_state_publisher.h> 

using namespace std; 

int main(int argc, char** argv) 
{ 
	ros::init(argc, argv, "state_1_publisher"); //节点的名称 
	ros::NodeHandle n; 
	ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1); //设置一个发布者，将消息发布出去,发布到相应的节点中去 
	ros::Rate loop_rate(10); //这个设置的太大，效果很不好，目前觉得为10最好了 
	//const double degree = M_PI/180; 
	const double radius = 2;
	double angle=0;
	sensor_msgs::JointState joint_state;
	//int i=-69; 
	while (ros::ok()) 
	{ 
		//update joint_state 
		joint_state.header.stamp = ros::Time::now(); 
		joint_state.name.resize(6); 
		joint_state.position.resize(6); 
		joint_state.name[0]="shoulder_pan_joint"; 
		joint_state.position[0] = -0.2; 
		joint_state.name[1] ="shoulder_lift_joint"; 
		joint_state.position[1] = 0.036; 
		joint_state.name[2] ="elbow_joint"; 
		joint_state.position[2] = -1.368; 
		joint_state.name[3] ="wrist_1_joint"; 
		joint_state.position[3] = -0.045; 
		joint_state.name[4] ="wrist_2_joint"; 
		joint_state.position[4] = 2.336; 
		joint_state.name[5] ="wrist_3_joint"; 
		joint_state.position[5] = -2.865; 
		//if(i<=70) 
		//	i++; 
		//else 
		//	i=-69; 
			
		//send the joint state and transform 
		joint_pub.publish(joint_state);
		
		// This will adjust as needed per iteration 
		loop_rate.sleep(); 
	} 
	
	return 0; 
	
}

