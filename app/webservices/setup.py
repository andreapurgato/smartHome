#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

from setuptools import setup

# setup function for python smart home app
setup(
    name='smarthome_project',
    version='0.1.0',
    packages=['python'],
    entry_points={
        'console_scripts': [
            'smarthome_project = python.__main__:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)