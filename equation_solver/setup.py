from setuptools import find_packages, setup

package_name = 'equation_solver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nathan Shankar',
    maintainer_email='nathanshankar465@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'equation_solver_server = equation_solver.equation_solver_server:main',
        'equation_solver_client = equation_solver.equation_solver_client:main',
        ],
    },
)
