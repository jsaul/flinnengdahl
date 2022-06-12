flinnengdahl.py
===============

This is a lightweight and fast Python/C++ module to generate
Flinn-Engdahl region numbers and names for any latitude, longitude
pair.

The goal is to have consistent and up-to-date region naming while
preserving the original region numbering scheme. We added the
ability to add arbitrary translations. An example translation table
is included. By default, hardcoded names are used. The C++ code
defining the hardcoded names can easily be (re)generated from the
translation table whenever needed.

The codes are set up in a way that allows defining new cells,
provided they fit in the 1x1-degree cells. But remember that such
modifications are then deviations from the "standard" Flinn-Engdahl
region numbering.

Python wrappers are automatically generated using SWIG.
