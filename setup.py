from setuptools import find_packages, setup

setup(
    name='katas',
    packages=find_packages(),
    version='0.0.1',
    description='Code katas',
    license='BSD-3',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
