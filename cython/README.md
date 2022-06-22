# Cython
https://cython.readthedocs.io/en/latest/index.html
## Basic Tutorial
ref: https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

cythonコードの記述方法は大きく分けて2種類
- `.py`: `cython`をimportして変数アノテーションを使って記述．
- `.pyx`: `cdef`を用いてC言語風に記述．

build `helloworld.pyx`
```
$python setup.py build_ext --inplace
```
`helloworld.c`, `helloworld.so`ができる．

```
$python
>> import helloworld
Hello World
```

### Fibonacci

### Primes
- `primes_pure`
    - `primes.py`: cython code by using pure python
    - `primes_python.py`: python code which return the same result with `primes.py`
    - `primes_python_complied.py`: Copy of `primes_python.py` which is used to compile by cython
    - `setup.py`: `primes.py`と`primes_python_complied.py`をコンパイルし，
    - `*.c`: コンパイルされたcコード
    - `*.html`: cにコンパイル箇所とcコードが確認できる．
- `primes_cython`
    - `primes_pure`と同様．`.pyx`で書いている．

cythonコード(`primes.py`)とpythonコード(`primes_python_complied.py`)をコンパイル
```
$python setup.py build_ext --inplace
```

primesが一番速い．
```
$python -m timeit -s 'from primes_python import primes' 'primes(1000)'
10 loops, best of 5: 22 msec per loop

$ python -m timeit -s 'from primes_python_compiled import primes' 'primes(1000)'
20 loops, best of 5: 10.3 msec per loop

$ python -m timeit -s 'from primes import primes' 'primes(1000)'
200 loops, best of 5: 1.37 msec per loop
```

## IPython
ref: https://cython.readthedocs.io/en/latest/src/quickstart/build.html

`notebooks/cython_helloworld.ipynb`