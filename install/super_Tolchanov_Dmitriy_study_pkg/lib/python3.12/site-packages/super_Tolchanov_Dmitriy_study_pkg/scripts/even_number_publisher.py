#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__('even_pub')
        
        self.publisher = self.create_publisher(Int32, 'even_numbers', 10)
        self.overflow_pub = self.create_publisher(Int32, 'overflow', 10)
        self.counter = 0

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        
        if self.counter >= 100:
            self.overflow_pub.publish(msg)
            self.get_logger().info(f'Printed in /overflow: {msg.data}')
            self.counter = 0
        else:
            self.publisher.publish(msg)
            self.get_logger().info(f'Printed in /even_numbers: {msg.data}')
            
            self.counter += 2

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

