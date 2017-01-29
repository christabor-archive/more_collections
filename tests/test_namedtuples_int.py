from more_collections import tuples

import pytest


def test_typednamedtuple():
    Person = tuples.typednamedtuple('Person', ['name', 'age'], [str, int])
    person = Person('Chris', 999)
    person2 = Person('Ella', 2)
    assert person.name == 'Chris'
    assert person.age == 999
    assert person2.name == 'Ella'
    assert person2.age == 2


def test_typednamedtuple_invalid():
    Person = tuples.typednamedtuple('Person', ['name', 'age'], [str, int])
    with pytest.raises(ValueError):
        Person('Chris', '999')
