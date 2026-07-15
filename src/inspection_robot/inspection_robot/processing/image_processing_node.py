#!/usr/bin/env python3

"""
image_processing_node.py

AI-Powered Industrial Safety Inspection Robot

Responsibilities:
- Subscribe to video image stream
- Convert ROS2 Image messages to OpenCV frames
- Publish processed image stream
- Prepare future YOLOv8 pipeline

Input Topic:
- /video/image_raw

Output Topic:
- /processed/image
"""

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class ImageProcessingNode(Node):

    def __init__(self):
        super().__init__("image_processing_node")

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            "/video/image_raw",
            self.image_callback,
            10
        )

        self.processed_image_publisher = self.create_publisher(
            Image,
            "/processed/image",
            10
        )

        self.get_logger().info(
            "Image Processing Node Started"
        )

    def image_callback(self, msg):

        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                "bgr8"
            )

            height, width = frame.shape[:2]

            # Future:
            # YOLOv8 detection will be added here

            processed_msg = self.bridge.cv2_to_imgmsg(
                frame,
                "bgr8"
            )

            self.processed_image_publisher.publish(
                processed_msg
            )

            self.get_logger().info(
                f"Published processed frame: {width}x{height}",
                throttle_duration_sec=5
            )

        except Exception as error:
            self.get_logger().error(
                f"Image processing failed: {error}"
            )


def main(args=None):

    rclpy.init(args=args)

    node = ImageProcessingNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
