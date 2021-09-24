def sum_digits_of_number(num: float) -> float:
    return sum([float(char) for char in str(num) if char.isdigit()])