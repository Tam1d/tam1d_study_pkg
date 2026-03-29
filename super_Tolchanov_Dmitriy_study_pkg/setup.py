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
        ],
    },
)
