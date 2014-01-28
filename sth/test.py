# -*- coding:utf-8 -*-
# filename: sth/test.py
# by スノル
from sciNote.units import api as sua

from traits import api as ta

class Cs(ta.HasTraits):
    xsk = ta.Float
    xsk2 = sua.HasUnit
    lent = sua.Length
    xsk3 = 0.0
    def __init__(self):
        pass

x=Cs()
