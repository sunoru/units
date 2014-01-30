# -*- coding: utf-8 -*-
# filename:  sciNote/units/data.py
# by スノル

#
from .locals import *

_pc = 30835997962819660.8
LENGTH_DATA = {
    u'default': u'm', u'type': B_LENGTH,
    u'm': 1e0, u'km': 1e3, u'cm': 1e-1, u'mm': 1e-3,
    u'dam': 1e1, u'hm': 1e2, u'Mm': 1e6, u'Gm': 1e9,
    u'µm': 1e-6, u'nm': 1e-9, u'pm': 1e-12, u'fm': 1e-15,
    u'Tm': 1e12, u'Pm': 1e15, u'Em': 1e18, u'Zm': 1e21,
    u'Ym': 1e24, u'am': 1e-18, u'zm': 1e-21, u'ym': 1e-24,
    
    u'mi': 1609.344, u'ft': 0.3048, u'in': 0.0254,
    u'n mile': 1852., # nautical mile has no standard symbol
    u'a0': 0.5291772108e-10,
    u'Å': 1e-10, u'ly': 9460730472580800., u'ua': 149597870700.,
    u'pc': _pc, u'kpc': _pc*1e3, u'Mpc': _pc*1e6, u'Gpc': _pc*1e9,
}

MASS_DATA = {
    u'default': u'kg', u'type': B_MASS,
    u'kg': 1e0, u'g': 1e-3, u'mg': 1e-6,
    u'µg': 1e-9, u'ng': 1e-12, u'pg': 1e-15, u'fg': 1e-18,
    u'Mg': 1e3, u't': 1e3, u'Gg': 1e6,
    u'Tg': 1e9, u'Pg': 1e12, u'Eg': 1e15, u'Zg': 1e18,
    u'Yg': 1e21, u'ag': 1e-21, u'zg': 1e-24, u'yg': 1e-27,

    u'Da': 1.66053886e-27, u'u': 1.66053886e-27,
    u'me': 9.1093826e-31, 
}

TIME_DATA = {
    u'default': u's', u'type': B_TIME,
    u's': 1e0, u'ms': 1e-3, u'µs': 1e-6,
    u'ns': 1e-9, u'ps': 1e-12, u'fs': 1e-15,

    u'min': 60., u'hr': 3.6e3, u'd': 8.64e4,
    u'yr': 365.2425, # yr?
}

CURRENT_DATA = {
    u'default': u'A', u'type': B_CURRENT,
    u'A': 1e0, u'mA': 1e-3, u'µA': 1e-6,
}

TEMPERATURE_DATA = {
    u'default': u'K', u'type': B_TEMPERATURE,
    u'K': 1e0
    ##### QAQ
}

AMOUNT_DATA = {
    u'default': u'mol', u'type': B_AMOUNT,
    u'mol': 1e0, u'mmol': 1e-3
}

LUMINOUS_DATA = {
    u'default': u'cd', u'type': B_LUMINOUS,
    u'cd': 1e0
}

UNIT_DATA = {
    B_LENGTH: LENGTH_DATA, B_MASS: MASS_DATA, B_TIME: TIME_DATA, 
    B_CURRENT: CURRENT_DATA, B_TEMPERATURE: TEMPERATURE_DATA,
    B_AMOUNT: AMOUNT_DATA, B_LUMINOUS: LUMINOUS_DATA
}

DERIVED_UNIT = {
    7: (u'Hz', {2: -1}),
    8: (u'N', {0: 1, 1: 1, 2: -2}),
    9: (u'Pa', {0: -1, 1: 1, 2: -2}),
    10: (u'J', {0: 2, 1: 1, 2: -2}),
    11: (u'W', {0: 2, 1: 1, 2: -3}),
    12: (u'C', {2: 1, 3: 1}),
    13: (u'V', {0: 2, 1: 1, 2: -3, 3: -1}),
    14: (u'F', {0: -2, 1: -1, 2: 4, 3: 2}),
    15: (u'\u03a9', {0: 2, 1: 1, 2: -3, 3: -2}),
    16: (u'S', {0: -2, 1: -1, 2: 3, 3: 2}),
    17: (u'Wb', {0: 2, 1: 1, 2: -2, 3: -1}),
    18: (u'T', {1: 1, 2: -2, 3: -1}),
    19: (u'H', {0: 2, 1: 1, 2: -2, 3: -2}),
    20: (u'lm', {6: 1}),
    21: (u'lx', {0: -2, 6: 1}),
    22: (u'Bq', {2: -1}),
    23: (u'Gy', {0: 2, 2: -2}),
    24: (u'Sv', {0: 2, 2: -2}),
    25: (u'kat', {2: -1, 5: 1})
}

DERIVED_DATA = {
    u'atm': (101325.0, {0: -1, 1: 1, 2: -2}),
    u'eV': (1.602176565e-19, {0: 2, 1: 1, 2: -2})
}

UNIT_PREFIX = {
    u'': 1e0, u'k': 1e3, u'c': 1e-1, u'm': 1e-3,
    u'da': 1e1, u'h': 1e2, u'M': 1e6, u'G': 1e9,
    u'µ': 1e-6, u'n': 1e-9, u'p': 1e-12, u'f': 1e-15,
    u'T': 1e12, u'P': 1e15, u'E': 1e18, u'Z': 1e21,
    u'Y': 1e24, u'a': 1e-18, u'z': 1e-21, u'y': 1e-24,
}

