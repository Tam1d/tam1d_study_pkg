#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__('even_pub')
        
        self.publisher = self.create_publisher(Int32, 'even_numbers', 10)
        self.counter = 0

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter

        self.publisher.publish(msg)
        self.get_logger().info(f'{msg.data}')
        
        self.counter = 0 if self.counter >= 98 else self.counter + 2

def main():
    rclpy.init()

    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()

