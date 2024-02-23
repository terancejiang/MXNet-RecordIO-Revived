# MXNet-RecordIO-Standalone
A standalone maintenance and enhancement project for the RecordIO serialization function, 
originally part of the now-retired MXNet framework.

When I try to install MXNET on newer version of Python or with newer packages such as numpy, 
I got all kinds of dependency issues. Therefore, I created this repo to extract recordio function, keep it up to date.

NOTE: This project incorporates the original library files(.so/.dll) from original MXnet project

## Introduction
MXNet-RecordIO-Revived is an open-source project focused on maintaining and enhancing the RecordIO function, 
a powerful data serialization tool originally developed as part of Apache MXNet. 
With MXNet no longer being updated, this project aims to keep RecordIO alive and evolving, 
serving the community that relies on its efficient data handling capabilities.

## Background
RecordIO facilitates efficient reading and writing of data in a serialized format, 
making it particularly useful for training deep learning models with large datasets. 
Its design allows for easy data manipulation and access, 
supporting the development of high-performance machine learning applications.

## Features
- all original mxnet recordio functionalities 

## Todos

Need to pack the libmxnet.dll(Windows). 
- [ ] MacOS support
- [ ] Windows support 
- [x] Linux support

## Getting Started
### Installation
```bash
pip install mx-recordio
```
#### Ubuntu

#### Step1:
Move the original MXnet library files to this repo's folder
```bash
cd /path/to/this/repo

cp $CONDA_HOME/envs/{your_env_name}/lib/python3.6/site-packages/mxnet/libmxnet.so  ./mx_recordio/lib/libmxnet.so

```

#### Step2:

The original MXnet is build on earlier version of Ubuntu, therefore its rely on **libgfortran.so.3**.

But libgfortran3 is no longer supported after Ubuntu 20.04. It depends on an older version of gcc which is no longer maintained in this version of the distribution.

For Ubuntu after 20.04, follows:
``` bash
# for ubuntu greater than 20.04
sudo apt-get install libgfortran5

# create a soft link to libgfortran.so.3
sudo ln -s /usr/lib/x86_64-linux-gnu/libgfortran.so.5 /usr/lib/x86_64-linux-gnu/libgfortran.so.3 

```

Do the same thing if you encounter the following error:
```bash
OSError: libgfortran.so.3: cannot open shared object file: No such file or directory
```

#### Windows
TODO

### usage 
More detailed usage please refer to original mxnet recordio documentations: https://mxnet.apache.org/versions/1.7/api/python/docs/api/mxnet/recordio/index.html

```python
# the original mxnet import 
import mxnet as mx

# change above import to this repo, and you good to go
import mx_recordio as mx

# usage same as the original mxnet recordio usage
record = mx.recordio.MXIndexedRecordIO('tmp.idx', 'tmp.rec', 'w')

for i, item in enumerate(some_data):
    record.write_idx(i, item)
record.close()

```
