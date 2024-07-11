
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():

    urdf_path = '/home/will/AckermanProject/xacro/ackerman_plus.xacro'

    pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path])
        }]
    )

    joint = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output='screen'
    )

    rviz = ExecuteProcess(
        cmd=['rviz2', '-d', '/home/will/AckermanProject/rviz_config/config.rviz'],
        output='screen'
    )

    return LaunchDescription([
        pub,
        joint,
        rviz
    ])
