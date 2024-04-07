#include <p_robot_learning_demo/UrDemoAction.h>
#include <actionlib/client/simple_action_client.h>
#include <iostream>
using namespace std;
typedef actionlib::SimpleActionClient<p_robot_learning_demo::UrDemoAction> Client;

using namespace std;

static int a_id;
static int m_id;
static double posi[4];

class UrDemoClient
{
private:
    //Called once when the goal completes
    void DoneCb(const actionlib::SimpleClientGoalState& state,
		const p_robot_learning_demo::UrDemoResultConstPtr& result)
    {
		ROS_INFO("Finished in state");
		ROS_INFO("The eef position is %f ", result->rurpos[0]);

		//ros::shutdown();
    }

    // 当目标激活的时候，会调用一次
    void ActiveCb()
    {
		ROS_INFO("Goal just went active");
    }

    //接收服务器的反馈消息
    void FeedbackCb(const p_robot_learning_demo::UrDemoFeedbackConstPtr& feedback)
    {
		ROS_INFO("Got Feedback Complete Rate is %f ", feedback->percent_complete);
    }

public:
    UrDemoClient(const std::string client_name, bool flag = true) :
		client(client_name, flag)
    {
    }

    //客户端开始
    void Start()
    {
		//等待服务器初始化完成
		client.waitForServer();
		p_robot_learning_demo::UrDemoGoal goal;
		goal.mode_id = m_id;
		goal.urpos.clear();
		if (m_id == 1)
		{
			goal.action_id = a_id;
			goal.urpos.push_back(posi[0]);
			goal.urpos.push_back(posi[1]);
			goal.urpos.push_back(posi[2]);
			goal.urpos.push_back(0.5);  //w
			goal.urpos.push_back(-0.5);  //x
			goal.urpos.push_back(0.5);  //y
			goal.urpos.push_back(0.5);  //z
	
			goal.gripper_val.push_back(0.266);
		}
		else if (m_id == 2)
		{
			goal.urpos.push_back(-0.197115);
			goal.urpos.push_back(0.035917);
			goal.urpos.push_back(-1.367742);
			goal.urpos.push_back(-0.045058);  //w
			goal.urpos.push_back(2.335935);  //x
			goal.urpos.push_back(-2.865158);  //y
		}
		//发送目标至服务器
		client.sendGoal(goal,
			boost::bind(&UrDemoClient::DoneCb, this, _1, _2),
			boost::bind(&UrDemoClient::ActiveCb, this),
			boost::bind(&UrDemoClient::FeedbackCb, this, _1));
		//等待结果，时间间隔5秒
		client.waitForResult(ros::Duration(10.0));

		//根据返回结果，做相应处理
		if (client.getState() == actionlib::SimpleClientGoalState::SUCCEEDED) 
		{
			ROS_INFO("Done"); 
	    }
		else 
		{
			ROS_INFO("Cancel Goal!");
			client.cancelAllGoals();
		}

		ROS_INFO("Current State: %s ", client.getState().toString().c_str());
    }
private:
    Client client;
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "ur_demo_client");
    ROS_INFO("Input mode_id 1 or 2 ?");
    std::cin>>m_id;
    if (m_id == 1)
    {
		ROS_INFO("Input action_id 1(arm_init) or 2(move) or 3(pick_obj) 4(place_obj) ?");
		std::cin>>a_id;
		if (a_id != 1)
		{
			ROS_INFO("Input position values X Y Z and robotiq joint value :");
			std::cin>>posi[0]>>posi[1]>>posi[2];
		}
		else
		{
			posi[0] = 1;
			posi[1] = 0.7;
			posi[2] = 1.1;
		}
    }
	string node_name;
	node_name = "ur_demo";

    UrDemoClient actionclient(node_name, true);
    //启动客户端
    actionclient.Start();
    //ros::spin();
    ros::shutdown;
    return 0;
}

