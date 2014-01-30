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
        for e1 in DERIVED_DATA.keys():
            if tmstr.endswith(e1):
                if ccflg:
                    t = UNIT_PREFIX.get(tmstr[:len(tmstr)-len(e1)], None)
                    if t is None:
                        return None
                    knd = DERIVED_DATA[e1][0] * t
                    for e2 in DERIVED_DATA[e1][1].keys():
                        if annit[e2] != '':
                            knd /= UNIT_DATA[e2][annit[e2]]
                        else:
                            annit[e2] = UNIT_DATA[e2]['default']
                        punit[e2] += censu * DERIVED_DATA[e1][1][e2]
                else:
                    t = UNIT_PREFIX.get(tmstr[:len(tmstr)-len(e1)], None)
                    if t is None:
                        return None
                    knd = 1 / DERIVED_DATA[e1][0] / t
                    for e2 in DERIVED_DATA[e1][1].keys():
                        if annit[e2] != '':
                            knd *= UNIT_DATA[e2][annit[e2]]
                        else:
                            annit[e2] = UNIT_DATA[e2]['default']
                        punit[e2] -= censu * DERIVED_DATA[e1][1][e2]
                return knd
        for e1 in UNIT_DATA.values():
            for e2 in e1.keys():
                if e2 == tmstr:
                    annit[e1['type']] = e2
                    if ccflg:
                        punit[e1['type']] += censu
                    else:
                        punit[e1['type']] -= censu
                    return 1e0
        for e1 in DERIVED_UNIT.values():
            if tmstr.endswith(e1[0]):
                if ccflg:
                    t = UNIT_PREFIX.get(tmstr[:len(tmstr)-len(e1[0])], None)
                    if t is None:
                        return None
                    knd = t
                    for e2 in e1[1].keys():
                        if annit[e2] != '':
                            knd /= UNIT_DATA[e2][annit[e2]]
                        else:
                            annit[e2] = UNIT_DATA[e2]['default']
                        punit[e2] += censu * e1[1][e2]
                else:
                    t = UNIT_PREFIX.get(tmstr[:len(tmstr)-len(e1[0])], None)
                    if t is None:
                        return None
                    knd = 1 / t
                    for e2 in e1[1].keys():
                        if annit[e2] != '':
                            knd *= UNIT_DATA[e2][annit[e2]]
                        else:
                            annit[e2] = UNIT_DATA[e2]['default']
                        punit[e2] -= censu * e1[1][e2]
                return knd
        return None

    @staticmethod
    def analysis(name):
        mystr = name.replace(' ', '')
        punit = [0] * 7
        annit = [''] * 7
        if len(mystr) == 0:
            return punit, annit
        tmstr = ''
        ccflg = True
        censu = 1
        miflg = False
        xx = 1e0
        for i in xrange(0, len(mystr)):
            if mystr[i] == '^':
                miflg = True
                mistr = tmstr
                tmstr = ''
            elif mystr[i] == '*':
                if miflg:
                    censu = int(tmstr)
                    tmstr = mistr
                pt = Unit.findUnit(ccflg, tmstr, punit, censu, annit)
                if pt is None:
                    raise IlligalUnit()
                xx *= pt
                tmstr = ''
                ccflg = True
                censu = 1
                miflg = False
            elif mystr[i] == '/':
                if miflg:
                    censu = int(tmstr)
                    tmstr = mistr
                pt = Unit.findUnit(ccflg, tmstr, punit, censu, annit)
                if pt is None:
                    raise IlligalUnit()
                xx *= pt
                tmstr = ''
                ccflg = False
                censu = 1
                miflg = False
            else:
                tmstr += mystr[i]
        if miflg:
            censu = int(tmstr)
            tmstr = mistr
        pt = Unit.findUnit(ccflg, tmstr, punit, censu, annit)
        if pt is None:
            raise IlligalUnit()
        xx *= pt
        return punit, annit, xx

    def __init__(self, data=None):
        BaseUnit.__init__(self, data)

    def __unicode__(self):
        re = u''
        for e1 in self.data.values():
            if e1[0] == 1:
                re += '*%s' % e1[1]
            else:
                re += '*%s^%s' % (e1[1], str(e1[0]))
        return re[1:]

    def __str__(self):
        tmp = unicode(self)
        try:
            tmp = str(tmp)
        except:
            tmp = '<unable to show units>'
        return tmp

    def __repr__(self):
        return str(self)

    def copy(self):
        return Unit(self.data)

    def normalize(self):
        ratio = 1e0
        re = self.copy()
        for e1, e2 in re.data.items():
            ratio *= UNIT_DATA[e1][e2[1]] ** e2[0]
            re.data[e1] = (e2[0], UNIT_DATA[e1]['default'])
        return re, ratio

    def convert(self, other):
        '''Convert other to the same as self.
        '''
        ra = 1e0
        for e1 in other.data.keys():
            if self.data.has_key(e1):
                ra *= (UNIT_DATA[e1][other.data[e1][1]] /
                    UNIT_DATA[e1][self.data[e1][1]]) ** other.data[e1][0]
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

    def __pow__(self, other):
        re = self.copy()
        other = int(other)
        for e1 in re.data.keys():
            re.data[e1] = (re.data[e1][0] * other, re.data[e1][1])
        return re

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

def genUnit(name):
    if name is None:
        return None, 1e0
    u1, u2, xx= Unit.analysis(name)
    re = {i1:(u1[i1], u2[i1]) for i1 in xrange(0, len(u2)) if u1[i1]!=0}
    return Unit(re), xx
