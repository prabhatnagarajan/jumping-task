from setuptools import find_packages
from setuptools import setup

install_requires = [
    'numpy',
    'gymnasium',
    'matplotlib',
    'pygame',
    'ipython',
    ]

test_requires = [
    'pytest',
    'attrs<19.2.0',  # pytest does not run with attrs==19.2.0 (https://github.com/pytest-dev/pytest/issues/3280)  # NOQA
]

setup(
    name='jumping-task',
    version='0.1',
    description='Jumping Task Gymnasium',
    keywords='Jumping Task, Deep RL',
    author='Prabhat Nagarajan',
    author_email='nagarajan@ualberta.ca',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires
)
