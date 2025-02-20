import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatesRelay(Node):
    def __init__(self):
        super().__init__('joint_states_relay')
        self.subscription = self.create_subscription(
            JointState,
            '/ros1_joint_states',
            self.joint_states_callback,
            10
        )
        self.publisher = self.create_publisher(JointState, '/joint_states', 10)

    def joint_states_callback(self, msg):
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = JointStatesRelay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
