from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    inspection_node = Node(
        package='inspection_robot',
        executable='inspection_node',
        name='inspection_node',
        output='screen'
    )

    return LaunchDescription([
        inspection_node
    ])
