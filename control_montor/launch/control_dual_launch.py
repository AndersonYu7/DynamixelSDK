from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='Control_Motor',
            namespace='',
            executable='control_dual',
            name='Control_motor'
        ),
        Node(
            package='Control_Motor',
            namespace='',
            executable='Twist2Speed',
            name='Twist2Speed'
        )
    ])