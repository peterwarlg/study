//包含API的头文件
//http://www.ncnynl.com/archives/201609/864.html
//https://answers.ros.org/question/234371/creating-a-collisionobject-from-a-mesh-in-indigo/
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>

#include "geometric_shapes/shapes.h"
#include "geometric_shapes/mesh_operations.h"
#include "geometric_shapes/shape_operations.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "add_object");
    ros::NodeHandle nh;
    ros::AsyncSpinner spin(1);
    spin.start();

    //创建运动规划场景，等待创建完成
    moveit::planning_interface::PlanningSceneInterface current_scene;
    sleep(2.0);

    /*moveit_msgs::CollisionObject cube;
    shapes::Mesh* m = shapes::createMeshFromResource("package://ur_platform/meshes/cube.STL");
    shape_msgs::Mesh cube_mesh;
    shapes::ShapeMsg cube_mesh_msg;
    shapes::constructMsgFromShape(m, cube_mesh_msg);
    cube_mesh = boost::get<shape_msgs::Mesh>(cube_mesh_msg);
    cube.meshes.resize(1);
    cube.meshes[0] = cube_mesh;
    cube.mesh_poses.resize(1);
    cube.mesh_poses[0].position.x = 0.2;
    cube.mesh_poses[0].position.y = 0.7;
    cube.mesh_poses[0].position.z = 0.83;
    cube.mesh_poses[0].orientation.w = 1;
    cube.mesh_poses[0].orientation.x = 0;
    cube.mesh_poses[0].orientation.y = 0;
    cube.mesh_poses[0].orientation.z = 0;

    cube.meshes.push_back(cube_mesh);
    cube.mesh_poses.push_back(cube.mesh_poses[0]);
    cube.operation = cube.ADD;

    std::vector<moveit_msgs::CollisionObject> collision_objects;
    collision_objects.push_back(cube);
    
    ROS_INFO("Add an object into the world");
    current_scene.addCollisionObjects(collision_objects);*/

	moveit_msgs::CollisionObject collision_object;
	collision_object.header.frame_id = "world";

	/* The id of the object is used to identify it. */
	collision_object.id = "box1";

	/* Define a box to add to the world. */
	shape_msgs::SolidPrimitive primitive;
	primitive.type = primitive.BOX;
	primitive.dimensions.resize(3);
	primitive.dimensions[0] = 1.6;
	primitive.dimensions[1] = 1.6;
	primitive.dimensions[2] = 0.02;

	/* A pose for the box (specified relative to frame_id) */
	geometry_msgs::Pose box_pose;
	box_pose.orientation.w = 1.0;
	box_pose.position.x =  0.4;
	box_pose.position.y = 0.55;
	box_pose.position.z =  0.82;

	collision_object.primitives.push_back(primitive);
	collision_object.primitive_poses.push_back(box_pose);
	collision_object.operation = collision_object.ADD;

	std::vector<moveit_msgs::CollisionObject> collision_objects;
	collision_objects.push_back(collision_object);
        current_scene.addCollisionObjects(collision_objects);

    ros::shutdown();
    return 0;
    
}
