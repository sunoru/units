# -*- coding:utf-8 -*-
# filename: sth/test.py
# by スノル
from sciNote.units import api as sua

from traits import api as ta

V = sua.Vu

class Cs(ta.HasTraits):
    xsk = ta.Float
    xsk2 = sua.HasUnit
    xsk3 = sua.HasUnit('m')
    def __init__(self):
        pass

x=Cs()
v1 = V('123', 'm/s')
v2 = V('120', u'µm/s')
#y = str(v2)
t = V('43.2', 's')
