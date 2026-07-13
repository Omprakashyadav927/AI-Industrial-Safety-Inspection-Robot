from setuptools import setup
import os
from glob import glob

package_name = 'inspection_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Omprakash Yadav',
    maintainer_email='omprakashyadav5592@gmail.com',
    description='AI-Powered Industrial Safety Inspection Robot (Demo Version)',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'inspection_node = inspection_robot.inspection_node:main',
        ],
    },
)
