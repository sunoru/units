from sciNote.units import api as sua

from traits import api as ta

class Cs(ta.HasTraits):
    xsk=ta.Float
    xsk2=sua.BaseHasUnit
    def __init__(self):
        pass

x=Cs()
