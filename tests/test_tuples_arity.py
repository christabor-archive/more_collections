from more_collections import tuples

import pytest


def test_1_tuple_arity():
    assert tuples.n_tuple(1)('bar') == ('bar',)


def test_1_tuple_invalid_arity():
    with pytest.raises(ValueError):
        tuples.n_tuple(1)('foo', 'bar')


def test_2_tuple():
    assert tuples.n_tuple(2)('foo', 'bar') == ('foo', 'bar')


def test_2_tuple_invalid_arity():
    with pytest.raises(ValueError):
        tuples.n_tuple(2)('33', 'foo', 'bar')


def test_3_tuple():
    assert tuples.n_tuple(3)('foo', 'bar', 'baz') == ('foo', 'bar', 'baz')


def test_3_tuple_invalid_arity():
    with pytest.raises(ValueError):
        tuples.n_tuple(3)('33', 'foo', 'bar', '33')


def test_4_tuple():
    assert tuples.n_tuple(4)(
        'foo', 'bar', 'baz', 'quux') == ('foo', 'bar', 'baz', 'quux')


def test_4_tuple_invalid_arity():
    with pytest.raises(ValueError):
        tuples.n_tuple(4)('foo')
