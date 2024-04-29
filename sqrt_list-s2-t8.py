import math

def sqrt_list(l: list) -> float:
    return round(math.sqrt(sum(l)), 2)

print(sqrt_list([6,18,7,5]) == 6.0)
print(sqrt_list([50,2,33,8,4,3,10]) == 10.49)