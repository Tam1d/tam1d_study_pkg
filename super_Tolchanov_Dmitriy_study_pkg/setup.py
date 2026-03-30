import os
from setuptools import setup

package_name = 'super_Tolchanov_Dmitriy_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, package_name + '.scripts'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/my_first_launch.py']),
        (os.path.join('share', package_name, 'launch'), ['launch/robot_system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tam1d',
    maintainer_email='tamid777@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'time_printer = super_Tolchanov_Dmitriy_study_pkg.scripts.time_printer:main',
            'even_number_publisher = super_Tolchanov_Dmitriy_study_pkg.scripts.even_number_publisher:main',
            'overflow_listener = super_Tolchanov_Dmitriy_study_pkg.scripts.overflow_listener:main',
            'static_tf_broadcaster = super_Tolchanov_Dmitriy_study_pkg.scripts.static_tf_broadcaster:main',
            'carrot_broadcaster = super_Tolchanov_Dmitriy_study_pkg.scripts.turtle_carrot_tf_broadcaster:main',
            'turtle_broadcaster = super_Tolchanov_Dmitriy_study_pkg.scripts.turtle_tf_broadcaster:main',
        ],
    },
)
