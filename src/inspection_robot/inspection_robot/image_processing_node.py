#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class ImageProcessingNode(Node):

    def __init__(self):
        super().__init__("image_processing_node")

        self.bridge = CvBridge()

        # Subscriber
        self.image_subscriber = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        # Publisher
        self.image_publisher = self.create_publisher(
            Image,
            "/processed/image",
            10
        )

        self.get_logger().info("=" * 50)
        self.get_logger().info("Image Processing Node Started")
        self.get_logger().info("Subscribed : /camera/image_raw")
        self.get_logger().info("Publishing : /processed/image")
        self.get_logger().info("=" * 50)

    def image_callback(self, msg):

        try:
            # ROS Image → OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            # Future image processing can be added here
            processed_image = cv_image

            # OpenCV → ROS Image
            output_msg = self.bridge.cv2_to_imgmsg(
                processed_image,
                encoding="bgr8"
            )

            self.image_publisher.publish(output_msg)

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
        node.get_logger().info(
            "Shutting down Image Processing Node..."
        )

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()

