# Basic Tutorial Cython
ref: https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

build `helloworld.pyx`
```
python setup.py build_ext --inplace
```
`helloworld.c`, `helloworld.so`ができる．

```
python
>> import helloworld
Hello World
```