import pytest

import tasks


def test_set1():
    s = set('hello')
    assert s == {'h', 'e', 'l', 'o'}
    s.update([1,2])
    assert s == {'h', 'e', 'l', 'o', 1, 2}
    s = s.union({'h', 'e', 3})
    assert s == {'h', 'e', 'l', 'o', 1, 2, 3}


@pytest.mark.parametrize('numbers,result', [
    ([1, 2, 3, 4, 5, 6], {2, 4, 6}),
    ([], set()),
    ([2, 2, 0], {0, 2}),
    ([1, 3], set()),
])
def add_even(numbers, result):
    assert tasks.add_even(numbers) == result


def test_set3():
    try:
        assert tasks.add_even(['asd', 2]) == {2}
    except TypeError:
        pass


    
    