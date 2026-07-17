from setuptools import find_packages, setup

package_name = 'modena_common'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matheus Lino',
    maintainer_email='matheus.vlino@gmail.com',
    description='Common Python utilities shared across Modena ROS 2 packages',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
        ],
    },
)
