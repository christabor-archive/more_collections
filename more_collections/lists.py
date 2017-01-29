"""Specialized lists."""


def typedlist(oktype):
    """Return a list that enforces a type signature on appends.

    >>> intlist = typedlist(int)
    >>> someints = intlist([1, 2, 3])

    But this fails:

    >>> someints = intlist(['1', '2', '3'])
    """
    class TypedList(list):
        def __init__(self, *lst):
            if lst:
                lst = lst[0]
                for el in lst:
                    if not isinstance(el, oktype):
                        raise ValueError(
                            'Tried to set value "{}" of type "{}" but '
                            'expected type of "{}"'.format(
                                el, type(el), oktype))
            return super(TypedList, self).__init__(lst)

        def append(self, v):
            if not isinstance(v, oktype):
                raise ValueError(
                    'Tried to set value "{}" of type "{}" but '
                    'expected type of "{}"'.format(v, type(v), oktype))
            return super(TypedList, self).append(v)

        def insert(self, i, v):
            if not isinstance(v, oktype):
                raise ValueError(
                    'Tried to set value "{}" of type "{}" but '
                    'expected type of "{}"'.format(v, type(v), oktype))
            return super(TypedList, self).insert(i, v)

        def extend(self, lst):
            for el in lst:
                if not isinstance(el, oktype):
                    raise ValueError(
                        'Tried to set value "{}" of type "{}" but '
                        'expected type of "{}"'.format(el, type(el), oktype))
            return super(TypedList, self).extend(lst)
    return TypedList
