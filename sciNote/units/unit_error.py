
class BaseError(Exception):
    _mes = 'Unknown Error.'
    def __init__(self):
        Exception.__init__(self, self._mes)

class IlligalUnit(BaseError):
    _mes = 'Illigal Unit!'

class UnmatchedUnits(BaseError):
    _mes = 'Unmatched Units!'
