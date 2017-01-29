"""Specialized tuples."""

import inspect

from collections import namedtuple


def n_tuple(argcount):
    """Return a new function to generate an n-tuple with.

    That works only if the specified arity is met when called.
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


def typedtuple(*typesig):
    """Return a new function to generate an n-tuple with.

    That works only if the entire type signature is identical when called.
    """
    def _tuple(*someargs):
        if len(someargs) != len(typesig):
            raise ValueError(
                '{}-tuple requires arity of {}, '
                'but arity of {} was passed'.format(
                    len(typesig),
                    len(typesig),
                    len(someargs)
                ))
        called_typesig = []
        for arg in someargs:
            if inspect.isclass(arg):
                called_typesig.append(object)
            else:
                called_typesig.append(type(arg))
        _typesig = list(typesig)
        if called_typesig != _typesig:
            raise ValueError(
                'Called with type signature "{}" '
                'but expected {}'.format(called_typesig, _typesig)
            )
        return tuple(someargs)
    return _tuple


def typednamedtuple(name, props, typesig):
    """Return a new function to generate a namedtuple with.

    That works only if the entire type signature is identical when called.


    Traditional NT use:
    >>> Person = namedtuple('Person', ['name', 'age'])
    >>> person = Person('Chris', 32)

    This usage:
    >>> Person = namedtypedtuple('Person', ['name', 'age'], [str, int])
    >>> person = Person('Chris', 32)
    but this throws ValueError:
    >>> person = Person('Chris', '32')
    """
    def _namedtuple(*someargs):
        nt = namedtuple(name, props)

        def _called(*_):
            if len(someargs) != len(typesig):
                raise ValueError(
                    '{}-tuple requires arity of {}, '
                    'but arity of {} was passed'.format(
                        len(typesig),
                        len(typesig),
                        len(someargs)
                    ))
            called_typesig = []
            for arg in someargs:
                if inspect.isclass(arg):
                    called_typesig.append(object)
                else:
                    called_typesig.append(type(arg))
            _typesig = list(typesig)
            if called_typesig != _typesig:
                raise ValueError(
                    'Called with type signature "{}" '
                    'but expected {}'.format(called_typesig, _typesig)
                )
            return nt(*someargs)
        return _called(*someargs)
    return _namedtuple
