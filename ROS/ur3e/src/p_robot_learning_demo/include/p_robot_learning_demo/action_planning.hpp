#include <ros/ros.h>

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>

#include <std_msgs/Float64.h>

#include <tf/tf.h>

#include <p_robot_learning_demo/path_planning.hpp>

#include <io.hpp>
#include <ur_msgs/SetIO.h>

#include <iostream>

static double speed = 2;

namespace arm_planning
{
    class action_planning
    {
    protected:
        ros::NodeHandle nh_; // https://stackoverflow.com/questions/45309584/error-using-boostbind-for-subscribe-callback
        
    public:
        action_planning(ros::NodeHandle &nh);
        
        moveit::planning_interface::MoveGroupInterface ur5_;
        moveit::planning_interface::MoveGroupInterface robotiq_;
        
        bool success;
        tf::Quaternion q;
        double gripper_val;
        
        arm_planning::path_planning robot_planning;
        
        ros::ServiceClient client;
        ros::Publisher gripper_grasp_pub;
        
        bool arm_init(Object *ur5_target_p);
        
        bool move(Object *ur5_target_p);
        bool move(Object *ur5_target_p, const moveit_msgs::Constraints &path_constraints);
        
        bool move2(Object *ur5_target_p);
        
        bool pick_obj(Object *obj);
        
        bool pick_obj2(Object *obj);
        
        bool place_obj(Object *target_p);
        
        bool place_obj2(Object *target_p);
        
        bool gripper_grasp(double joint_val);
        
        bool gripper_grasp2(int grasp);
        
        bool arm_push(Object *push_p);
        
        bool action_execute(moveit::planning_interface::MoveGroupInterface::Plan &plan);
     
    }; // class action_planning
} // namespace

using namespace arm_planning;
using namespace std;

action_planning::action_planning(ros::NodeHandle &nh) :
    ur5_("ur_arm"),
    robotiq_("robotiq"),
    nh_(nh)
    {
		ur5_.setPlannerId("RRTConnectkConfigDefault");
		ur5_.setPlanningTime(5);
		ur5_.setNumPlanningAttempts(25);
    
    	client = nh_.serviceClient<ur_msgs::SetIO>("/ur_driver/set_io");
    	gripper_grasp_pub = nh_.advertise<std_msgs::Float64>("gripper_go", 1000); // 发布手抓运动话题
    } // action_planning  
    
bool action_planning::arm_init(Object *ur5_target_p)  // action_id = 0
{
	cout << "Action: Init." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    
    //避免ur5第6个关节极限
    moveit_msgs::JointConstraint jcm5;
    moveit_msgs::Constraints ur5_constraints;
    jcm5.joint_name="wrist_3_joint";
    jcm5.position = 0.0;
    jcm5.tolerance_above = 3.0;  //运动限制
    jcm5.tolerance_below = 3.0;
    jcm5.weight = 1.0;
    ur5_constraints.joint_constraints.push_back(jcm5);
    
    Object ur5_p;
	ur5_p.pose.position.x = ur5_target_p->pose.position.x;
	ur5_p.pose.position.y = ur5_target_p->pose.position.y;
	ur5_p.pose.position.z = ur5_target_p->pose.position.z; 
	tf::Quaternion q;
	q.setRPY(0, PI / 2, PI / 2); // x: 90 y: 90
	ur5_p.pose.orientation.w = q[3];  // 0.5 0.5 0.5 -0.5
	ur5_p.pose.orientation.x = q[0];
	ur5_p.pose.orientation.y = q[1];
	ur5_p.pose.orientation.z = q[2];
	
	ur5_p.pose_rpy.r = 0;
	ur5_p.pose_rpy.p = PI / 2;
	ur5_p.pose_rpy.y = PI / 2;
	
    move(&ur5_p, ur5_constraints);
    
    return true;    
} // arm_init
    
bool action_planning::move(Object *ur5_target_p) // action_id = 1
{
	cout << "Action: Move." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    arm_planning::path_planning robot_planning;
    bool try_step = true;
    
    while (try_step && ros::ok())
    {
        plan = robot_planning.CartesianPath(ur5_, ur5_target_p);
        robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
        success = action_execute(plan);
        try_step = false;
    } // while
    
    return success;
}
  
bool action_planning::move(Object *ur5_target_p, const moveit_msgs::Constraints &path_constraints) // action_id = 1
{
	cout << "Action: Move." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    arm_planning::path_planning robot_planning;
    bool try_step = true;
    
    while (try_step && ros::ok())
    {
        plan = robot_planning.CartesianPath(ur5_, ur5_target_p,path_constraints);
        robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
        success = action_execute(plan);
        try_step = false;
    } // while
	
    return success;
}
bool action_planning::move2(Object *ur5_target_p) // action_id = 1
{
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    geometry_msgs::Pose target_pose;
    bool try_step = true;
    
    while (try_step && ros::ok())
    {
        target_pose = ur5_target_p->pose;
        ur5_.setPoseTarget(target_pose, "ur5_gripper");
        ur5_.plan(plan);
        success = action_execute(plan);
        ROS_INFO("Visualizing plan 1 (pose goal) %s",success?"SUCCEED":"FAILED");
        try_step = false;
    } // while
    
    return success;
} // move2
    
bool action_planning::pick_obj(Object *obj) // action_id = 2  simu robot pick
{
	cout << "Action: Pick object." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
  
    double lift_hight = 0.1;
    Object obj_target_pose[3];
    Object *p1[2];
    
    obj_target_pose[1] = *obj;
    
    obj_target_pose[0] = obj_target_pose[1];
    obj_target_pose[0].pose.position.z += lift_hight;
    
    obj_target_pose[2] = obj_target_pose[0];
    
    for (int i = 0; i < 2; i++)
    {
        p1[i] = &obj_target_pose[i];
    }
    
    plan = robot_planning.CartesianPath_arc(ur5_, p1, 2);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    success = action_execute(plan);
    /*sleep(3);
    //cout << "joint_val= " << joint_val << endl;
    //gripper_grasp(joint_val);
    gripper_grasp_pub.publish(1);
    sleep(3);

    plan = robot_planning.CartesianPath(ur5_, &obj_target_pose[2]);
    success = action_execute(plan);*/
    return success;
} // pick_obj

bool action_planning::pick_obj2(Object *obj) // action_id = 2  real robot pick
{
	cout << "Action: Pick object." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    
    double lift_hight = 0.1;
    Object obj_target_pose[3];
    Object *p1[2];
    
    obj_target_pose[1] = *obj;
    
    obj_target_pose[0] = obj_target_pose[1];
    obj_target_pose[0].pose.position.z += lift_hight;
    
    obj_target_pose[2] = obj_target_pose[0];
    
    for (int i = 0; i < 2; i++)
    {
        p1[i] = &obj_target_pose[i];
    }
    
    plan = robot_planning.CartesianPath_arc(ur5_, p1, 2);   
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    action_execute(plan);
    
    Right_Gripper(client, true, 1);
    
    plan = robot_planning.CartesianPath(ur5_, &obj_target_pose[2]);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    success = action_execute(plan);
    return true;
} // pick_obj2
    
bool action_planning::place_obj(Object *target_p) // action_id = 3
{
	cout << "Action: Place object." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
  
    double lift_hight = 0.1;
    Object obj_target_pose[3];
    Object *p1[2];
    
    obj_target_pose[1] = *target_p;
    obj_target_pose[1].pose.position.z += 0.005;
    
    obj_target_pose[0] = obj_target_pose[1];
    obj_target_pose[0].pose.position.z += lift_hight;
    
    obj_target_pose[2] = obj_target_pose[0];
    
    for (int i = 0; i < 2; i++)
    {
        p1[i] = &obj_target_pose[i];
    }
    
    plan = robot_planning.CartesianPath_arc(ur5_, p1, 2);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    success = action_execute(plan);
    
    //gripper_grasp(0);
    /*gripper_grasp_pub.publish(0.0);
    sleep(3);

    plan = robot_planning.CartesianPath(ur5_, &obj_target_pose[2]);
    success = action_execute(plan);*/
    return success;
} // place_obj

bool action_planning::place_obj2(Object *target_p) // action_id = 2
{
	cout << "Action: Place object." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
  
    double lift_hight = 0.1;
    Object obj_target_pose[3];
    Object *p1[2];
    
    obj_target_pose[1] = *target_p;
    obj_target_pose[1].pose.position.z += 0.005;
    
    obj_target_pose[0] = obj_target_pose[1];
    obj_target_pose[0].pose.position.z += lift_hight;
    
    obj_target_pose[2] = obj_target_pose[0];
    
    for (int i = 0; i < 2; i++)
    {
        p1[i] = &obj_target_pose[i];
    }
    
    plan = robot_planning.CartesianPath_arc(ur5_, p1, 2);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    action_execute(plan);
    
    Right_Gripper(client, false, 1);

    plan = robot_planning.CartesianPath(ur5_, &obj_target_pose[2]);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    success = action_execute(plan);
    return true;
} // pick_obj2

bool action_planning::gripper_grasp(double joint_val)
{
	std::vector<double> rbq_joint_values;
	robotiq_.getCurrentState()->copyJointGroupPositions(robotiq_.getCurrentState()->getRobotModel()->getJointModelGroup(robotiq_.getName()),rbq_joint_values);

	rbq_joint_values[0] = 0;
	rbq_joint_values[1] = 0;
	rbq_joint_values[2] = joint_val;
	rbq_joint_values[3] = 0;
	rbq_joint_values[4] = 0;
	rbq_joint_values[5] = 0;

	robotiq_.setJointValueTarget(rbq_joint_values);
	moveit::planning_interface::MoveGroupInterface::Plan my_plan;
	//success = robotiq_.plan(my_plan);
    bool success = (robotiq_.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
	robotiq_.execute(my_plan);
	
	sleep(1);
} // gripper_grasp

bool action_planning::gripper_grasp2(int grasp)
{
	if (grasp == 1)
	{
		Right_Gripper(client, true, 1);
	}
	else
	{
		Right_Gripper(client, false, 1);
	}
} // gripper_grasp2
    
bool action_planning::arm_push(Object *push_p) // action_id = 4
{   
	cout << "Action: Arm push." << endl;
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    
    double x = 0.5, y = 0;
    
    double lift_hight = 0.1;
    Object obj_target_pose[4];
    Object *p1[3];
    
    obj_target_pose[1] = *push_p;
    obj_target_pose[1].pose.position.z -= 0.005;
    
    obj_target_pose[0] = obj_target_pose[1];
    obj_target_pose[0].pose.position.z += lift_hight;
    
    obj_target_pose[2] = obj_target_pose[1];
    //obj_target_pose[2].pose.position.x = push_p->pose.position.x + 0.1 * (x - push_p->pose.position.x);
    if (ur5_.getName().compare("ur5_manipulator") == 0)
    {
        obj_target_pose[2].pose.position.y = push_p->pose.position.y + 0.2;
    }
        
    obj_target_pose[3] = obj_target_pose[2];
    obj_target_pose[3].pose.position.z = obj_target_pose[0].pose.position.z + 0.1;
    
    for (int i = 0; i < 3; i++)
    {
        p1[i] = &obj_target_pose[i];
    }
    
    plan = robot_planning.CartesianPath_arc(ur5_, p1, 3);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    action_execute(plan);
    
    // up
    plan = robot_planning.CartesianPath(ur5_, &obj_target_pose[3]);
    robot_planning.scaleTrajectorySpeed(plan.trajectory_, speed);
    action_execute(plan);
} // arm_push

bool action_planning::action_execute(moveit::planning_interface::MoveGroupInterface::Plan &plan)
{
	//success = ur5_.execute(plan);
    bool success = (ur5_.execute(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
	int count = 0;
	while (success == 0 && count < 5)
	{
		//success = ur5_.execute(plan); //2020
        success = (ur5_.execute(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
		
        count++;
	}
	
	if (success == 0)
	{
		ROS_WARN("Action execute failed!");
		return false;
	}
	else
	{
		ROS_INFO("Action execute succeed!");
		return true;
	}
}


