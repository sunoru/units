# -*- coding:utf-8 -*-
# filename: sciNote/units/si_base_units.py
# by スノル

from .bases import (ta, HasUnit, Undefined)
import .units_lengthSI as lengthSI
import .units_length as lengthAll
class BaseLength(HasUnit):
    '''The base class of length'''
    _default_unit = lengthSI.Meter
    _unit_list = lengthSI.__all__
    unit = _default_unit

class Length(BaseLength):
    _unit_list = lengthAll.__all__
