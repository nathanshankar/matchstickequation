import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EquationSolverClient(Node):

    def __init__(self):
        super().__init__('equation_solver_client')
        self.publisher_ = self.create_publisher(String, 'equation_input', 10)
        self.subscription = self.create_subscription(
            String,
            'equation_result',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received equation result: "%s"' % msg.data)

    def send_equation(self, equation):
        self.publisher_.publish(String(data=equation))


def main(args=None):
    rclpy.init(args=args)

    equation_solver_client = EquationSolverClient()

    while True:
        equation = input("Enter an equation (or 'exit' to quit): ")
        if equation.lower() == 'exit':
            break
        equation_solver_client.send_equation(equation)

    equation_solver_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
