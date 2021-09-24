from distutils.core import setup
import setuptools
setup(
  name = 'py-strict-typing',
  packages = ['strict_typing'],
  version = '0.1.0',
  license='MIT',
  description = 'A library for enforcing strict typing of class members and function parameters in Python.',
  author = 'whdev1',
  author_email = 'whdev1@protonmail.com',
  url = 'https://github.com/whdev1/py-strict-typing',
  download_url = 'https://github.com/whdev1/py-strict-typing/archive/refs/tags/v0.1.0.tar.gz',
  keywords = ['Strict', 'Typing', 'Type-checking', 'Decorator', 'py-strict-typing'],
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