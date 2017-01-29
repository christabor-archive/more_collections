from more_collections import tuples

import pytest


def test_list_tuple1():
    assert tuples.typedtuple(list)([]) == ([],)


def test_list_tuple1_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list)([], [])


def test_list_tuple1_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list)(1)


def test_list_tuple2():
    assert tuples.typedtuple(list, list)([], []) == ([], [])


def test_list_tuple2_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list, list)('foo')


def test_list_tuple2_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list, list)(1, 2)


def test_list_tuple3():
    assert tuples.typedtuple(list, list, list)([], [], []) == ([], [], [])


def test_list_tuple3_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list, list, list)('foo')


def test_list_tuple3_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list, list, list)('1', 2, 3)


def test_list_tuple4():
    assert tuples.typedtuple(
        list, list, list, list)([], [], [], []) == ([], [], [], [])


def test_list_tuple4_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(list, list, list, list)(1)


def test_list_tuple4_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(
            list, list, list, list)([], [], [], '4')
