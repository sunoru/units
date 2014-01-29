# -*- coding:utf-8 -*-
# filename: sciNote/units/has_units.py
# by スノル

import traits.api as ta
from .locals import *
from .bases import Unit, ValueUnit
from .utils import genUnit

PRENAME = '_unit_'

class BaseHasUnit(TraitType):
    '''The base of all HasUnit classes.
    '''
    unit = ta.Undefined
    def __init__(self, unitname):
        TraitType.__init__(self)
        self.unit = genUnit(unitname)
        self.unit.normalize()

    def set_value_withunit(self, object, name, value):
        object.__dict__[PRENAME + name] = value

    def set_value_nounit(self, object, name, value):
        object.__dict__[PRENAME + name] =
            ValueUnit(value, self.value.unit)

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': ' + str(self.value) +\
            ' ' + self.unit.get_sig() + '>'

class HasUnit(BaseHasUnit):
    '''A normal base of HasUnit classes.
    '''
    def get(self, object, name):
        return object.__dict__.get(PRENAME + name, ta.Undefined)

    def set(self, object, name, value):
        if type(value) is tuple:
            self.set_value_withunit(object, name, value)
        else:
            self.set_value_nounit(object, name, value)

    def validate(self, object, name, value):
        if isinstance(value, list) or isinstance(value,tuple):
            t = genUnit(value[1])
            if self.unit != ta.Undefined and self.unit != t:
                self.error(object, name, value)
            return ValueUnit(value[0], t)
        return ta.Float.validate(self, object, name, value)
