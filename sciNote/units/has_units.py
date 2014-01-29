# -*- coding:utf-8 -*-
# filename: sciNote/units/has_units.py
# by スノル

import traits.api as ta
from .locals import *
from .bases import Unit, ValueUnit

PRENAME = '_unit_'

class BaseHasUnit(TraitType):
    '''The base of all HasUnit classes.
    '''
    def set_value_withunit(self, object, name, value):
        object.__dict__[PRENAME + name] = 
            ValueUnit(value[0], Unit.genUnit(value[1]))

    def set_value_nounit(self, object, name, value):
        object.__dict__[PRENAME + name] =
            ValueUnit(value, self.value.unit)

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': ' + str(self.value) +\
            ' ' + self.unit.get_sig() + '>'

class HasUnit(BaseHasUnit):
    '''A normal base of HasUnit classes.
    '''
    _set_value = {tuple: BaseHasUnit.set_value_withunit,
        list: BaseHasUnit.set_value_nounit}

    def get(self, object, name):
        return object.__dict__.get(PRENAME + name, ta.Undefined)

    def set(self, object, name, value):
        if type(value) is tuple:
            self.set_value_withunit(object, name, value)
        else:
            self.set_value_nounit(object, name, value)

    def validate(self, object, name, value):
        if isinstance(value, list):
            return tuple(value)
        if isinstance(value, tuple):
            return value
        return ta.Float.validate(self, object, name, value)
