#!/bin/sh

python codegen-numbers.py > src/fe-numbers.cpp
python codegen-names.py
