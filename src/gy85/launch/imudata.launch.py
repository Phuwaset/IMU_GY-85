import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gy85',
            executable='imu_node',
            name='imu_node'
        ),
    ])
