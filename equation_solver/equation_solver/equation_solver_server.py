import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from equation_solver.equation_processing import generate_combinations


class EquationSolverServer(Node):

    def __init__(self):
        super().__init__('equation_solver_server')
        self.publisher_ = self.create_publisher(String, 'equation_result', 10)
        self.subscription = self.create_subscription(
            String,
            'equation_input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        input_str = msg.data
        result_combinations = generate_combinations(input_str)

        for combination in result_combinations:
            self.publisher_.publish(String(data=combination))


def main(args=None):
    rclpy.init(args=args)

    equation_solver_server = EquationSolverServer()

    rclpy.spin(equation_solver_server)

    equation_solver_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
