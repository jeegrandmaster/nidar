from setuptools import find_packages, setup

package_name = 'drone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/rsp.launch.py',
            'launch/launch_sim.launch.py',
        ]),
        ('share/' + package_name + '/description', [
            'drone/description/drone.urdf.xacro',
            'drone/description/drone_core.xacro',
            'drone/description/gazebo.xacro',
        ]),
        ('share/' + package_name + '/rviz', [
            'rviz/drone.rviz',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='onlydrones',
    maintainer_email='onlydrones@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
