# -*- coding:utf-8 -*-
# filename: sciNote/units/unit_error.py
# by スノル

class BaseError(Exception):
    _mes = 'Unknown Error.'
    def __init__(self):
        Exception.__init__(self, self._mes)

class IlligalUnit(BaseError):
    _mes = 'Illigal Unit!'

class UnmatchedUnits(BaseError):
    _mes = 'Unmatched Units!'

class ComplexOrderE(BaseError):
    _mes = 'No ordering relation is defined for complex numbers'
