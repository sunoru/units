
from .unit_error import UnmatchedUnits
from .bases import Unit
from .utils import genUnit

class ValueUnit(complex):
    def __new__(cls, value=0.0 + 0.0j, unit=None):
        obj = complex.__new__(cls, value)
        if unit is None:
            obj.unit = Unit()
        else:
            obj.unit = unit
        if isinstance(obj.unit, str):
            obj.unit = genUnit(obj.unit)
        return obj
    
    def isreal(self):
        return self.imag == 0

    def __eq__(self, other):
        return complex.__eq__(self,
            complex.__mul__(other, self.unit.convert(other.unit)[1]))

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
        return complex.__gt__(self,
            complex.__mul__(other, self.unit.convert(other.unit)[1]))
    
    def __ge__(self, other):
        return complex.__ge__(self,
            complex.__mul__(other, self.unit.convert(other.unit)[1]))

    def __lt__(self, other):
        return complex.__lt__(self,
            complex.__mul__(other, self.unit.convert(other.unit)[1]))

    def __le__(self, other):
        return complex.__le__(self,
            complex.__mul__(other, self.unit.convert(other.unit)[1]))
    

    def convert(self, unit_after):
        ra = unit_after.convert(self.unit)
        return ValueUnit(complex.__mul__(self, ra), unit_after.copy())

    def normalize(self):
        ra = self.unit.normalize()
        return ValueUnit(complex.__mul__(self, ra[1]), ra[0])

    def __repr__(self):
        if self.isreal():
            return str(self.real) + ' ' + str(self.unit)
        return '(' + str(self.real) + '+' + str(self.imag) + 'j) ' + str(self.unit)
