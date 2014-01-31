# -*- coding:utf-8 -*-
# filename: units/unit_error.py
# by スノル

class BaseError(Exception):
    _mes = 'Unknown Error.'
    def __init__(self):
        Exception.__init__(self, self._mes)

class IlligalUnit(BaseError):
    _mes = 'Illigal Unit!'

class UnmatchedUnits(BaseError):
    _mes = 'Unmatched Units!'

class ComplexError(BaseError):
    _mes = 'Complex Error!'

class ValueInitError(BaseError):
    _mes = 'Value Initializing Error!'
