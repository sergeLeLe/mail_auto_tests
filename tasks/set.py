from typing import Optional


def add_even(numbers: list[int]) -> set[Optional[int]]:
    return {
        number for number in numbers
        if number % 2 == 0
    }