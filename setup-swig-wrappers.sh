#!/bin/sh -e

INCLUDE=$(pwd)/src
SWIG="swig -python -py3 -c++"

cd src

for item in flinnengdahl
do
	module="$item"
	$SWIG -I$INCLUDE -o ${module}_wrap.cpp ${module}.i
	mv ${module}.py ..
done
