import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.actions import TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'drone'
    package_share = get_package_share_directory(package_name)
    gazebo_share = get_package_share_directory('gazebo_ros')
    rviz_config = os.path.join(package_share, 'rviz', 'drone.rviz')
    gui = LaunchConfiguration('gui')
    description_file = os.path.join(
        package_share,
        'description',
        'drone.urdf.xacro',
    )

    robot_description = Command(['xacro ', description_file])

    return LaunchDescription([
        DeclareLaunchArgument(
            'gui',
            default_value='true',
            description='Start the Gazebo Classic GUI client.',
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_share, 'launch', 'gzserver.launch.py')
            )
        ),
        ExecuteProcess(
            cmd=['gzclient'],
            output='screen',
            condition=IfCondition(gui),
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen',
        ),
        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='gazebo_ros',
                    executable='spawn_entity.py',
                    arguments=[
                        '-topic',
                        'robot_description',
                        '-entity',
                        'nidar_drone',
                        '-z',
                        '0.5',
                    ],
                    output='screen',
                ),
            ],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen',
        ),
    ])
