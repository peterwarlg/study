#include <ros/ros.h>

//包含actionlib的头文件
#include <actionlib/server/simple_action_server.h>
#include <p_robot_learning_demo/UrDemoAction.h>

//包含moveit的API头文件
#include <moveit/move_group_interface/move_group_interface.h>

#include <vector>

typedef actionlib::SimpleActionServer<p_robot_learning_demo::UrDemoAction> Server;

class RbqDemoServer
{
public:
    RbqDemoServer(ros::NodeHandle n):
	server(n, "robotiq_demo", boost::bind(&RbqDemoServer::ExecuteCb, this, _1), false)
    {
	//注册抢占回调函数
	server.registerPreemptCallback(boost::bind(&RbqDemoServer::preemptCb, this));
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
	ROS_INFO("Received goal, the task id is: %d", goal->mode_id);
	int id = goal->mode_id;
	
	//my_robot::UrDemoFeedback feedback;
	//feedback.percent_complete = 1/10.0;
	//server.publishFeedback(feedback);

	//ros::AsyncSpinner spinner(1);
	//spinner.start();	           //20200218

	//规划robotiq手抓
    moveit::planning_interface::MoveGroupInterface group2("robotiq");
	p_robot_learning_demo::UrDemoResult result;
	std::vector<double> rbq_joint_values;
        //id=0：获取状态， id=1：规划
	if (id != 0)
	{
		group2.getCurrentState()->copyJointGroupPositions(group2.getCurrentState()->getRobotModel()->getJointModelGroup(group2.getName()),rbq_joint_values);

		rbq_joint_values[0] = 0;
		rbq_joint_values[1] = 0;
		rbq_joint_values[2] = goal->urpos[0];
		rbq_joint_values[3] = 0;
		rbq_joint_values[4] = 0;
		rbq_joint_values[5] = 0;

		group2.setJointValueTarget(rbq_joint_values);
		moveit::planning_interface::MoveGroupInterface::Plan my_plan;
		//bool success = group2.plan(my_plan);
		bool success = (group2.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
		bool succ = false;
		
		//让机械臂按照规划的轨迹开始运动。
		// if(success)
		// {
   		// 	succ = group2.execute(my_plan);
		// 	int count = 0;
		// 	while ((succ == 0) && (count < 5)) //如果失败，最多再重新尝试5次
		// 	{
		// 		group2.plan(my_plan);
		// 		succ = group2.execute(my_plan);
		// 		count++;
		// 	}
		// }
		if(success)
		{
			succ = (group2.execute(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
			int count = 0;
			while( (int(succ) == 0) && (count < 5 ))
			{
				group2.plan(my_plan);
				succ = (group2.execute(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
				count++;
			}
		}
	}
	
	//获取robotiq状态信息
	group2.getCurrentState()->copyJointGroupPositions(group2.getCurrentState()->getRobotModel()->getJointModelGroup(group2.getName()),rbq_joint_values);
	double rbqjv;
	rbqjv = rbq_joint_values[2];
	result.rurpos.push_back(rbqjv);

	if(server.isActive())
	    server.setSucceeded(result);
    }

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
    ros::init(argc, argv, "robotiq_demo_server");
    ros::NodeHandle n;

    //Define a server
    RbqDemoServer actionserver(n);
    //启动服务器，等待客户端信息到来
    actionserver.Start();
    
    ros::spin();
    return 0;
}






