import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from time import sleep
import sys

sys.path.insert(1, '/home/ubuntu/IMU_GY-85/src/gy85')
from i2clibraries.i2c_adxl345 import i2c_adxl345
from i2clibraries.i2c_itg3205 import i2c_itg3205

class ImuNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        self.timer = self.create_timer(1, self.publish_data)
        self.adxl345 = i2c_adxl345(1)
        self.itg3205 = i2c_itg3205(1)  # สร้างอินสแตนซ์ของ i2c_itg3205

    def publish_data(self):
        msg = Imu()

        # Accelerometer data
        accel_data = self.adxl345.getAxes()
        msg.linear_acceleration.x = accel_data[0]
        msg.linear_acceleration.y = accel_data[1]
        msg.linear_acceleration.z = accel_data[2]

        # Gyroscope data
        (itgready, dataready) = self.itg3205.getInterruptStatus()
        if dataready:
            temp = self.itg3205.getDieTemperature()
            (x, y, z) = self.itg3205.getDegPerSecAxes()
            msg.angular_velocity.x = x
            msg.angular_velocity.y = y
            msg.angular_velocity.z = z

        self.get_logger().info(f"Accelerometer data: {accel_data}, Gyroscope data: Temp={temp}, X={x}, Y={y}, Z={z}")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    imu_node = ImuNode()
    rclpy.spin(imu_node)
    imu_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
