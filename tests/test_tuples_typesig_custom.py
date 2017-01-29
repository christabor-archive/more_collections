from more_collections import tuples

import pytest


def test_typedtuple_custom():
    tpl = tuples.typedtuple(int, dict, list, int, float)
    assert tpl(3, {}, [], 3, 3.0) == (3, {}, [], 3, 3.0)


def test_typedtuple_custom_invalid():
    tpl = tuples.typedtuple(int, dict, list, int, float)
    with pytest.raises(ValueError):
        assert tpl('3', {}, [], 3, 3.0)


def test_typedtuple_custom_object_class():
    tpl = tuples.typedtuple(int, dict, list, int, object)
    class Foo(object):
        pass
    assert tpl(3, {}, [], 3, Foo)


def test_typedtuple_custom_object_invalid():
    tpl = tuples.typedtuple(int, dict, list, int, object)
    class Foo(object):
        pass
    with pytest.raises(ValueError):
        assert tpl(3, {}, [], 3, Foo())
