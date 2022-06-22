from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        ['primes.pyx',                   # Cython code file with primes() function
         'primes_python_compiled.py'],  # Python code file with primes() function
        annotate=True),                 # enables generation of the html annotation file
)
