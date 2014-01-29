
from .bases import Unit

def genUnit(name):
    u1, u2 = Unit.analysis(name)
    re = {i1:(u1[i1], u2[i1]) for i1 in xrange(0, len(u2)) if u1[i1]!=0}
    return Unit(re)

