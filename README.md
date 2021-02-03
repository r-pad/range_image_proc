# range_image_proc
Utility functions for processing range images in python

## Instilation 

Set up conda environment (tested with python3.6)

```
sudo apt-get install build-essential cmake
conda install -c conda-forge eigen
conda install -c conda-forge pcl=1.9.1
conda install -c conda-forge xtensor xtensor-python pybind11
conda install faiss-gpu cudatoolkit=10.0 -c pytorch
conda install -c menpo opencv3
```

Compile the c++ library for python bindings in the conda virtual environment

```
mkdir build
cd build
cmake .. -DPYTHON_EXECUTABLE=/location/of/conda/env/bin/python3
#cmake .. -DPYTHON_EXECUTABLE=$(echo $(which python))
make
make install
```

In case of error, consider

```
ln -s /location/of/conda/env/python3.7/site-packages/numpy/core/include/numpy/ /usr/include/numpy
```

Install python package

```
pip install .
```