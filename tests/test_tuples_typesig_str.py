from more_collections import tuples

import pytest


def test_str_tuple1():
    assert tuples.typedtuple(str)('foo') == ('foo',)


def test_str_tuple1_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str)('foo', 'bar')


def test_str_tuple1_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str)(1)


def test_str_tuple2():
    assert tuples.typedtuple(str, str)('foo', 'bar') == ('foo', 'bar')


def test_str_tuple2_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str)('foo')


def test_str_tuple2_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str)(1, 2)


def test_str_tuple3():
    assert tuples.typedtuple(
        str, str, str)('foo', 'bar', 'baz') == ('foo', 'bar', 'baz')


def test_str_tuple3_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str, str)('foo')


def test_str_tuple3_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str, str)(1, 2, 3)


def test_str_tuple4():
    assert tuples.typedtuple(str, str, str, str)(
        'foo', 'bar', 'baz', 'foo') == ('foo', 'bar', 'baz', 'foo')


def test_str_tuple4_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str, str, str)('foo')


def test_str_tuple4_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(str, str, str, str)(1, 2, 3, 4)
