# -*- coding:utf-8 -*-
# filename: sciNote/units/units_lengthSI.py
# by スノル
from .bases import Unit

__all__=(Meter, Kilometer, )
class Meter(Unit):
    _ratio = 1.0
m=Meter

class Kilometer(Unit):
    _ratio = 1e3
km=Kilometer
