# -*- coding:utf-8 -*-
# filename: sciNote/units/bases.py
# by スノル

from .data import *
from .locals import *

class BaseUnit():
    @staticmethod
    def genUnitnameInit():
        re = []
        for e1 in UNIT_DATA.values():
            re.append(e1['default'])
        return re

    def __init__(self, unittype, unitname):
        if unittype is None:
            self.unittype = (0, ) * 7
        else:
            self.unittype = tuple(unittype)
        if unitname is None:
            self.unitname = tuple(BaseUnit.genUnitnameInit())
        else:
            self.unitname = tuple(unitname)

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
        annit = BaseUnit.genUnitnameInit()
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
                    raise Exception('Illigal Unit!')
                tmstr = ''
                ccflg = True
                censu = 1
                miflg = False
            elif mystr[i] == '/':
                if miflg:
                    censu = int(tmstr)
                    tmstr = mistr
                if not Unit.findUnit(ccflg, tmstr, punit, censu, annit):
                    raise Exception('Illigal Unit!')
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
            raise Exception('Illigal Unit!')
        return punit, annit

    @staticmethod
    def genUnit(name):
        u1, u2 = Unit.analysis(name)
        return Unit(u1, u2)

    def __init__(self, unittype=None, unitname=None):
        BaseUnit.__init__(self, unittype, unitname)

    def __repr__(self):
        re = ''
        for e1 in xrange(0, len(self.unittype)):
            if self.unittype[e1] == 0:
                continue
            elif self.unittype[e1] == 1:
                re += '*' + self.unitname[e1]
            else:
                re += '*' + self.unitname[e1] + '^' + str(self.unittype[e1])
        return re[1:]

    def __add__(self, other):
        if self.unittype != 


class ValueUnit(float):
    def __init__(self, value, unit):
        float.__init__(self, value)
        self.unit = unit
        
    @staticmethod
    def convert(value, unit_before, unit_after):
        if unit_before is unit_after:
            return value
        return value * unit_after.ratio() / unit_before.ratio()

    def __abs__(self):
        return ValueUnit(float.__abs__(self), self.unit)
        
    def __add__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')
# TODO
        self
        return ValueUnit(float.__add__(self, other), self.unit)
        
    def __div__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')
        return ValueUnit(float.__div__(self, other))
        
    def __divmod__(self, other):
        if self.unit.unittype != self.other.unittype:
            raise Exception('Different Type of Data')

        return ValueUnit(float.__add__(self, other))

