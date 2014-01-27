# -*- coding:utf-8 -*-
# filename: sciNote/units/si_base_units.py
# by スノル

from .bases import (ta, HasUnit, Undefined)

from .units_all import units_lengthSI as SIUnitLength
from .units_all import units_length as UnitLength

class BaseLength(HasUnit):
    '''The base class of length'''
    _default_unit = SIUnitLength.Meter
    _unit_list = SIUnitLength.__all__
    unit = _default_unit

class Length(BaseLength):
    _unit_list = UnitLength.__all__
