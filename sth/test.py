# -*- coding:utf-8 -*-
# filename: sth/test.py
# by スノル
from units import api as sua
from units.api import V

from traits import api as ta

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
