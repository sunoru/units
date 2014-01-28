# -*- coding:utf-8 -*-
# filename: sciNote/units/units_all/units_lengthSI.py
# by スノル
from .unit_types import *

__all__ = ('ALIAS', 'UNITS', 'Meter', 'Kilometer', 'Centimeter',
    'Millimeter', 'Micrometer', 'Nanometer', 'Picometer', 'Femtometer')
ALIAS = {}

class Length(HasUnit):
    pass
class Meter(Unit):
    symbol = 'm'
    unittype = LENGTH

class Kilometer(UnitKilo, Meter):
    symbol = UnitKilo.symbol + Meter.symbol

class Centimeter(UnitCenti, Meter):
    symbol = UnitCenti.symbol + Meter.symbol

class Millimeter(UnitMilli, Meter):
    symbol = UnitMilli.symbol + Meter.symbol

class Micrometer(UnitMicro, Meter):
    symbol = UnitMicro.symbol + Meter.symbol

class Nanometer(UnitNano, Meter):
    symbol = UnitNano.symbol + Meter.symbol

class Picometer(UnitPico, Meter):
    symbol = UnitPico.symbol + Meter.symbol

class Femtometer(UnitFemto, Meter):
    symbol = UnitFemto.symbol + Meter.symbol

UNITS = (Meter, Kilometer, Centimeter, Millimeter,
    Micrometer, Nanometer, Picometer, Femtometer)
for each in UNITS:
    ALIAS[each.symbol] = each

