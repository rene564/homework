import math

r1 = float(input())
r2 = float(input())

R = max(r1, r2)
r = min(r1, r2)

a = math.pi * (R**2 - r**2)
print(a)