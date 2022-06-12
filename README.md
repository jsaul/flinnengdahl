# flinnengdahl.py

Lightweight, fast and configurable Python/C++ module to compute
Flinn-Engdahl region numbers and names.

## Author

Joachim Saul, GFZ Potsdam

## Motivation

The goal is to have consistent and up-to-date region naming while
preserving the original region numbering scheme. We added the
ability to use arbitrary translations. An example translation table
is included. English region names are hardcoded as default and the C++ code
defining the hardcoded names can easily be (re)generated from the
translation table whenever needed.

The codes are set up in a way that in theory allows defining new cells,
provided they fit in the 1x1-degree cells. But remember that such
modifications are then deviations from the "standard" Flinn-Engdahl
region numbering and should not be called "Flinn-Engdahl regions" any more.

## Python

Simple Python wrappers are automatically generated using SWIG.

## Examples

```
>>> import flinnengdahl
>>> fe=flinnengdahl.FlinnEngdahl()
>>> fe.name(50,10)
'Germany'
>>> fe.number(50,10)
543
>>> fe.read("numbered-names-intl.txt")
>>> fe.name(50,10,"de")
'Deutschland'
>>> fe.name(50,10,"es")
'Alemania'
>>> fe.name(50,10,"en")
'Germany'
>>> fe.name(50,10,"")
'Germany'
>>> fe.setCategory("de")
>>> fe.name(50,10)
'Deutschland'
```

You get the picture.
