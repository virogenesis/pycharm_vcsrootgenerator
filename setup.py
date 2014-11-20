import glob
from distutils.core import setup

setup(
    name='pycharm_vcsrootgenerator',
    version='0.1',
    packages=[],
    install_requires=[
        'lxml',
    ],
    license='MIT',
    scripts = glob.glob("Scripts/*.py"),
    long_description="VCS root generator"
)