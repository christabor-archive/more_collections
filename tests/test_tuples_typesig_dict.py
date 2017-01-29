from more_collections import tuples

import pytest


def test_dict_tuple1():
    assert tuples.typedtuple(dict)({}) == ({},)


def test_dict_tuple1_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict)({}, {})


def test_dict_tuple1_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict)(1)


def test_dict_tuple2():
    assert tuples.typedtuple(dict, dict)({}, {}) == ({}, {})


def test_dict_tuple2_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict, dict)('foo')


def test_dict_tuple2_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict, dict)(1, 2)


def test_dict_tuple3():
    assert tuples.typedtuple(dict, dict, dict)({}, {}, {}) == ({}, {}, {})


def test_dict_tuple3_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict, dict, dict)('foo')


def test_dict_tuple3_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict, dict, dict)('1', 2, 3)


def test_dict_tuple4():
    assert tuples.typedtuple(
        dict, dict, dict, dict)({}, {}, {}, {}) == ({}, {}, {}, {})


def test_dict_tuple4_invalid_arity():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(dict, dict, dict, dict)(1)


def test_dict_tuple4_invalid_type():
    with pytest.raises(ValueError):
        assert tuples.typedtuple(
            dict, dict, dict, dict)({}, {}, {}, '4')
