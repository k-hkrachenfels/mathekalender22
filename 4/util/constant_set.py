from __future__ import absolute_import, division, print_function, unicode_literals
from future.utils import with_metaclass

import inspect
from functools import cache

class MetaConstantSet(type):

    ordinals = None

    def __setattr__(cls, name, value):
        if name != 'ordinals':
            raise TypeError("Constant sets are immutable")

    def __delattr__(cls, name):
        raise TypeError("Constant sets are immutable")

    @property
    def values(cls):
        return set(
            [ 
                prop[1]
                for prop in inspect.getmembers(cls, lambda x: not inspect.isroutine(x))
                if not prop[0].startswith("__")
            ]
        )


    def __iter__(cls):
        for val in cls.values:
            yield val

    def __contains__(cls, item):
        return item in cls.values

    @cache
    def ordinal(cls,key):
        values=cls.values
        for i,val in enumerate(sorted(values)):
            if val==key:
                return i
        raise Exception(f"{key} is no element of ConstantSet")

    @cache
    def value(cls,ordinal):
        values=sorted(cls.values)
        return values[ordinal]


class ConstantSet(with_metaclass(MetaConstantSet, object)):
    """Constant set can be used as mixin, e.g. like in
    `class SomeClass(ConstantSet, SomeSuperClass):...`"""

    def __init__(self, *args, **kwargs):
        """Needed to support usage as mixin"""
        super().__init__(*args, **kwargs)  # forwards all arguments


# class Colors(ConstantSet):
#     RED="red"
#     BLUE="blue"
#     GREEN="green"

# print( "red" in Colors)
# print( [color for color in Colors] )