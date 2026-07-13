#!/usr/bin/env python3

"""
inspection_node.py

AI-Powered Industrial Safety Inspection Robot

Responsibilities (current):
- Initialize ROS2 node
- Verify project setup
- Print startup message

Future Responsibilities:
- Camera subscriber
- YOLOv8 inference
- PPE violation detection
- SQLite logging
- Image saving
- Inspection report generation
"""

import rclpy
from rclpy.node import Node


class InspectionNode(Node):
    """Main node for the AI Safety Inspection Robot."""

    def __init__(self):
        super().__init__("inspection_node")

        self.get_logger().info("=" * 60)
        self.get_logger().info("AI Safety Inspection Robot Started")
        self.get_logger().info("ROS2 Node Initialized Successfully")
        self.get_logger().info("System Status : READY")
        self.get_logger().info("=" * 60)


def main(args=None):
    rclpy.init(args=args)

    node = InspectionNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Inspection Robot...")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
