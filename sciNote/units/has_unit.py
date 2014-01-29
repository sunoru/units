# -*- coding:utf-8 -*-
# filename: sciNote/units/has_unit.py
# by スノル

import traits.api as ta
from .locals import *
from .bases import Unit, genUnit
from .value_type import ValueUnit, genValue

PRENAME = '_unit_'

class BaseHasUnit(ta.TraitType):
    '''The base of all HasUnit classes.
    '''
    info_text = 'has unit'

    def __init__(self, unit=None):
        ta.TraitType.__init__(self)
        self.unit = genUnit(unit)
        if self.unit is not None:
            self.unit = self.unit.normalize()[0]

    def create_editor(self):
        pass

class HasUnit(BaseHasUnit):
    '''A normal base of HasUnit classes.
    '''
    def get_default(self):
        return ValueUnit(unit = self.unit)

    def get(self, object, name):
        if not object.__dict__.has_key(PRENAME + name):
            self.set(object, name, self.get_default())
        return object.__dict__[PRENAME + name]

    def set(self, object, name, value):
        object.__dict__[PRENAME + name] = value

    def validate(self, object, name, value):
        if isinstance(value, ValueUnit) and value.isreal():
            return value

        if isinstance(value, basestring):
            t = genValue(value)
            if self.imag != 0 or self.unit is not None and self.unit != t:
                self.error(object, name, value)
            return t

        if (isinstance(value, list) or isinstance(value, tuple)) and value[0].imag == 0:
            t = genUnit(value[1])
            if self.unit is not None and self.unit != t:
                self.error(object, name, value)
            return ValueUnit(value[0], t)

        if isinstance(value, float) or isinstance(value, int):
            rtmp = ValueUnit(value, self.unit)
            return rtmp

        self.error(object, name, value)

class HasUnitComplex(HasUnit):
    def validate(self, object, name, value):
        if isinstance(value, complex) or isinstance(value, float) or isinstance(value, int):
            return ValueUnit(value, self.unit)

        if isinstance(value, ValueUnit):
            return value

        if isinstance(value, basestring):
            t = genValue(value)
            if self.unit is not None and self.unit != t:
                self.error(object, name, value)
            return t

        if (isinstance(value, list) or isinstance(value, tuple)):
            t = genUnit(value[1])
            if self.unit is not None and self.unit != t:
                self.error(object, name, value)
            return ValueUnit(value[0], t)

        self.error(object, name, value)

