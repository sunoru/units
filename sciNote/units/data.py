# -*- coding:utf-8 -*-
# filename: sciNote/units/data.py
# by スノル

LENGTH_DATA = {
    u'default':u'm',
    u'm':1e0, u'km':1e3, u'cm':1e-1, u'mm':1e-3,
    u'µm':1e-6, u'nm':1e-9, u'pm':1e-12, u'fm':1e-15,
    u'Å',
}

MASS_DATA = {
    u'default':u'kg',
    u'kg':1e0,
}

TIME_DATA = {
    u'default':u's',
    u's':1e0,
}

CURRENT_DATA = {
    u'default':u'A',
    u'A':1e0,
}

TEMPERATURE_DATA = {
    u'default':u'K',
    u'K':1e0,
    ##### QAQ
}

AMOUNT_DATA = {
    u'default':u'mol',
    u'mol':1e0,
}

LUMINOUS = {
    u'default':u'cd',
    u'cd':1e0,
}

UNIT_DATA = {LENGTH:LENGTH_DATA, MASS:MASS_DATA, TIME = TIME_DATA, 
    CURRENT = CURRENT_DATA, TEMPERATURE = TEMPERATURE_DATA,
    AMOUNT = AMOUNT_DATA, LUMINOUS = LUMINOUS
}
