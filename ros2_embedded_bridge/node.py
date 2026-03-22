"""Main ROS2 bridge node for embedded systems."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
import serial

class EmbeddedBridge(Node):
    def __init__(self):
        super().__init__('embedded_bridge')
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baud', 115200)

        port = self.get_parameter('port').value
        baud = self.get_parameter('baud').value
        self.serial = serial.Serial(port, baud, timeout=0.1)

        self.publisher_ = self.create_publisher(Float32MultiArray, 'embedded_sensors', 10)
        self.subscription = self.create_subscription(
            String, 'embedded_command', self.command_callback, 10)
        self.timer = self.create_timer(0.01, self.timer_callback)
        self.get_logger().info(f'Bridge started on {port}@{baud}')

    def command_callback(self, msg):
        cmd = msg.data.encode() + b'\n'
        self.serial.write(cmd)

    def timer_callback(self):
        if self.serial.in_waiting:
            line = self.serial.readline().decode('utf-8').strip()
            if line:
                try:
                    vals = [float(v) for v in line.split(',')]
                    msg = Float32MultiArray()
                    msg.data = vals
                    self.publisher_.publish(msg)
                except ValueError:
                    self.get_logger().warn(f'Malformed packet: {line}')

def main(args=None):
    rclpy.init(args=args)
    node = EmbeddedBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
