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
            self.data = data

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
                re += '*' + e1[1] + '^' + e1[0]
        return re[1:]

    def copy(self):
        return Unit(self.data)

    def normalize(self):
        ratio = 1e0
        for e1, e2 in self.data.items():
            ratio *= UNIT_DATA[e1][e2[1]]
            self.data[e1] = (e2[0], UNIT_DATA[e1]['default'])
        return ratio

    def convert(self, other):
        re = self.copy()
        ra = 1e0
        for e1 in self.data.keys():
            ra *= other.data.keys()


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
        return self.copy()

    def __sub__(self, other):
        if self != other:
            raise UnmatchedUnits()
        return self.copy()

    def __mul__(self, other):
        it = other.data.items()
        re = self.copy()
        for i1 in xrange(0, len(it)):
            if not re.data.has_key(it[i1][0]):
                re.data[it[i1][0]] = it[i1][1]
            tmp = re.data[it[i1][0]][0] + it[i1][1][0]
            if tmp == 0:
                del re.data[it[i1][0]]
            else
                re.data[it[i1][0]] = (tmp, re.data[it[i1][0]][1])
        return re,

    def __div__(self, other):
        it = other.data.items()
        re = self.copy()
        for i1 in xrange(0, len(it)):
            if not re.data.has_key(it[i1][0]):
                re.data[it[i1][0]] = -it[i1][1]
            tmp = re.data[it[i1][0]][0] - it[i1][1][0]
            if tmp == 0:
                del re.data[it[i1][0]]
            else
                re.data[it[i1][0]] = (tmp, re.data[it[i1][0]][1])
        return re,

class ValueUnit(float):

    @staticmethod
    def convert(value, unit_before, unit_after):
        if unit_before is unit_after:
            return value
        return value * unit_after.ratio() / unit_before.ratio()

    def __init__(self, value, unit):
        float.__init__(self, value)
        self.unit = unit

    def __abs__(self):
        return ValueUnit(float.__abs__(self), self.unit)
        
    def __add__(self, other):
        self.unit += other.unit 
##
        return ValueUnit(float.__add__(self, other), self.unit)
        
    def __div__(self, other):
        self.unit
        return ValueUnit(float.__div__(self, other))
        
    def __divmod__(self, other):
        if self.unit.data != self.other.data:
            raise Exception('Different Type of Data')

        return ValueUnit(float.__add__(self, other))

