import pytest

import tasks


def test_float1():
    assert 1.0 == float(1)
    assert 10 / 5 == 2.0


@pytest.mark.parametrize('number,result', [
    (126.6, 15.0),
    (1.0, 1.0),
    (-15, 6.0),
    (0.0, 0.0)
])
def test_sum_digits_of_number(number, result):
    assert tasks.sum_digits_of_number(number) == result


def test_float3():
    assert 0.1 == 0.10000000000000001








