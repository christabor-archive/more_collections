from more_collections import dicts

import pytest


def test_typeddict():
    tdict = dicts.typeddict(int, str)
    mydict = tdict()
    mydict[3] = 'three'
    assert mydict[3] == 'three'


def test_typeddict_invalid_type_key():
    tdict = dicts.typeddict(int, str)
    mydict = tdict()
    with pytest.raises(ValueError):
        mydict['3'] = 3


def test_typeddict_invalid_type_val():
    tdict = dicts.typeddict(int, str)
    mydict = tdict()
    with pytest.raises(ValueError):
        mydict[3] = 3
