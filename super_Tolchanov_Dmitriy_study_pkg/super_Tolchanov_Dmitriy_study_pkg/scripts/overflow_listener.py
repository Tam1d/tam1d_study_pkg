#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int32

class Listener(Node):

    def __init__(self):
        super().__init__('overflow_listener')

        self.subscription = self.create_subscription(Int32, 'overflow', self.callback, 10)

        #self.get_logger().info("Узел listener запущен и слушает топик!")

    def callback(self, msg):
        self.get_logger().warn(f"!!! ПЕРЕПОЛНЕНИЕ !!! Получено значение: {msg.data}")

def main():
    rclpy.init() 
    
    node = Listener() 
    
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
