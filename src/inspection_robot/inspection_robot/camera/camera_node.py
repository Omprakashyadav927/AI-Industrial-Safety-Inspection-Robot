#!/usr/bin/env python3

"""
camera_node.py

Camera Interface Module

Responsibilities:
- Initialize ROS2 camera node
- Subscribe to ROS2 image topic
- Convert ROS Image message to OpenCV format
- Provide future AI pipeline input

Future:
- YOLOv8 detection
- Image preprocessing
- Safety object detection
"""

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class CameraNode(Node):
    """ROS2 Camera Interface Node."""

    def __init__(self):
        super().__init__("camera_node")

        # ROS2 parameters
        self.declare_parameter(
            "camera_topic",
            "/camera/image_raw"
        )

        self.camera_topic = self.get_parameter(
            "camera_topic"
        ).value

        # OpenCV bridge
        self.bridge = CvBridge()

        # Image subscriber
        self.image_subscriber = self.create_subscription(
            Image,
            self.camera_topic,
            self.image_callback,
            10
        )

        self.get_logger().info("=" * 50)
        self.get_logger().info("Camera Interface Node Started")
        self.get_logger().info(
            f"Subscribed Topic: {self.camera_topic}"
        )
        self.get_logger().info("=" * 50)


    def image_callback(self, msg):
        """
        Receive ROS Image message
        Convert to OpenCV format
        """

        try:
            cv_image = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            # Future:
            # Send cv_image to YOLOv8 detector

        except Exception as error:
            self.get_logger().error(
                f"Camera conversion failed: {error}"
            )


def main(args=None):

    rclpy.init(args=args)

    node = CameraNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            "Shutting down Camera Node..."
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
