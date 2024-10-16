# flinnengdahl.py

Standalone, lightweight, fast and configurable Python/C++ module to compute
Flinn-Engdahl region numbers and names.

## Author

Joachim Saul, GFZ Potsdam

## Motivation

The goal is to have consistent and up-to-date region *naming* while
preserving the original region *numbering* scheme. Names may change and some
of the names in the original Flinn-Engdahl region naming are at least debatable.
The goal here is to follow Wikipedia as closely as possible. We added the
ability to use arbitrary translations. An example translation table
is included for English, German and Spanish. The English region names are
hardcoded as default and the C++ code defining the hardcoded names can easily
be (re)generated from the translation table whenever needed.

The translation table is provided as a *single file*, as it was found to be convenient
to have translations to several languages on consecutive lines for comparison, with
comments added where needed to support a certain naming (e.g. "Revillagigedo" or
"Haida Gwaii").

The codes are set up in a way that in theory allows defining new cells,
provided they fit in the 1x1-degree raster. But please note that such
modifications would be deviations from the "standard" Flinn-Engdahl
region numbering and should not be called "Flinn-Engdahl regions" any more.

## Python

Simple Python wrappers are automatically generated using SWIG.

Note that there are other Python modules available to compute Flinn-Engdahl regions,
e.g. in [SeisComP](https://github.com/SeisComP) and [ObsPy](https://github.com/obspy).
There is no reason not to use those, except in situations where the installation of
a large software package is not feasible or if the translation feature is of interest.

## Examples

```
>>> import flinnengdahl
>>> fe=flinnengdahl.FlinnEngdahl()
>>> fe.name(50, 10)
'Germany'
>>> fe.number(50, 10)
543
>>> fe.read("numbered-names-intl.txt")
>>> fe.name(50, 10, "de")
'Deutschland'
>>> fe.name(50, 10, "es")
'Alemania'
>>> fe.name(50, 10, "en")
'Germany'
>>> fe.name(50, 10, "")
'Germany'
>>> fe.setCategory("de")
>>> fe.name(50, 10)
'Deutschland'
```

You get the picture.


## Issues

There are still some names that may create confusion or discomfort, like
"Kashmir-India border region".  Ideas on how to resolve this (and at the same
time keep the region numbering!) are welcome but probably outside the scope of
this module.


## Reference

J.B. Young, B.W. Presgrave, H. Aichele, D.A. Wiens, E.A. Flinn (1996),
The Flinn-Engdahl Regionalisation Scheme: The 1995 revision.
Physics of the Earth and Planetary Interiors, 96, pp 223-297.
https://doi.org/10.1016/0031-9201(96)03141-X
