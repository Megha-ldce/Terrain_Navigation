#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
from geometry_msgs.msg import Twist
import sensor_msgs_py.point_cloud2 as pc2
import numpy as np

class TerrainDetector(Node):
    def __init__(self):
        super().__init__('terrain_detector')
        
        # Subscribers
        self.depth_sub = self.create_subscription(
            PointCloud2,
            '/depth_camera/points',
            self.depth_callback,
            10
        )
        
        # Publishers
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Parameters
        self.ditch_threshold = -0.3  # 30cm drop
        self.safe_distance = 1.0  # meters ahead to check
        self.stop_detected = False
        
        self.get_logger().info('Terrain Detector Node Started')
        
    def depth_callback(self, msg):
        # Convert point cloud to numpy array
        points = []
        for point in pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            points.append([point[0], point[1], point[2]])
        
        if len(points) == 0:
            return
            
        points = np.array(points)
        
        # Check region ahead of robot (0.5m to 2m ahead, centered)
        forward_points = points[
            (points[:, 0] > 0.5) & (points[:, 0] < 2.0) &  # Forward range
            (np.abs(points[:, 1]) < 0.5)  # Width in front
        ]
        
        if len(forward_points) == 0:
            self.publish_safe_velocity()
            return
        
        # Check for sudden drops (ditches)
        min_height = np.min(forward_points[:, 2])
        
        if min_height < self.ditch_threshold:
            self.get_logger().warn(f'DITCH DETECTED! Min height: {min_height:.2f}m')
            self.stop_robot()
        else:
            self.publish_safe_velocity()
    
    def stop_robot(self):
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)
        self.stop_detected = True
    
    def publish_safe_velocity(self):
        if not self.stop_detected:
            cmd = Twist()
            cmd.linear.x = 0.3  # Slow forward speed
            cmd.angular.z = 0.0
            self.cmd_vel_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TerrainDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
