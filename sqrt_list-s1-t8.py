import math

def sqrt_list(l):
    total = sum(l)
    sqrt_total = math.sqrt(total)
    return round(sqrt_total, 2)

print(sqrt_list([6,18,7,5]) == 6.0)
print(sqrt_list([50,2,33,8,4,3,10]) == 10.49)