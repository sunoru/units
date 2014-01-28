# -*- coding:utf-8 -*-
# filename: sciNote/units/data.py
# by スノル

from .locals import *

LENGTH_DATA = {
    u'default':u'm', u'type':B_LENGTH,
    u'm':1e0, u'km':1e3, u'cm':1e-1, u'mm':1e-3,
    u'µm':1e-6, u'nm':1e-9, u'pm':1e-12, u'fm':1e-15,
    u'Å':1e-10,
}

MASS_DATA = {
    u'default':u'kg', u'type':B_MASS,
    u'kg':1e0,
}

TIME_DATA = {
    u'default':u's', u'type':B_TIME,
    u's':1e0,
}

CURRENT_DATA = {
    u'default':u'A', u'type':B_CURRENT,
    u'A':1e0
}

TEMPERATURE_DATA = {
    u'default':u'K', u'type':B_TEMPERATURE,
    u'K':1e0
    ##### QAQ
}

AMOUNT_DATA = {
    u'default':u'mol', u'type':B_AMOUNT,
    u'mol':1e0
}

LUMINOUS_DATA = {
    u'default':u'cd', u'type':B_LUMINOUS,
    u'cd':1e0
}

UNIT_DATA = {
    B_LENGTH:LENGTH_DATA, B_MASS:MASS_DATA, B_TIME:TIME_DATA, 
    B_CURRENT:CURRENT_DATA, B_TEMPERATURE:TEMPERATURE_DATA,
    B_AMOUNT:AMOUNT_DATA, B_LUMINOUS:LUMINOUS_DATA
}
