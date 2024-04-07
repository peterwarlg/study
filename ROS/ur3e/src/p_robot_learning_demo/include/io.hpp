#include "ros/ros.h"
#include "ur_msgs/SetIO.h"
#include <cstdlib>

/************************Gripper********************************/
void Right_Gripper(ros::ServiceClient &client,bool iscatch, int sleep_time)
{
	sleep(0.2);
	ur_msgs::SetIO srv;
	srv.request.fun= 1;//digital mode
	srv.request.pin = 0;//io_0
	
	if(iscatch)
		srv.request.state =1;//high_level
	else
		srv.request.state =0;//low_level

	if (client.call(srv))
	{
	    ros::Duration(sleep_time).sleep();
	    ROS_INFO("Success: %d", (bool)srv.response.success);
		
	}
	else
	{
	    ROS_ERROR("Failed to call service");
	}
}

void Left_Gripper(ros::ServiceClient &client, bool iscatch, int sleep_time)
{
	sleep(0.2);
	ur_msgs::SetIO srv;
	srv.request.fun= 1;//digital mode
	srv.request.pin = 1;//io_1

	if(iscatch)
		srv.request.state =1;//high_level
	else
		srv.request.state =0;

	if (client.call(srv))
	{
	   ros::Duration(sleep_time).sleep(); 
	   ROS_INFO("Success: %d", (bool)srv.response.success);
		
	}
	else
	{
	    ROS_ERROR("Failed to call service");	    
	}
}

/************************Sucker********************************/
void Main_Sucker(ros::ServiceClient &client,bool iscatch, int sleep_time)//干路
{
	ur_msgs::SetIO srv;
	srv.request.fun= 1;//digital mode
	srv.request.pin = 2;//io_2

	if(iscatch)
		srv.request.state =1;//high_level
	else
		srv.request.state =0;

	if (client.call(srv))
	{
	   ros::Duration(sleep_time).sleep(); 
	   ROS_INFO("Success: %d", (bool)srv.response.success);
		
	}
	else
	{
	    ROS_ERROR("Failed to call service");	    
	}
}

void Left_Sucker(ros::ServiceClient &client,bool iscatch, int sleep_time)
{
	ur_msgs::SetIO srv;
	srv.request.fun= 1;//digital mode
	srv.request.pin = 3;//io_3

	if(iscatch)
		srv.request.state =1;//high_level
	else
		srv.request.state =0;
	Main_Sucker(client,iscatch,sleep_time);

	if (client.call(srv))
	{
	   ros::Duration(sleep_time).sleep(); 
	   ROS_INFO("Success: %d", (bool)srv.response.success);
	}
	else
	{
	    ROS_ERROR("Failed to call service");	    
	}
}

void Right_Sucker(ros::ServiceClient &client,bool iscatch, int sleep_time)
{
	ur_msgs::SetIO srv;
	srv.request.fun= 1;//digital mode
	srv.request.pin = 4;//io_4
	
	if(iscatch)
		srv.request.state =1;//high_level
	else
		srv.request.state =0;//low_level
	Main_Sucker(client,iscatch,sleep_time);//干路

	if (client.call(srv))
	{
	    ros::Duration(sleep_time).sleep();
	    ROS_INFO("Success: %d", (bool)srv.response.success);
		
	}
	else
	{
	    ROS_ERROR("Failed to call service");
	}
}
