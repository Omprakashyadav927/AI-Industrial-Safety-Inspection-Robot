#!/usr/bin/env python3

"""
inspection_node.py

AI-Powered Industrial Safety Inspection Robot

Responsibilities:
- Initialize ROS2 node
- Load ROS2 parameters
- Verify system configuration
- Prepare future AI inspection pipeline
"""

import rclpy
from rclpy.node import Node


class InspectionNode(Node):
    """Main node for the AI Safety Inspection Robot."""

    def __init__(self):
        super().__init__("inspection_node")

        # Declare ROS2 parameters
        self.declare_parameter(
            "robot_name",
            "AI_Industrial_Safety_Inspection_Robot"
        )

        self.declare_parameter(
            "inspection_frequency",
            1.0
        )

        self.declare_parameter(
            "system_status",
            "READY"
        )

        self.declare_parameter(
            "camera_enabled",
            False
        )

        self.declare_parameter(
            "camera_topic",
            "/camera/image_raw"
        )

        self.declare_parameter(
            "ai_detection_enabled",
            False
        )

        self.declare_parameter(
            "model_path",
            "models/safety_detection.onnx"
        )

        self.declare_parameter(
            "database_logging_enabled",
            True
        )

        self.declare_parameter(
            "database_path",
            "database/inspection.db"
        )

        # Read parameters
        self.robot_name = self.get_parameter(
            "robot_name"
        ).value

        self.inspection_frequency = self.get_parameter(
            "inspection_frequency"
        ).value

        self.system_status = self.get_parameter(
            "system_status"
        ).value

        self.camera_enabled = self.get_parameter(
            "camera_enabled"
        ).value

        self.camera_topic = self.get_parameter(
            "camera_topic"
        ).value

        self.ai_detection_enabled = self.get_parameter(
            "ai_detection_enabled"
        ).value

        self.model_path = self.get_parameter(
            "model_path"
        ).value

        self.database_logging_enabled = self.get_parameter(
            "database_logging_enabled"
        ).value

        self.database_path = self.get_parameter(
            "database_path"
        ).value


        # Startup logs
        self.get_logger().info("=" * 60)
        self.get_logger().info("AI Safety Inspection Robot Started")
        self.get_logger().info("ROS2 Node Initialized Successfully")

        self.get_logger().info(
            f"Robot Name : {self.robot_name}"
        )

        self.get_logger().info(
            f"Inspection Frequency : {self.inspection_frequency} Hz"
        )

        self.get_logger().info(
            f"System Status : {self.system_status}"
        )

        self.get_logger().info(
            f"Camera Enabled : {self.camera_enabled}"
        )

        self.get_logger().info(
            f"AI Detection Enabled : {self.ai_detection_enabled}"
        )

        self.get_logger().info(
            f"Database Logging : {self.database_logging_enabled}"
        )

        self.get_logger().info("=" * 60)


def main(args=None):
    rclpy.init(args=args)

    node = InspectionNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            "Shutting down Inspection Robot..."
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
