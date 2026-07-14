import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray

from cv_bridge import CvBridge
from ultralytics import YOLO


class YOLOv8DetectionNode(Node):

    def __init__(self):
        super().__init__('yolov8_detection_node')

        self.get_logger().info("Starting YOLOv8 Detection Node...")

        # CvBridge
        self.bridge = CvBridge()

        # Load YOLOv8 model
        self.model = YOLO("yolov8n.pt")

        self.get_logger().info("YOLOv8 model loaded successfully.")

        # Subscriber
        self.image_sub = self.create_subscription(
            Image,
            "/processed/image",
            self.image_callback,
            10
        )

        # Publishers
        self.image_pub = self.create_publisher(
            Image,
            "/detection/image",
            10
        )

        self.detection_pub = self.create_publisher(
            Detection2DArray,
            "/detections",
            10
        )

    def image_callback(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)

    node = YOLOv8DetectionNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()