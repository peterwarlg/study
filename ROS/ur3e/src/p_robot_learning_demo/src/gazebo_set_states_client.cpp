#include <ros/ros.h>
//#include <gazebo/gazebo.hh>
#include <gazebo_msgs/SetModelState.h>
#include <stdlib.h> 
#include <time.h>
#include <math.h>

#define x_min (40-5.8) // 0.4*100
#define x_max (85-5.8) // 0.8*100
#define y_min 35 // 0.35*100
#define y_max 58 // 0.58*100

// produce a random num in a range  min+rand()%(max-min+1)
double random(double start, double end);

int main(int argc, char **argv)
{
	ros::init(argc, argv, "gazebo_set_states_client");
	
	int choice_id;
	double pos[9];
	srand((int)time(0));

	ros::NodeHandle n;
	ros::ServiceClient client = n.serviceClient<gazebo_msgs::SetModelState>("/gazebo/set_model_state");

	ROS_INFO("Chose a mode:1.human mode 2.rondom mode.");
	std::cin>>choice_id;
	gazebo_msgs::SetModelState objstate;
	if (choice_id == 1)
	{
		//set red_cube position
		ROS_INFO("Input three cube's position : x1 y1 z1 x2 y2 z2 x3 y3 z3");
		std::cin>>pos[0]>>pos[1]>>pos[2]>>pos[3]>>pos[4]>>pos[5]>>pos[6]>>pos[7]>>pos[8];
		objstate.request.model_state.model_name = "red_cube";
		objstate.request.model_state.pose.position.x = pos[0];
		objstate.request.model_state.pose.position.y = pos[1];
		objstate.request.model_state.pose.position.z = pos[2];
		objstate.request.model_state.pose.orientation.w = 1;
		objstate.request.model_state.pose.orientation.x = 0;
		objstate.request.model_state.pose.orientation.y = 0;
		objstate.request.model_state.pose.orientation.z = 0;
		objstate.request.model_state.twist.linear.x = 0.0;
		objstate.request.model_state.twist.linear.y = 0.0;
		objstate.request.model_state.twist.linear.z = 0.0;
		objstate.request.model_state.twist.angular.x = 0.0;
		objstate.request.model_state.twist.angular.y = 0.0;
		objstate.request.model_state.twist.angular.z = 0.0;
		objstate.request.model_state.reference_frame = "world";
	
		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		//set yellow_cube position
		objstate.request.model_state.model_name = "yellow_cube";
		objstate.request.model_state.pose.position.x = pos[3];
		objstate.request.model_state.pose.position.y = pos[4];
		objstate.request.model_state.pose.position.z = pos[5];

		if (client.call(objstate))
		{
		    ROS_INFO("MOdels state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		//set blue_cube position
		objstate.request.model_state.model_name = "blue_cube";
		objstate.request.model_state.pose.position.x = pos[6];
		objstate.request.model_state.pose.position.y = pos[7];
		objstate.request.model_state.pose.position.z = pos[8];

		if (client.call(objstate))
		{
		    ROS_INFO("MOdels state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}
	} // if (choice_id == 1)
	else if (choice_id == 2)
	{
		double dist;
                // set red cube pos
	        pos[0] = random(x_min, x_max)/100;
	        pos[1] = random(y_min, y_max)/100;
	        pos[2] = 0.83;
		ROS_INFO("red cube x= %lf y= %lf",pos[0],pos[1]);
		objstate.request.model_state.model_name = "red_cube";
		objstate.request.model_state.pose.position.x = pos[0];
		objstate.request.model_state.pose.position.y = pos[1];
		objstate.request.model_state.pose.position.z = pos[2];
		objstate.request.model_state.pose.orientation.w = 1;
		objstate.request.model_state.pose.orientation.x = 0;
		objstate.request.model_state.pose.orientation.y = 0;
		objstate.request.model_state.pose.orientation.z = 0;
		objstate.request.model_state.twist.linear.x = 0.0;
		objstate.request.model_state.twist.linear.y = 0.0;
		objstate.request.model_state.twist.linear.z = 0.0;
		objstate.request.model_state.twist.angular.x = 0.0;
		objstate.request.model_state.twist.angular.y = 0.0;
		objstate.request.model_state.twist.angular.z = 0.0;
		objstate.request.model_state.reference_frame = "world";

		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		// set yellow cube pos
		pos[3] = random(x_min, x_max)/100;
		pos[4] = random(y_min, y_max)/100;
		pos[5] = 0.83;
		
		dist = sqrt((pos[0] - pos[3]) * (pos[0] - pos[3]) + (pos[1] - pos[4]) * (pos[1] - pos[4]));
		if (dist < 0.85)
			pos[4] = pos[1] + 0.07;
		ROS_INFO("yellow cube x= %lf y= %lf",pos[3],pos[4]);
		objstate.request.model_state.model_name = "yellow_cube";
		objstate.request.model_state.pose.position.x = pos[3];
		objstate.request.model_state.pose.position.y = pos[4];
		objstate.request.model_state.pose.position.z = pos[5];

		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		// set blue cube pos
		pos[6] = random(x_min, x_max)/100;
		pos[7] = random(y_min, y_max)/100;
		pos[8] = 0.83;
		
		dist = sqrt((pos[6] - pos[3]) * (pos[6] - pos[3]) + (pos[7] - pos[4]) * (pos[7] - pos[4]));
		if (dist < 0.85 && pos[4] < 0.58)
			pos[7] = pos[4] + 0.07;
		else
			pos[7] = pos[1] - 0.07;
		ROS_INFO("blue cube x= %lf y= %lf",pos[6],pos[7]);
		objstate.request.model_state.model_name = "blue_cube";
		objstate.request.model_state.pose.position.x = pos[6];
		objstate.request.model_state.pose.position.y = pos[7];
		objstate.request.model_state.pose.position.z = pos[8];

		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		objstate.request.model_state.model_name = "black_cube";
		objstate.request.model_state.pose.position.x = 0.1;
		objstate.request.model_state.pose.position.y = 0.5;
		objstate.request.model_state.pose.position.z = 0.83;
		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}

		objstate.request.model_state.model_name = "aruco_cube";
		objstate.request.model_state.pose.position.x = 0.1;
		objstate.request.model_state.pose.position.y = 0.4;
		objstate.request.model_state.pose.position.z = 0.83;
		if (client.call(objstate))
		{
		    ROS_INFO("Models state setting is OK!");
		}
		else
		{
		    ROS_ERROR("failed to set models state!");
		    return 1;
		}
	}
	

	return 0;
}

double random(double start, double end)
{
	return start + (end - start) * rand()/(RAND_MAX + 1.0);
}
