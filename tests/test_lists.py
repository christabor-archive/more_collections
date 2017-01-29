from more_collections import lists

import pytest


def test_typedlist_append():
    tlist = lists.typedlist(int)
    mylist = tlist()
    mylist.append(3)
    assert mylist[0] == 3


def test_typedlist_append_invalid():
    tlist = lists.typedlist(int)
    mylist = tlist()
    with pytest.raises(ValueError):
        mylist.append('3')


def test_typedlist_insert():
    tlist = lists.typedlist(int)
    mylist = tlist()
    mylist.insert(0, 3)


def test_typedlist_insert_invalid():
    tlist = lists.typedlist(int)
    mylist = tlist()
    with pytest.raises(ValueError):
        mylist.insert(0, '3')


def test_typedlist_extend():
    tlist = lists.typedlist(int)
    mylist = tlist()
    mylist.extend([1, 2, 3])


def test_typedlist_extend_invalid():
    tlist = lists.typedlist(int)
    mylist = tlist()
    with pytest.raises(ValueError):
        mylist.extend(['1', '2', '3'])
