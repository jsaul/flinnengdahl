#!/bin/sh -e

SWIG="swig -python -c++"

cd src

for module in flinnengdahl
do
	cd $module

	$SWIG -I. -o ${module}_wrap.cpp ${module}.i
	mv ${module}.py __init__.py

	cd ..
done
