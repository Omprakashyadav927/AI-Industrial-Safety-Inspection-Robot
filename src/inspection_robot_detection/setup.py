from setuptools import find_packages, setup

package_name = 'inspection_robot_detection'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    maintainer='Prince Jaiswal',
    maintainer_email='princejaiswal16796@gmail.com',
    description='YOLOv8 object detection package for AI Industrial Safety Inspection Robot.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolov8_detection_node = inspection_robot_detection.yolov8_detection_node:main',
        ],
    },
)
