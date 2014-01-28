# -*- coding:utf-8 -*-
# filename: sciNote/units/bases.py
# by スノル

import traits.api as ta
from .data import *
from .locals import *

PRENAME = '_unit_'
class BaseUnit():
    ratio=1e0
class Unit(BaseUnit):
    def __init__(self, ratio=1e0, unittype=None):
        self.ratio = ratio
        if unittype is None:
            self.unittype = (0,)*7
        else:
            self.unittype = unittype

NOW_UNITS = {}
def newUnit(unit):
    NOW_UNITS[unit.unittype+(ratio,)] = unit

def askUnit(unittype):
    if NOW_UNITS.has_key(unittype):
        return NOW_UNITS[unittype)
    return None

class Any(Unit):
    def __init__(self):
        Unit.__init__(self)
newUnit(Any())

class Meter(Unit):
    def 

class ValueUnit(float):
    def __init__(self, value, unit):
        float.__init__(self, value)
        self.unit = unit
        
    @staticmethod
    def convert(value, unit_before, unit_after):
        if unit_before is unit_after:
            return value
        return value * unit_after.ratio() / unit_before.ratio()

    def __abs__(self):
        return ValueUnit(float.__abs__(self), self.unit)
        
    def __add__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')
        self
        return ValueUnit(float.__add__(self, other), self.unit)
        
    def __div__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')
        return ValueUnit(float.__div__(self, other))
        
    def __divmod__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')

        return ValueUnit(float.__add__(self, other))

