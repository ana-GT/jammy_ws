from http.server import executable
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import TextSubstitution, PathJoinSubstitution, LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.event_handlers import OnProcessExit, OnExecutionComplete
from launch.launch_description_sources import PythonLaunchDescriptionSource


import os
from os import environ

from ament_index_python.packages import get_package_share_directory

import xacro


def generate_launch_description():
    # ld = LaunchDescription()

    humble_robots_path = get_package_share_directory('humble_robots')
    clearpath_platform_path = get_package_share_directory('clearpath_platform_description')

    # Determine all ros packages that are sourced
    packages_paths = [os.path.join(p, 'share') for p in os.getenv('AMENT_PREFIX_PATH').split(':')]

    gz_sim_resource_path = SetEnvironmentVariable(
        name='IGN_GAZEBO_RESOURCE_PATH',
        value=[
            os.path.join(humble_robots_path, 'worlds'),
            ':' + ':'.join(packages_paths)])

    world_model = os.path.join(humble_robots_path, 'worlds', 'simple.sdf')

    # Paths
    gz_sim_launch = PathJoinSubstitution(
        [get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])

    gui_config = PathJoinSubstitution(
        [get_package_share_directory('humble_robots'), 'config', 'husky', 'gui.config'])

    # Gazebo Simulator
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gz_sim_launch]),
        launch_arguments=[
            ('gz_args', [world_model,
                         ' -v 4',
                         ' --gui-config ',
                         gui_config])
        ]
    )







    # Clock bridge
    clock_bridge = Node(package='ros_gz_bridge',
                        executable='parameter_bridge',
                        name='clock_bridge',
                        output='screen',
                        arguments=[
                          '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock'
                        ])


    return LaunchDescription([
        gz_sim_resource_path,
        gz_sim,
        clock_bridge
    ])