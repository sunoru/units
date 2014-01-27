# -*- coding:utf-8 -*-
# filename: sciNote/units/bases.py
# by スノル

import traits.api as ta

PreName = 'the_unit_'

class BaseUnit():
    pass
class Unit(BaseUnit):
    _ratio=1e0
    @classmethod
    def get_ratio(cls):
        return cls._ratio
class Any(Unit):
    pass

class BaseHasUnit(ta.Float):
    '''The base of all HasUnit classes.
    '''
    _default_unit = Any
    _unit_list = [Any]
    unit = _default_unit

    def set_value_withunit(self, object, name, value):
        myunit = self._unit_list.get(value[1], ta.Undefined)
        if myunit is ta.Undefined:
            self.error(object, name, value)
        tmpv = self.convert(value[0], value[1], self._default_unit)
        self.unit = myunit

    def set_value_nounit(self, object, name, value):
        object.__dict__[PreName + name] = value

    def convert(self, value, unit_before, unit_after):
        if unit_before == unit_after:
            return value
        return value * unit_after.get_ratio() / unit_before.get_ratio()

    def get_value(self, object, name, unitName):
        tmpv = object.__dict__.get(PreName + name, ta.Undefined)
        if unitName is not self.unit:
            tmpv = self.convert(tmpv, self.unit, unitName)
        return tmpv

    def get_default_unit(self):
        return self._default_unit

    def get_unit_list(self):
        return self._unit_list

class HasUnit(BaseHasUnit):
    '''A normal base of HasUnit classes.
    '''
    _set_value = {tuple: BaseHasUnit.set_value_withunit,
        list: BaseHasUnit.set_value_withunit}

    def get(self, object, name):
        return self.get_value(object, name, self.unit)

    def set(self, object, name, value):
        self.set_value.get(type(value),
            BaseHasUnit.set_value_nounit)\
            (self, object, name, value)

