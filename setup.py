from setuptools import setup

package_name = 'python_gui_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
<<<<<<< HEAD
    description='0',
=======
    description='A package for publishing goal poses from a GUI',
>>>>>>> origin/main
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'goal_publisher = python_gui_pkg.goal_publisher:main',
        ],
    },
)