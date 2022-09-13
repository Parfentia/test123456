import math
import pytest

test_data = [
    (0, 'a'),
    (1, 'b'),
    (2, 'c'),
    (3, 'd'),
    (4, 'e')
]

@pytest.mark.parametrize("index, result", test_data)
def test_get_by_index_tuple(index, result):
    tuple = ('a', 'b', 'c', 'd', 'e')
    assert tuple[index] == result

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_type_int():
    num = 10
    assert str(type(num)) == "<class 'int'>"

def test_check_len_tuple():
    tuple = ('a', 'b', 'c', 'd')
    assert len(tuple) == 4

def test_check_index():
    list = [1, 2, 3]
    try:
        assert list[4] == 4
    except IndexError:
        pass

def test_add_element_to_list():
    list = [1, 2, 3, 4]
    list += [5]
    assert list == [1, 2, 3, 4, 5]
