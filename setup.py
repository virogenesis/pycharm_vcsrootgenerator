import glob
from distutils.core import setup
from setuptools import find_packages


setup(
    name='pycharm_vcsrootgenerator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'lxml',
    ],
    license='MIT',
    scripts = glob.glob("Scripts/*.py"),
    long_description="VCS root generator"
)