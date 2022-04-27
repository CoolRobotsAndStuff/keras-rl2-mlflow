from setuptools import setup
from setuptools import find_packages


setup(name='keras-rl2-mlflow',
      version='1.0.5',
      description='Deep Reinforcement Learning for Tensorflow 2 Keras',
      author='Taylor McNally',
      url='https://github.com/CoolRobotsAndStuff/keras-rl2-mlflow',
      license='MIT',
      install_requires=['tensorflow'],
      extras_require={
          'gym': ['gym'],
      },
      packages=find_packages())
