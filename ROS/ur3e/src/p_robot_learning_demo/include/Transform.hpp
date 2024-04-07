//
// Created by daniel on 27.12.16.
//

#ifndef PROJECT_TRANSFORM_H
#define PROJECT_TRANSFORM_H

// ROS
#include <ros/ros.h>
#include <geometry_msgs/Pose.h>

// Controller Manager  该service请求包含要启动的controller名字list
/*要停止的controller名字list，以及一个表明约束度 (BEST_EFFORT or STRICT)的int变量。
STRICT意思是只要有一个controller无效,，switch就会失败。  BEST_EFFORT意思是有些controller无效
但是仍然会启动/停止其它剩余controller。 service响应以bool指示成功or失败。*/
#include <controller_manager_msgs/SwitchController.h>
#include <controller_manager_msgs/SwitchControllerRequest.h>
#include <controller_manager_msgs/SwitchControllerResponse.h>

// MoveIt!
#include <moveit_msgs/PlanningScene.h>//
#include <moveit/move_group_interface/move_group_interface.h> //规划组
#include <moveit/planning_scene_interface/planning_scene_interface.h>//场景规划
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/GetStateValidity.h>//服务消息
#include <moveit_msgs/DisplayRobotState.h>
//#include <controller_manager/controller_manager.h>
//#include <moveit_ros_control_interface>

// Rviz
#include <moveit_msgs/DisplayTrajectory.h>

// Trajectory tools
#include <moveit/robot_trajectory/robot_trajectory.h>
#include <moveit/trajectory_processing/iterative_time_parameterization.h>

// KDL
#include <kdl/frames_io.hpp>

//PyKDL中坐标系类Frame的成员M为其旋转矩阵，p为其原点坐标。
namespace dual_arm_toolbox{
    class Transform {
    protected:
    public:
        static void transformPoseToKDL(geometry_msgs::Pose pose, KDL::Frame& kdl_frame);
        static void transformKDLtoPose(KDL::Frame kdl_frame, geometry_msgs::Pose& pose);
    };
}
void dual_arm_toolbox::Transform::transformPoseToKDL(geometry_msgs::Pose pose, KDL::Frame& kdl_frame){
    kdl_frame.M = kdl_frame.M.Quaternion(
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w
    );
    kdl_frame.p.x(pose.position.x);
    kdl_frame.p.y(pose.position.y);
    kdl_frame.p.z(pose.position.z);
}
//将4*4的矩阵与点与四元数进行转换,坐标系类Frame的成员M为其旋转矩阵，p为其原点坐标。
void dual_arm_toolbox::Transform::transformKDLtoPose(KDL::Frame kdl_frame, geometry_msgs::Pose& pose){
    kdl_frame.M.GetQuaternion(
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w
    );
    pose.position.x = kdl_frame.p.x();
    pose.position.y = kdl_frame.p.y();
    pose.position.z = kdl_frame.p.z();
}
#endif //PROJECT_TRANSFORM_H
