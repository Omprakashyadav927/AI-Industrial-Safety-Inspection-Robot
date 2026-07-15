#!/usr/bin/env python3

"""
video_source_node.py

Recorded Video Input Node

Responsibilities:
- Read recorded inspection video using OpenCV
- Convert frames to ROS2 Image messages
- Publish frames for AI inspection pipeline

Topic:
- /video/image_raw
"""

import rclpy
from rclpy.node import Node

import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class VideoSourceNode(Node):
    """ROS2 node for recorded video input."""

    def __init__(self):
        super().__init__("video_source_node")

        self.declare_parameter(
            "video_path",
            "videos/inspection_video.mp4"
        )

        self.declare_parameter(
            "publish_rate",
            10.0
        )

        self.video_path = self.get_parameter(
            "video_path"
        ).value

        self.publish_rate = self.get_parameter(
            "publish_rate"
        ).value

        self.bridge = CvBridge()

        self.publisher = self.create_publisher(
            Image,
            "/video/image_raw",
            10
        )

        self.cap = cv2.VideoCapture(
            self.video_path
        )

        if not self.cap.isOpened():
            self.get_logger().error(
                f"Failed to open video: {self.video_path}"
            )
        else:
            self.get_logger().info(
                f"Video opened: {self.video_path}"
            )

        self.timer = self.create_timer(
            1.0 / self.publish_rate,
            self.publish_frame
        )

    def publish_frame(self):

        if not self.cap.isOpened():
            return

        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().info(
                "Video finished"
            )
            self.cap.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )
            return

        try:
            msg = self.bridge.cv2_to_imgmsg(
                frame,
                encoding="bgr8"
            )

            self.publisher.publish(msg)

        except Exception as error:
            self.get_logger().error(
                f"Image conversion failed: {error}"
            )


def main(args=None):

    rclpy.init(args=args)

    node = VideoSourceNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.cap.release()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
