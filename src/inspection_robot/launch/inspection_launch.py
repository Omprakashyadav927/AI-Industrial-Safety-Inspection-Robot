from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_name = 'inspection_robot'

    config_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'parameters.yaml'
    )

    inspection_node = Node(
        package=package_name,
        executable='inspection_node',
        name='inspection_node',
        output='screen',
        parameters=[
            config_file
        ]
    )

    return LaunchDescription([
        inspection_node
    ])
