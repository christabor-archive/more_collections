from more_collections import tuples

import pytest


def test_int_tuple1():
    assert tuples.typedtuple(int)(1) == (1,)


def test_int_tuple1_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int)(1, 2)


def test_int_tuple1_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int)('1')


def test_int_tuple2():
    assert tuples.typedtuple(int, int)(1, 2) == (1, 2)


def test_int_tuple2_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int)(1)


def test_int_tuple2_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int)(1, '2')


def test_int_tuple3():
    assert tuples.typedtuple(int, int, int)(1, 2, 3) == (1, 2, 3)


def test_int_tuple3_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int, int)('foo')


def test_int_tuple3_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int, int)('1', 2, 3)


def test_int_tuple4():
    assert tuples.typedtuple(int, int, int, int)(1, 2, 3, 4) == (1, 2, 3, 4)


def test_int_tuple4_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int, int, int)(1)


def test_int_tuple4_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(int, int, int, int)('1', '2', '3', '4')
