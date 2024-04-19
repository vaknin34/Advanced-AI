import math

def sqrt_list(l: list) -> float:
    sum_of_list = sum(l)
    square_root = math.sqrt(sum_of_list)
    return round(square_root, 2)