# Libabigail Python

This is a small repository to test creating python bindings for [Libabigail](https://sourceware.org/git/?p=libabigail.git;a=tree).
It includes the following sections:

 - [bindings](bindings): early testing of ctypes (and other) to create bindings
 - [wrapper](wrapper): a more "expected" wrapper to just parse the abidw command output into json
 - [abispack-lib](abispack-lib): A C++ library that we would want to use libabigial, and expose some subset of functions to spack (so there would be Python bindings)
 - [abicompat](abicompat): an attempt to write out what the [abicomat](https://github.com/woodard/libabigail/blob/master/tools/abicompat.cc) script is doing.
 - [abi-python](abi-python): after reading about abicompat, I want to try walking through these steps to see how hard it would be to do in Python natively.
 - [libabi-ml](libabi-ml): Starting to think about if it makes sense to restructure the json to provide some subset of features.
 - [clingo](clingo): learning a bit of using clingo with the goal of being able to eventually assess ABI compatability using a logic program.
