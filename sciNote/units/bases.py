
import traits.api as ta

class BaseHasUnit ( ta.Float ):
    def get ( self, object, name ):
        print object
        print name
        ta.Float.get_value( self, object, name, BaseHasUnit )

    def set ( self, object, name ,value):
        print object
        print name
        print value
        ta.Float.set_value( self, object, name, value )

