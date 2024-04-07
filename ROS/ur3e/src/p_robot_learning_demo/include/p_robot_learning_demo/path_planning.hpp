#include <ros/ros.h>

#include <actionlib/server/simple_action_server.h>

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit/trajectory_processing/iterative_time_parameterization.h>
#include <moveit/robot_state/conversions.h>

#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <moveit_msgs/GetStateValidity.h>
#include <moveit_msgs/GetPositionIK.h>
#include <moveit_msgs/GetPositionFK.h>

#include <geometry_msgs/PointStamped.h>
#include <geometry_msgs/Pose.h>

// tf
#include <tf/tf.h>

//KDL
#include <kdl/frames.hpp>
#include <kdl/frames_io.hpp>
#include <kdl/trajectory.hpp>
#include <kdl/trajectory_segment.hpp>
#include <kdl/trajectory_stationary.hpp>
#include <kdl/trajectory_composite.hpp>
#include <kdl/velocityprofile_spline.hpp>
#include <kdl/velocityprofile_trap.hpp>
#include <kdl/path_line.hpp>
#include <kdl/path_roundedcomposite.hpp>
#include <kdl/rotational_interpolation_sa.hpp>

// Controller Manager
#include <controller_manager_msgs/SwitchController.h>
#include <controller_manager_msgs/SwitchControllerRequest.h>
#include <controller_manager_msgs/SwitchControllerResponse.h>
// Controller Interface
#include <moveit_simple_controller_manager/follow_joint_trajectory_controller_handle.h>

#include <math.h>
#include <vector>
#include <string>
#include <iostream>
#include <stdbool.h>

#include <Transform.hpp>

#define PI 3.14159265

using namespace std;
using namespace KDL;

//typedef struct Object
struct Object
{
    int state;  //1：  0： -1：
	double obj_id;  //0:  1:  2:  3:
	geometry_msgs::Pose pose;
	
	struct Pose_rpy
	{
		double r, p, y;
	} pose_rpy;
	
	/*struct Grasp_point
	{
		double x, y, z, w, wx, wy, wz, r, p, y1;
	} g_point;*/
};

/**
* @PointsArray  the struct of objects' info
* pose array
* len  num of objects
*/
//typedef struct ObjectsArray
struct ObjectsArray
{
	int len;
	Object object[9];
} Objects;

double dist_compute(Object *a, Object *b);

/**
* @arm_planning 
* 
*/
namespace arm_planning
{
	/**
	* @path_planning assembly path planning
	* ÀàµÄÏêÏžžÅÊö
	*/
	class path_planning  //arm_planning::path_planning path
	{
	public:
		path_planning();  //constructor
		~path_planning();

		Object obj;
		
		void computeTimeFromStart(moveit_msgs::RobotTrajectory& trajectory, double step_t);
		bool computeVelocities(moveit_msgs::RobotTrajectory& trajectory, moveit::planning_interface::MoveGroupInterface& moveGroup);
		
		void scaleTrajectorySpeed(moveit_msgs::RobotTrajectory& trajectory, double scale);
		
		moveit::planning_interface::MoveGroupInterface::Plan CartesianPath(moveit::planning_interface::MoveGroupInterface &group, Object *targete_p); //单点到单点直线
		moveit::planning_interface::MoveGroupInterface::Plan CartesianPath(moveit::planning_interface::MoveGroupInterface &group, Object *targete_p, const moveit_msgs::Constraints &path_constraints); //单点到单点直线
		moveit::planning_interface::MoveGroupInterface::Plan CartesianPath_arc(moveit::planning_interface::MoveGroupInterface &group,Object *target_p[],int len);//多目标点路径规划
		moveit::planning_interface::MoveGroupInterface::Plan CartesianPath_arc(moveit::planning_interface::MoveGroupInterface &group, Object *target_p[], int len,const moveit_msgs::Constraints &path_constraints);

		//point to point path planning
		moveit::planning_interface::MoveGroupInterface::Plan setpose_planning(moveit::planning_interface::MoveGroupInterface &group, Object *end_p);

		//
		void spiral_search_planning(int p_num, double a, double *x, double *y);
		
	}; // class path_planning
} // ns

arm_planning::path_planning::path_planning()
{

}
arm_planning::path_planning::~path_planning()
{

}

void arm_planning::path_planning::computeTimeFromStart(moveit_msgs::RobotTrajectory& trajectory, double step_t)
{
    for (unsigned int i=0; i < trajectory.joint_trajectory.points.size(); i++)
    {
        trajectory.joint_trajectory.points[i].time_from_start.fromSec(i*step_t);
    }
}

bool arm_planning::path_planning::computeVelocities(moveit_msgs::RobotTrajectory& trajectory, moveit::planning_interface::MoveGroupInterface& moveGroup)
{
    arm_planning::path_planning::computeTimeFromStart(trajectory, 0.1);
    robot_trajectory::RobotTrajectory rt(moveGroup.getCurrentState()->getRobotModel(), moveGroup.getName());
    
    rt.setRobotTrajectoryMsg(*moveGroup.getCurrentState(), trajectory);// get a RobotTrajectory from trajectory
    trajectory_processing::IterativeParabolicTimeParameterization iptp;
    if (!iptp.computeTimeStamps(rt))
    {
        ROS_WARN("computed time stamp FAILED.");
        return false;
    }
    rt.getRobotTrajectoryMsg(trajectory);// Get RobotTrajectory_msg from RobotTrajectory
    return true;
}

void arm_planning::path_planning::scaleTrajectorySpeed(moveit_msgs::RobotTrajectory& trajectory, double scale)
{    
    for (unsigned int i = 0; i < trajectory.joint_trajectory.points.size(); i++)
    {        
        trajectory.joint_trajectory.points[i].time_from_start.fromSec(trajectory.joint_trajectory.points[i].time_from_start.toSec()/scale);
        for (unsigned int j = 0; j < trajectory.joint_trajectory.joint_names.size(); j++)
        {            
            trajectory.joint_trajectory.points[i].velocities[j] *= scale;            
            trajectory.joint_trajectory.points[i].accelerations[j] *= scale;        
        }
    }
}

moveit::planning_interface::MoveGroupInterface::Plan arm_planning::path_planning::CartesianPath(moveit::planning_interface::MoveGroupInterface &group, Object *target_p)//笛卡尔路径规划（单目标点）
{
	// moveit_msgs::RobotState current_state_msg;
    // moveit::core::robotStateToRobotStateMsg(getCurrentRobotState(), current_state_msg)

	// group.setStartState(current_state_msg);
	group.setStartState(*group.getCurrentState());
	//group.setStartStateToCurrentState();
	std::vector<geometry_msgs::Pose> waypoints;
	geometry_msgs::Pose target_pose ;
////	KDL::Frame kdl_frame;	

    group.setPlanningTime(5);
    group.setNumPlanningAttempts(25);

	// std::vector<double> rpy = group.getCurrentRPY(group.getEndEffectorLink());

	//transform quaternion to RPY
////	dual_arm_toolbox::Transform::transformPoseToKDL(target_p->pose,kdl_frame);

	//KDL
/*************************************/

	Path_RoundedComposite* path = new Path_RoundedComposite(0.05, 0.01, new RotationalInterpolation_SingleAxis());
	//0.1:过渡圆弧半径;0.01:等效半径;RotationalInterpolation_SingleAxis():旋转处理算法
	path->Add(Frame(Rotation::RPY(target_p->pose_rpy.r, target_p->pose_rpy.p, target_p->pose_rpy.y), Vector(target_p->pose.position.x, target_p->pose.position.y, target_p->pose.position.z))); ////
////	path->Add(kdl_frame); 

	path->Finish();
//	VelocityProfile* velpref = new VelocityProfile_Trap(0.1, 1);//梯形速度：0.1，加速度：1

    KDL::VelocityProfile_Spline* velpref = new KDL::VelocityProfile_Spline();

	velpref->SetProfile(0, path->PathLength());
	Trajectory* traject = new Trajectory_Segment(path, velpref);
										
	double dt = 0.01;//0.1 is so short
	for (double t = 0.0; t <= traject->Duration(); t += dt)
	{
		Frame current_pose;
		current_pose = traject->Pos(t);//t时刻对应的轨迹
		dual_arm_toolbox::Transform::transformKDLtoPose(current_pose,target_pose);
		waypoints.push_back(target_pose);
	}

	//笛卡尔空间路径规划
	moveit_msgs::RobotTrajectory trajectory_msg;
	double fraction = group.computeCartesianPath(waypoints,
		0.001, // eef_step,
		0.0, // jump_threshold
		trajectory_msg,
		true);

	ROS_WARN("%s cartesian path (%.2f%% acheived)", group.getEndEffectorLink().c_str(),fraction * 100.0); 
/*	if (fraction < 0.9) {
            ROS_WARN("UR5 cartesian path. (%.2f%% achieved)", fraction * 100.0);
            count++;
			//if(count>=5) break;
			continue;            
        }
    else {
 */         //  dual_arm_path_planning::path_planning::clean(trajectory_msg);

	if(!computeVelocities(trajectory_msg, group))
	{//TOOP
		ROS_WARN("TOOP processing FAILED.");       
	}

	moveit::planning_interface::MoveGroupInterface::Plan plan;	
	plan.trajectory_ = trajectory_msg;

	return plan;
}
//重载CartesianPath（）函数
moveit::planning_interface::MoveGroupInterface::Plan arm_planning::path_planning::CartesianPath(moveit::planning_interface::MoveGroupInterface &group, Object *target_p, const moveit_msgs::Constraints &path_constraints)//笛卡尔路径规划（单目标点）
{
	// moveit_msgs::RobotState current_state_msg;
    // moveit::core::robotStateToRobotStateMsg(getCurrentRobotState(), current_state_msg)

	// group.setStartState(current_state_msg);
	group.setStartState(*group.getCurrentState());
	//group.setStartStateToCurrentState();
	std::vector<geometry_msgs::Pose> waypoints;
	geometry_msgs::Pose target_pose ;
////	KDL::Frame kdl_frame;	

    group.setPlanningTime(5);
    group.setNumPlanningAttempts(25);

	// std::vector<double> pos;
	// pos.push_back(group.getCurrentPose().pose.position.x);
	// pos.push_back(group.getCurrentPose().pose.position.y);
	// pos.push_back(group.getCurrentPose().pose.position.z);

	// std::vector<double> rpy = group.getCurrentRPY(group.getEndEffectorLink());

	//transform quaternion to RPY
////	dual_arm_toolbox::Transform::transformPoseToKDL(target_p->pose,kdl_frame);

	//KDL
/*************************************/

	Path_RoundedComposite* path = new Path_RoundedComposite(0.05, 0.01, new RotationalInterpolation_SingleAxis());
	//0.1:过渡圆弧半径;0.01:等效半径;RotationalInterpolation_SingleAxis():旋转处理算法
//	path->Add(Frame(Rotation::RPY(rpy[0], rpy[1], rpy[2]), Vector(0.7,-0.6,1.2)));
	path->Add(Frame(Rotation::RPY(target_p->pose_rpy.r, target_p->pose_rpy.p, target_p->pose_rpy.y), Vector(target_p->pose.position.x, target_p->pose.position.y, target_p->pose.position.z))); ////
////	path->Add(kdl_frame); 

	path->Finish();
//	VelocityProfile* velpref = new VelocityProfile_Trap(0.1, 1);//梯形速度：0.1，加速度：1

    KDL::VelocityProfile_Spline* velpref = new KDL::VelocityProfile_Spline();

	velpref->SetProfile(0, path->PathLength());
	Trajectory* traject = new Trajectory_Segment(path, velpref);
										
	double dt = 0.01;//0.1 is so short
	for (double t = 0.0; t <= traject->Duration(); t += dt)
	{
		Frame current_pose;
		current_pose = traject->Pos(t);//t时刻对应的轨迹
		dual_arm_toolbox::Transform::transformKDLtoPose(current_pose,target_pose);
		waypoints.push_back(target_pose);
	}

	//笛卡尔空间路径规划
	moveit_msgs::RobotTrajectory trajectory_msg;
	double fraction = group.computeCartesianPath(waypoints,
		0.001, // eef_step,
		0.0, // jump_threshold
		trajectory_msg,
		path_constraints,//路径约束
		true);

	ROS_WARN("%s cartesian path (%.2f%% acheived)", group.getEndEffectorLink().c_str(),fraction * 100.0); 
/*	if (fraction < 0.9) {
            ROS_WARN("UR5 cartesian path. (%.2f%% achieved)", fraction * 100.0);
            count++;
			//if(count>=5) break;
			continue;            
        }
    else {
 */         //  dual_arm_path_planning::path_planning::clean(trajectory_msg);

	if(!computeVelocities(trajectory_msg, group))
	{//TOOP
		ROS_WARN("TOOP processing FAILED.");       
	}

	moveit::planning_interface::MoveGroupInterface::Plan plan;	
	plan.trajectory_ = trajectory_msg;

	return plan;
}


moveit::planning_interface::MoveGroupInterface::Plan arm_planning::path_planning::CartesianPath_arc(moveit::planning_interface::MoveGroupInterface &group, Object *target_p[], int len)//笛卡尔路径规划（圆弧过渡，需多目标点）
{

	group.setStartState(*group.getCurrentState());
	//group.setStartStateToCurrentState();
	std::vector<geometry_msgs::Pose> waypoints;
	geometry_msgs::Pose target_pose;
////	KDL::Frame kdl_frame;	

    group.setPlanningTime(5);
    group.setNumPlanningAttempts(25);

	//KDL
/*************************************/

	Path_RoundedComposite* path = new Path_RoundedComposite(0.05, 0.01, new RotationalInterpolation_SingleAxis());
	//0.1:过渡圆弧半径;0.01:等效半径;RotationalInterpolation_SingleAxis():旋转处理算法

	//transform quaternion to RPY
	for(int i=0; i < len; i++){
////		dual_arm_toolbox::Transform::transformPoseToKDL(target_p[i]->pose,kdl_frame);
		path->Add(Frame(Rotation::RPY(target_p[i]->pose_rpy.r, target_p[i]->pose_rpy.p, target_p[i]->pose_rpy.y), Vector(target_p[i]->pose.position.x, target_p[i]->pose.position.y, target_p[i]->pose.position.z)));
////		path->Add(kdl_frame); 
	}
//	path->Add(Frame(Rotation::RPY(target.roll, target.pitch, target.yall), Vector(target.x, target.y, target.z)));	
	path->Finish();
	VelocityProfile* velpref = new VelocityProfile_Trap(0.1, 1);//梯形速度：0.1，加速度：1

	velpref->SetProfile(0, path->PathLength());
	Trajectory* traject = new Trajectory_Segment(path, velpref);

											
	double dt = 0.01;//0.1 is so short
	for (double t = 0.0; t <= traject->Duration(); t += dt)
	{
		Frame current_pose;
		current_pose = traject->Pos(t);//t时刻对应的轨迹
		dual_arm_toolbox::Transform::transformKDLtoPose(current_pose,target_pose);
		waypoints.push_back(target_pose);
	}

	//笛卡尔空间路径规划
	moveit_msgs::RobotTrajectory trajectory_msg;
	double fraction = group.computeCartesianPath(waypoints,
		0.001, // eef_step,
		0.0, // jump_threshold
		trajectory_msg,
		true);

	ROS_WARN("%s cartesian path (%.2f%% acheived)", group.getEndEffectorLink().c_str(),fraction * 100.0);

	if(!computeVelocities(trajectory_msg,group)){//TOOP
		ROS_WARN("TOOP processing FAILED.");       
	}

	moveit::planning_interface::MoveGroupInterface::Plan plan;	
	plan.trajectory_ = trajectory_msg;

	return plan;
}


//重载CartesianPath_arc()函数
moveit::planning_interface::MoveGroupInterface::Plan arm_planning::path_planning::CartesianPath_arc(moveit::planning_interface::MoveGroupInterface &group, Object *target_p[], int len,const moveit_msgs::Constraints &path_constraints)//笛卡尔路径规划（圆弧过渡，需多目标点）
{

	group.setStartState(*group.getCurrentState());
	//group.setStartStateToCurrentState();
	std::vector<geometry_msgs::Pose> waypoints;
	geometry_msgs::Pose target_pose;
////	KDL::Frame kdl_frame;	

    group.setPlanningTime(5);
    group.setNumPlanningAttempts(25);

	//KDL
/*************************************/

	Path_RoundedComposite* path = new Path_RoundedComposite(0.05, 0.01, new RotationalInterpolation_SingleAxis());
	//0.1:过渡圆弧半径;0.01:等效半径;RotationalInterpolation_SingleAxis():旋转处理算法

	//transform quaternion to RPY
	for(int i=0; i < len; i++){
////		dual_arm_toolbox::Transform::transformPoseToKDL(target_p[i]->pose,kdl_frame);
			path->Add(Frame(Rotation::RPY(target_p[i]->pose_rpy.r, target_p[i]->pose_rpy.p, target_p[i]->pose_rpy.y), Vector(target_p[i]->pose.position.x, target_p[i]->pose.position.y, target_p[i]->pose.position.z)));
////		path->Add(kdl_frame); 
	}
//	path->Add(Frame(Rotation::RPY(target.roll, target.pitch, target.yall), Vector(target.x, target.y, target.z)));	
	path->Finish();
	VelocityProfile* velpref = new VelocityProfile_Trap(0.1, 1);//梯形速度：0.1，加速度：1

	velpref->SetProfile(0, path->PathLength());
	Trajectory* traject = new Trajectory_Segment(path, velpref);

											
	double dt = 0.01;//0.1 is so short
	for (double t = 0.0; t <= traject->Duration(); t += dt)
	{
		Frame current_pose;
		current_pose = traject->Pos(t);//t时刻对应的轨迹
		dual_arm_toolbox::Transform::transformKDLtoPose(current_pose,target_pose);
		waypoints.push_back(target_pose);
	}

	//笛卡尔空间路径规划
	moveit_msgs::RobotTrajectory trajectory_msg;
	double fraction = group.computeCartesianPath(waypoints,
		0.001, // eef_step,
		0.0, // jump_threshold
		trajectory_msg,
		path_constraints,
		true);

	ROS_WARN("%s cartesian path (%.2f%% acheived)", group.getEndEffectorLink().c_str(),fraction * 100.0);

	if(!computeVelocities(trajectory_msg,group)){//TOOP
		ROS_WARN("TOOP processing FAILED.");       
	}

	moveit::planning_interface::MoveGroupInterface::Plan plan;	
	plan.trajectory_ = trajectory_msg;

	return plan;
}

/**
* @p2p_planning, point to point planning 
* @param a : pose of a object
* @param hole : pose of a hole
*/
moveit::planning_interface::MoveGroupInterface::Plan arm_planning::path_planning::setpose_planning(moveit::planning_interface::MoveGroupInterface &group, Object *end_p)
{
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    
    geometry_msgs::Pose target_pose1;

    target_pose1 = end_p->pose;

    group.setPoseTarget(target_pose1);
    group.setPlanningTime(10);
   
    // 进行运动规划，计算机器人移动到目标的运动轨迹，此时只是计算出轨迹，并不会控制机械臂运动
    //bool success = group.plan(plan);
	bool success = (group.plan(plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);

	
	return plan;
}

void arm_planning::path_planning::spiral_search_planning(int p_num, double a, double *x, double *y)
{
    double theta_max = 10 * PI;  //圈数
    //int p_num = 100;
    //int a = 2;
    double r;
    double theta_step = theta_max / p_num;
    //double x[len], y[len];
    for (int i = 0; i < p_num; i++)
    {
        r = a * theta_step;
        x[i] = r * cos(theta_step);
        y[i] = r * sin(theta_step);
    }  
}

double dist_compute(Object *a, Object *b)
{
	return sqrt((a->pose.position.x - b->pose.position.x) * (a->pose.position.x - b->pose.position.x) + 
				(a->pose.position.y - b->pose.position.y) * (a->pose.position.y - b->pose.position.y) + 
				(a->pose.position.z - b->pose.position.z) * (a->pose.position.z - b->pose.position.z));
}

