"""Specialized tuples."""


def n_tuple(argcount):
    """Return a new function to generate a tuple.

    But only if the specified arity is met.
    """
    def _tuple(*someargs):
        if len(someargs) != argcount:
            raise ValueError(
                '{}-tuple requires arity of {}, '
                'but arity of {} was passed'.format(
                    argcount,
                    argcount,
                    len(someargs)
                ))
        return tuple(someargs)
    return _tuple


def tuple1(*args):
    """Create a 1-tuple."""
    return n_tuple(2)(*args)


def tuple2(*args):
    """Create a 2-tuple."""
    return n_tuple(2)(*args)


def tuple3(*args):
    """Create a 3-tuple."""
    return n_tuple(3)(*args)


def tuple4(*args):
    """Create a 4-tuple."""
    return n_tuple(3)(*args)
