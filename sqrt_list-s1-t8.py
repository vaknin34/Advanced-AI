import math

def sqrt_list(l):
    total = sum(l)
    square_root = math.sqrt(total)
    return round(square_root, 2)

print(sqrt_list([6,18,7,5]) == 6.0)
print(sqrt_list([50,2,33,8,4,3,10]) == 10.49)