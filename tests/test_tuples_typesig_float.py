from more_collections import tuples

import pytest


def test_float_tuple1():
    assert tuples.typedtuple(float)(.0) == (.0,)


def test_float_tuple1_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float)(.0, 0.)


def test_float_tuple1_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float)(1)


def test_float_tuple2():
    assert tuples.typedtuple(float, float)(.0, 0.) == (.0, 0.)


def test_float_tuple2_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float, float)('foo')


def test_float_tuple2_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float, float)(1, 2)


def test_float_tuple3():
    assert tuples.typedtuple(float, float, float)(.0, .0, .0) == (.0, .0, .0)


def test_float_tuple3_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float, float, float)('foo')


def test_float_tuple3_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float, float, float)('1', 2, 3)


def test_float_tuple4():
    assert tuples.typedtuple(
        float, float, float, int)(.0, .0, .0, 4) == (.0, .0, .0, 4)


def test_float_tuple4_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(float, float, float, float)(1)


def test_float_tuple4_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(
            float, float, float, float)('1', '2', '3', '4')
