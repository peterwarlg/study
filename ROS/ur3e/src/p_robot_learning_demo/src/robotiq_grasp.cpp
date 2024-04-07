#include "ros/ros.h"

#include <moveit/move_group_interface/move_group_interface.h>

#include <std_msgs/Float64.h>

static double g_val;

void callback(const std_msgs::Float64 &gripper_val)
{
	//g_val = static_cast<double>(gripper_val.data);
	
	moveit::planning_interface::MoveGroupInterface group2("robotiq");
	
	std::vector<double> rbq_joint_values;
	group2.getCurrentState()->copyJointGroupPositions(group2.getCurrentState()->getRobotModel()->getJointModelGroup(group2.getName()),rbq_joint_values);

	rbq_joint_values[0] = 0;
	rbq_joint_values[1] = 0;
	rbq_joint_values[2] = gripper_val.data;
	rbq_joint_values[3] = 0;
	rbq_joint_values[4] = 0;
	rbq_joint_values[5] = 0;

	group2.setJointValueTarget(rbq_joint_values);
	moveit::planning_interface::MoveGroupInterface::Plan my_plan;
	//bool success = group2.plan(my_plan);
	//bool success = static_cast<bool>(group2.plan(my_plan));
	bool success = (group2.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
	bool succ = false;
	if (success)
	{
		succ = (group2.execute(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
		int count = 0;
		while(int(succ)==0 && (count < 5))
		{
			group2.plan(my_plan);
			succ = (group2.execute(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
			count++;
		}
	}
	// if (success)
	// {
	// 	succ = group2.execute(my_plan);
	// 	int count = 0;
	// 	while (succ == 0 && count < 5)
	// 	{
	// 		group2.plan(my_plan);
	// 		succ = group2.execute(my_plan);
	// 		count++;
	// 	}
	// }
	//group2.execute(my_plan);
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "group2grasp");
	ros::NodeHandle n;
	
	ros::AsyncSpinner spinner(2);
	spinner.start();
	
	ros::Subscriber gripper_grasp_sub = n.subscribe("gripper_go", 1000, callback);
	
	ros::Rate loop_rate(10);
	
	while(ros::ok())
	{
		ros::spinOnce();
	}
}
