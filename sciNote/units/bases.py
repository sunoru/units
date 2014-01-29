# -*- coding:utf-8 -*-
# filename: sciNote/units/bases.py
# by スノル

from .data import *
from .unit_error import (IlligalUnit, UnmatchedUnits)
from .locals import *

class BaseUnit():
    def __init__(self, data):
        if data is None:
            self.data = {}
        else:
            self.data = data.copy()

class Unit(BaseUnit):
    '''Unit class.
    '''
    @staticmethod
    def findUnit(ccflg, tmstr, punit, censu, annit):
        ttflg = False
        for e1 in UNIT_DATA.values():
            for e2 in e1.keys():
                if e2 == tmstr:
                    ttflg = True
                    annit[e1['type']] = e2
                    if ccflg:
                        punit[e1['type']] += censu
                    else:
                        punit[e1['type']] -= censu
                    break
            if ttflg:
                break
        return ttflg

    @staticmethod
    def analysis(name):
        mystr = name.replace(' ', '')
        tmstr = ''
        ccflg = True
        censu = 1
        punit = [0] * 7
        annit = [''] * 7
        miflg = False
        for i in xrange(0, len(mystr)):
            if mystr[i] == '^':
                miflg = True
                mistr = tmstr
                tmstr = ''
            elif mystr[i] == '*':
                if miflg:
                    censu = int(tmstr)
                    tmstr = mistr
                if not Unit.findUnit(ccflg, tmstr, punit, censu, annit):
                    raise IlligalUnit()
                tmstr = ''
                ccflg = True
                censu = 1
                miflg = False
            elif mystr[i] == '/':
                if miflg:
                    censu = int(tmstr)
                    tmstr = mistr
                if not Unit.findUnit(ccflg, tmstr, punit, censu, annit):
                    raise IlligalUnit()
                tmstr = ''
                ccflg = False
                censu = 1
                miflg = False
            else:
                tmstr += mystr[i]
        if miflg:
            censu = int(tmstr)
            tmstr = mistr
        if not Unit.findUnit(ccflg, tmstr, punit, censu, annit):
            raise IlligalUnit()
        return punit, annit

    @staticmethod
    def genUnit(name):
        u1, u2 = Unit.analysis(name)
        re = {i1:(u1[i1], u2[i1]) for i1 in xrange(0, len(u2)) if u1[i1]!=0}
        return Unit(re)

    def __init__(self, data=None):
        BaseUnit.__init__(self, data)

    def __repr__(self):
        re = ''
        for e1 in  self.data.values():
            if e1[0] == 1:
                re += '*' + e1[1]
            else:
                re += '*' + e1[1] + '^' + str(e1[0])
        return re[1:]

    def copy(self):
        return Unit(self.data)

    def normalize(self):
        ratio = 1e0
        for e1, e2 in self.data.items():
            ratio *= UNIT_DATA[e1][e2[1]] ** e2[0]
            self.data[e1] = (e2[0], UNIT_DATA[e1]['default'])
        return ratio

    def convert(self, other):
        '''Convert other to the same as self.
        '''
        ra = 1e0
        for e1 in other.data.keys():
            if self.data.has_key(e1):
                ra *= (UNIT_DATA[e1][self.data[e1][1]] /
                    UNIT_DATA[e1][other.data[e1][1]]) ** other.data[e1][0]
        return ra


    def __eq__(self, other):
        p1 = self.data.keys()
        p2 = other.data.keys()
        if p1 != p2:
            return False
        for e1 in xrange(0, len(p1)):
            if self.data[p1[e1]][0] != other.data[p2[e1]][0]:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self != other:
            raise UnmatchedUnits()
        return (self.copy(), self.convert(other))

    def __sub__(self, other):
        if self != other:
            raise UnmatchedUnits()
        return (self.copy(), self.convert(other))

    def __mul__(self, other):
        it = other.data.items()
        re = self.copy()
        for i1 in xrange(0, len(it)):
            if not re.data.has_key(it[i1][0]):
                re.data[it[i1][0]] = it[i1][1]
            else:
                tmp = re.data[it[i1][0]][0] + it[i1][1][0]
                if tmp == 0:
                    del re.data[it[i1][0]]
                else:
                    re.data[it[i1][0]] = (tmp, re.data[it[i1][0]][1])
        return (re, self.convert(other))

    def __div__(self, other):
        it = other.data.items()
        re = self.copy()
        for i1 in xrange(0, len(it)):
            if not re.data.has_key(it[i1][0]):
                re.data[it[i1][0]] = (-it[i1][1][0], it[i1][1][1])
            else:
                tmp = re.data[it[i1][0]][0] - it[i1][1][0]
                if tmp == 0:
                    del re.data[it[i1][0]]
                else:
                    re.data[it[i1][0]] = (tmp, re.data[it[i1][0]][1])
        return (re, self.convert(other))

class ValueUnit(float):
    def __init__(self, value=0.0, unit=None):
        float.__init__(self, value)
        if unit is None:
            self.unit = Unit()
        else:
            self.unit = unit

    def __abs__(self):
        return ValueUnit(float.__abs__(self), self.unit)
        
    def __add__(self, other):
        reunit = self.unit + other.unit
        return ValueUnit(float.__add__(self, float.__mul__(other, reunit[1])), reunit[0])
        
    def __sub__(self, other):
        reunit = self.unit - other.unit
        return ValueUnit(float.__sub__(self, float.__mul__(other, reunit[1])), reunit[0])
    
    def __div__(self, other):
        reunit = self.unit / other.unit
        return ValueUnit(float.__div__(self, float.__mul__(other, reunit[1])), reunit[0])

    def __mul__(self, other):
        reunit = self.unit * other.unit
        return ValueUnit(float.__mul__(self, float.__mul__(other, reunit[1])), reunit[0])
        
    def __divmod__(self, other):
        if self.unit != other.unit:
            raise UnmatchedUnits()
        return ValueUnit(float.__divmod__(self, other), Unit())

    def convert(self, unit_after):
        ra = unit_after.convert(self.unit)
        return ValueUnit(float.__mul__(self, ra), unit_after.copy())

    def normalize(self):
        ra = self.unit.normalize()
        self = ValueUnit(float.__mul__(self, ra), self.unit)

