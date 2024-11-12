from setuptools import setup

setup(
    name='my_project',
    version='1.0',
    packages=['my_project'],
    install_requires=[
        'pytest',
    ],
    tests_require=[
        'pytest',
    ],
    test_suite='tests',
)