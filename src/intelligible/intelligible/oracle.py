import rclpy
import logging
from rclpy.node import Node
from geometry_msgs.msg import Pose
from intelligible.publisher import Publisher


class Oracle(Node):
    def __init__(self):
        super().__init__("oracle")
        self.oracle = Publisher(self, "enqueue", "/enqueue", Pose)
        self.oracle.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Pose()
        msg.position.x = float(input('Enter x position: '))
        msg.position.y = float(input('Enter y position: '))
        msg.position.z = float(input('Enter z position: '))

        self.oracle.publish(msg)

        self.get_logger().info(f"Pose {msg.position.x, msg.position.y, msg.position.z} published.")

    def destroy(self):
        self.oracle.destroy_pub()
        self.destroy_node()


def main(args=None):
    rclpy.init(args=args)
    oracle_node = Oracle()
    rclpy.spin(oracle_node)
    oracle_node.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()