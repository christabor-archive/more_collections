"""Specialized dicts."""


def typeddict(expected_k, expected_v):
    """Return a dictionary that enforces a key/value type signature.

    >>> tdict = typeddict(int, str)
    >>> mydict = tdict()
    >>> mydict[3] = 'three'

    But this fails:

    >>> mydict['3'] = 'three'
    """
    class TypedDict(dict):
        def __setitem__(self, k, v):
            if not isinstance(k, expected_k):
                raise ValueError(
                    'Tried to set key "{}" of type "{}" but '
                    'expected type of "{}"'.format(k, type(k), expected_k))
            if not isinstance(v, expected_v):
                raise ValueError(
                    'Tried to set value "{}" of type "{}" but '
                    'expected type of "{}"'.format(v, type(v), expected_v))
            return super(TypedDict, self).__setitem__(k, v)
    return TypedDict
