# -*- coding:utf-8 -*-
# filename: sciNote/units/value_type.py
# by スノル

from sys import stdout
from .unit_error import UnmatchedUnits, ComplexError, ValueInitError
from .bases import Unit, genUnit

class ValueUnit(complex):
    def __new__(cls, value=0.0 + 0.0j, unit=None):
        obj = complex.__new__(cls, value)
        if unit is None:
            obj.unit = Unit()
        else:
            obj.unit = unit
        return obj
    
    def isreal(self):
        return self.imag == 0

    def __eq__(self, other):
        return complex.__eq__(self,
            complex.__mul__(other, self.unit.convert(other.unit)))

    def __abs__(self):
        return ValueUnit(complex.__abs__(self), self.unit)
 
    def __add__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(complex.__add__(self, other), self.unit)
        reunit = self.unit + other.unit
        return ValueUnit(complex.__add__(self, complex.__mul__(other, reunit[1])
            ), reunit[0])

    def __radd__(self, other):
        return self + other
        
    def __sub__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(complex.__sub__(self, other), self.unit)
        reunit = self.unit - other.unit
        return ValueUnit(complex.__sub__(self, complex.__mul__(other, reunit[1])
            ), reunit[0])
    
    def __rsub__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(other) - self
    
    def __div__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(complex.__div__(self, other), self.unit)
        reunit = self.unit / other.unit
        return ValueUnit(complex.__div__(self, complex.__mul__(other, reunit[1])
            ), reunit[0])

    def __rdiv__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(other) / self

    def __mul__(self, other):
        if not isinstance(other, ValueUnit):
            return ValueUnit(complex.__mul__(self, other), self.unit)
        reunit = self.unit * other.unit
        return ValueUnit(complex.__mul__(self, complex.__mul__(other, reunit[1])), reunit[0])

    def __rmul__(self, other):
        return self * other

    def __divmod__(self, other):
        if self.unit != other.unit:
            raise UnmatchedUnits()
        return ValueUnit(complex.__divmod__(self, other), Unit())

    def __pow__(self, other):
        if isinstance(other, ValueUnit) and other.unit != Unit():
            raise UnmatchedUnits()
        if self.unit != Unit():
            if isinstance(other, int) or (other.imag == 0 and other.real.is_integer()):
                return ValueUnit(complex.__pow__(self, other), self.unit**(other.real))
            else:
                raise UnmatchedUnits()
        return ValueUnit(complex.__pow__(self, other), Unit())

    def __rpow__(self, other):
        if self.unit != Unit():
            raise UnmatchedUnits()
        return ValueUnit(complex.__rpow__(self, other), Unit())

    def __gt__(self, other):
        if self.imag !=0 or other.imag != 0:
            raise ComplexError()
        return self.real > (complex.__mul__(other, self.unit.convert(other.unit))).real
    
    def __ge__(self, other):
        if self.imag !=0 or other.imag != 0:
            raise ComplexError()
        return self.real >= (complex.__mul__(other, self.unit.convert(other.unit))).real

    def __lt__(self, other):
        if self.imag !=0 or other.imag != 0:
            raise ComplexError()
        return self.real < (complex.__mul__(other, self.unit.convert(other.unit))).real

    def __le__(self, other):
        if self.imag !=0 or other.imag != 0:
            raise ComplexError()
        return self.real <= (complex.__mul__(other, self.unit.convert(other.unit))).real
    

    def convert(self, unit_after):
        if isinstance(unit_after, basestring):
            unit_after = genUnit(unit_after)
        ra = unit_after.convert(self.unit)
        return ValueUnit(complex.__mul__(self, ra), unit_after.copy())

    def normalize(self):
        ra = self.unit.normalize()
        return ValueUnit(complex.__mul__(self, ra[1]), ra[0])

    def __unicode__(self):
        if self.isreal():
            return '%s %s' % (self.real, unicode(self.unit))
        return u'(%s+%sj) %s ' % (self.real ,self.imag, unicode(self.unit))

    def __str__(self):
        if self.isreal():
            return '%s %s' % (self.real, self.unit)
        return '(%s+%sj) %s' % (self.real, self.imag ,self.unit)

    def __repr__(self):
        return str(self)

    def printme(self, out=stdout, method='sci'):
        if method == 'sci':
            if self.isreal():
                out.write('%e %s\n' % (self.real, unicode(self.unit)))
            else:
                out.write('(%e+%ej) %s\n' % (self.real, self.imag, unicode(self.unit)))
        else:
            out.write(unicode(self))

def genValue(*value):
    if len(value)>=2:
        t = genUnit(value[1])
        return ValueUnit(complex(value[0]) * t[1], t[0])
    value = value[0]
    if isinstance(value, complex) or isinstance(value, float) or isinstance(value, int):
        return ValueUnit(value)
    if isinstance(value, basestring):
        for i1 in xrange(0, len(value)):
            if value[i1].isalpha():
                t = genUnit(value[i1:])
                return ValueUnit(complex(value[:i1]) * t[1], t[0])
        return ValueUnit(value)
    raise ValueInitError()

