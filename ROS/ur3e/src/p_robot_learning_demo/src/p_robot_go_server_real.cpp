#include <ros/ros.h>

//包含actionlib的头文件
#include <actionlib/server/simple_action_server.h>
#include <p_robot_learning_demo/UrDemoAction.h>

#include <p_robot_learning_demo/action_planning.hpp>

//包含moveit的API头文件
#include <moveit/move_group_interface/move_group_interface.h>

#include <vector>

typedef actionlib::SimpleActionServer<p_robot_learning_demo::UrDemoAction> Server;

using namespace arm_planning;
using namespace std;

class UrDemoServer
{
protected:
	ros::NodeHandle n_;
public:
    UrDemoServer(ros::NodeHandle &n):
    n_(n),
	server(n, "ur_demo", boost::bind(&UrDemoServer::ExecuteCb, this, _1), false)
    {
	//注册抢占回调函数
	server.registerPreemptCallback(boost::bind(&UrDemoServer::preemptCb, this));
    }

    //Start server
    void Start()
    {
		server.start();
    }

    //回调函数，在此添加代码实现你要的功能
    void ExecuteCb(const p_robot_learning_demo::UrDemoGoalConstPtr& goal)
    {
		// 在此添加你所要实现的功能
		int mode_id = goal->mode_id;
		int action_id = goal->action_id;
	
		//p_robot_learning_demo::UrDemoFeedback feedback;
		//feedback.percent_complete = 1/10.0;
		//server.publishFeedback(feedback);

		ros::AsyncSpinner spinner(4);
		spinner.start();	

		//规划UR机械臂
		moveit::planning_interface::MoveGroupInterface group("ur_arm");
	
		action_planning acpl(n_);

		//打印该组的参考系的名称
		//ROS_INFO("Reference frame: %s", group.getPlanningFrame().c_str());  // world

		//打印该组的末端执行器的名称
		//ROS_INFO("End effector links: %s", group.getEndEffectorLink().c_str());

		ROS_INFO("mode_id: %d", mode_id);
		ROS_INFO("Received goal, the action id is: %d", action_id);
		double suc = 0;
		//group.setPlannerId("RRTConnectkConfigDefault");
		if (mode_id != 0)
		{
			if (mode_id == 1)
			{
				Object obj;
				double gripper_val;
				obj.pose.position.x = goal->urpos[0];
				obj.pose.position.y = goal->urpos[1];
				obj.pose.position.z = goal->urpos[2];
			
				obj.pose.orientation.w = goal->urpos[3];
				obj.pose.orientation.x = goal->urpos[4];
				obj.pose.orientation.y = goal->urpos[5];
				obj.pose.orientation.z = goal->urpos[6];
				
				obj.pose_rpy.r = 0;
				obj.pose_rpy.p = PI / 2;
				obj.pose_rpy.y = PI / 4;  //PI / 4 or PI / 2
			
				//gripper_val = goal->gripper_val[0];
			
				switch (action_id)
				{
					case 1: suc = acpl.arm_init(&obj);
						break;
					case 2: suc = acpl.move(&obj);
						break;
					case 3: suc = acpl.pick_obj2(&obj);
						break;
					case 4: suc = acpl.place_obj2(&obj);
						break;
					case 5: suc = acpl.gripper_grasp2(1);
						break;
					case 6: suc = acpl.gripper_grasp2(0);
						break;
					default: break;
				} // switch
			} // if mode_id == 1
			//规划到一个关节空间内的目标
			else if (mode_id == 2)
			{
				std::vector<double> joint_values;
				group.getCurrentState()->copyJointGroupPositions(group.getCurrentState()->getRobotModel()->getJointModelGroup(group.getName()),joint_values);
			
				ROS_INFO("joint1= %lf .",joint_values[0]);
				ROS_INFO("joint2= %lf .",joint_values[1]);
				ROS_INFO("joint3= %lf .",joint_values[2]);
				ROS_INFO("joint4= %lf .",joint_values[3]);
				ROS_INFO("joint5= %lf .",joint_values[4]);
				ROS_INFO("joint6= %lf .",joint_values[5]);
			
				for (int i = 0; i < 6; i++)
				{
					if (goal->urpos[i] != 10)
					{
						joint_values[i] = goal->urpos[i];
					} // if
				} // for

				group.setJointValueTarget(joint_values);
				moveit::planning_interface::MoveGroupInterface::Plan my_plan;
				//bool success = group.plan(my_plan);
				bool success = (group.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
			
				ROS_INFO("Visualizing plan 2 (joint space goal) %s",success?"":"FAILED");

				//让机械臂按照规划的轨迹开始运动。
		  			if(success)
		       			group.execute(my_plan);
			} // else if		

		} // if mode_id != 0

		//打印当前末端执行器位姿
	    geometry_msgs::PoseStamped current_pose;
	    current_pose = group.getCurrentPose();
	    
	    ROS_INFO("x= %lf .",current_pose.pose.position.x);
		ROS_INFO("y= %lf .",current_pose.pose.position.y);
		ROS_INFO("z= %lf .",current_pose.pose.position.z);

		p_robot_learning_demo::UrDemoResult result;
		result.rurpos.push_back(current_pose.pose.position.x);
		result.rurpos.push_back(current_pose.pose.position.y);
		result.rurpos.push_back(current_pose.pose.position.z);	
		result.rurpos.push_back(current_pose.pose.orientation.w);
		result.rurpos.push_back(current_pose.pose.orientation.x);
		result.rurpos.push_back(current_pose.pose.orientation.y);
		result.rurpos.push_back(current_pose.pose.orientation.z);
		result.rurpos.push_back(suc);
	
		if(server.isActive())
			server.setSucceeded(result);
	} // void ExecuteCb

	//中断回调函数
	void preemptCb()
	{
		if(server.isActive())
		{
			server.setPreempted();  //强制中断
		}
    }

    Server server;
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "ur_demo_server");
    ros::NodeHandle n;

    //Define a server
    UrDemoServer actionserver(n);
    //启动服务器，等待客户端信息到来
    actionserver.Start();
    
    ros::spin();
    return 0;
}
