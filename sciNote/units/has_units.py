# -*- coding:utf-8 -*-
# filename: sciNote/units/has_units.py
# by スノル

import traits.api as ta
from .locals import *

PRENAME = '_unit_'

class BaseHasUnit(TraitType):
    '''The base of all HasUnit classes.
    '''
    _default_unit = Any
    _unit_set = {Any}
    unit = _default_unit
    value = 0.0

    def set_value_withunit(self, object, name, value):
        if value[1] not in self._unit_set:
            self.error(object, name, value)
        self.unit = value[1]
        self.value = value[0]

    def set_value_nounit(self, object, name, value):
        self.value = value

    def get_value(self, object, name, unitName):
        tmpv = self.value
        if unitName is not self.unit:
            tmpv = self.convert(tmpv, self.unit, unitName)
        return tmpv

    def get_default_unit(self):
        return self._default_unit

    def get_unit_set(self):
        return self._unit_set

    def __repr__(self):
        return '<' + self.__class__.__name__ + ': ' + str(self.value) +\
            ' ' + self.unit.get_sig() + '>'

class HasUnit(BaseHasUnit):
    '''A normal base of HasUnit classes.
    '''
    _set_value = {tuple: BaseHasUnit.set_value_withunit,
        list: BaseHasUnit.set_value_withunit}

    def get(self, object, name):
        return self.get_value(object, name, self.unit)

    def set(self, object, name, value):
        self._set_value.get(type(value),
            BaseHasUnit.set_value_nounit)\
            (self, object, name, value)

    def validate(self, object, name, value):
        return value
