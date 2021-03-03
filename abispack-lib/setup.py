# setup.py
# This file is generated by Shroud 0.12.2. Do not edit.
from setuptools import setup, Extension
import numpy

module = Extension(
    'abispack',
    sources=[
         'abispack/pyabispack_Libabigailtype.cpp',
         'abispack/pyabispack_abispackmodule.cpp',
         'abispack/pyabispackmodule.cpp',
         'abispack/pyabispackutil.cpp',
         'abispack.cpp'
    ],
    language='c++',
    include_dirs = ['/usr/local/include/libabigail', '/usr/include/libxml2', numpy.get_include()],
    libraries = ['abigail'],
    library_dirs = ['/usr/local/lib', '/usr/local/lib/libabigail'], 
    extra_compile_args = [ '-g' ],
#    extra_link_args =
)

setup(
    name='abispack',
    ext_modules = [module],
)
