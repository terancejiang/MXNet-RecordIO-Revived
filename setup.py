"""
Project Name: MXNet-RecordIO-Standalone
File Created: 2024/2/23 上午9:46
Author: Ying.Jiang
File Name: setup.py
"""
import platform
from setuptools import setup

package_data = {}
if platform.system() == 'Linux':
    package_data['mx_recordio'] = ['mx_recordio/lib/libmxnet.so']


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mx_recordio',
    version='0.2',
    packages=package_data,
    install_requires=requirements,
)

entry_points = {
    'console_scripts': [
        'my_command=package_name.module:function',
    ],
},

author = 'JY',
author_email = 'yingjiang.jy@gmail.com',
url = 'https://github.com/terancejiang/MXNet-RecordIO-Standalone'
description = 'standalone version of mxnet-recordio functions, without mxnet dependency',

long_description = open('README.md').read(),
long_description_content_type = 'text/markdown',

license = 'MIT',
classifiers = [
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
],
