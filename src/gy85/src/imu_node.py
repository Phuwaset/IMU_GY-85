import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3
from time import sleep
import sys

# Import necessary i2clibraries and configure them here
sys.path.insert(1, '/home/ubuntu/IMU_GY-85/src/gy85')  # Adjust to your package's path
from i2clibraries.i2c_adxl345 import i2c_adxl345
from i2clibraries.i2c_itg3205 import i2c_itg3205

class ImuNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        self.timer = self.create_timer(1, self.publish_data)
        
        # Initialize your i2clibraries devices here
        self.adxl345 = i2c_adxl345(1)
        self.itg3205 = i2c_itg3205(1)

    def publish_data(self):
        msg = Imu()

        # Accelerometer data
        accel_data = self.adxl345.getAxes()
        msg.linear_acceleration = Vector3()
        msg.linear_acceleration.x = accel_data[0]
        msg.linear_acceleration.y = accel_data[1]
        msg.linear_acceleration.z = accel_data[2]

        # Gyroscope data
        (itgready, dataready) = self.itg3205.getInterruptStatus()
        if dataready:
            temp = self.itg3205.getDieTemperature()
            (x, y, z) = self.itg3205.getDegPerSecAxes()
            msg.angular_velocity = Vector3()
            msg.angular_velocity.x = x
            msg.angular_velocity.y = y
            msg.angular_velocity.z = z

        # Fill in the header
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_frame'  # Change this to the appropriate frame ID

        # Fill in covariance matrices
        msg.orientation_covariance = [0.0] * 9
        msg.angular_velocity_covariance = [0.0] * 9
        msg.linear_acceleration_covariance = [0.0] * 9

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
