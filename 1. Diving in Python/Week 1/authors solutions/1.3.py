import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b * b - 4 * a * c

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(int(x1))
print(int(x2))