from distutils.core import setup
import setuptools
setup(
  name = 'py-strong-typing',
  packages = ['strong_typing'],
  version = '0.1.0',
  license='MIT',
  description = 'A library for enforcing strong typing of class members and function parameters in Python.',
  author = 'whdev1',
  author_email = 'whdev1@protonmail.com',
  url = 'https://github.com/whdev1/py-strong-typing',
  download_url = 'https://github.com/whdev1/py-strong-typing/archive/refs/tags/v0.1.0.tar.gz',
  keywords = ['Strong', 'Typing', 'Type-checking', 'Decorator', 'py-strong-typing'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)