# sciNote

**Use Python for scientific calculation.**
https://github.com/sunoru/sciNote

Author: スノル <s@sunoru.com>

## Introduction

This library privides some useful modules for scientific calculation. It works with Python versions from 2.5 to 2.7.

* units: use value type with SI units.

## Building

from source:

Install the dependencies:

- [traits](https://github.com/enthought/traits)

You can alternatively use `apt-get` to install them:
```
$ apt-get install python-traits
```
Download the latest `sciNote` library from: https://www.sunoru.com/code/sciNote/

Extract the source distribution and run:
```
$ python setup.py build
$ python setup.py install
```

## Getting the code

The code is hosted at [Github](https://github.com/sunoru/sciNote)

```
$ git clone git://github.com/sunoru/sciNote.git
$ cd sciNote
```

## Using

At present the library only provides a module for `units`.

*API:*

Use sciNote.units.api.V to generate values with units.
```
>>> from sciNote.units.api import V
>>> a = V('5m/s^2')
>>> t = V('2.5s')
>>> s = 0.5 * a * t ** 2
>>> print s
15.625 m
>>> print s ** 2
244.140625 m^2
```

Use the HasUnit or HasUnitComplex to act as a trait that has units. (See the [traits](https://github.com/enthought/traits).)

```
>>> from sciNote.units.api import HasUnit
>>> from traits.api import HasTraits
>>> from math import pi
>>> class Cone(HasTraits):
        radius = HasUnit
        height = HasUnit('m') # use a symbol to force the trait to have a length unit.
        def get_volume(self):
            return 1. / 3 * pi * self.radius * self.radius * self.height
        def get_surface_area(self):
            return pi * self.radius * (self.radius **2 + self.height **2)**0.5
        # note that you have to use x**0.5 to fit the ValueUnit type.
>>> cone = Cone(radius=V('4m'), height=3)
>>> cone.get_volume()
50.2654824574 m^3
>>> cone.get_surface_area()
62.8318530718 m^2
```
    
