number = input("Type number: ")

# 01-1
length = len(number)
counter = 0
maximum = 0

while counter < length:
    new_value = int(number[counter])

    if new_value > maximum:
        maximum = new_value

    counter += 1

print(maximum)

# 01-2 (not exactly)
maximum = max(number) # <class 'str'> ENCODING SEARCH

# 02-1
a = int(input("First number: "))
b = int(input("Second number: "))

a, b = b, a

# 03-1
import math

# 5x^2 + 10x + 4 = 0
a = 5
b = 10
c = 4
# b^2 - 4ac
D = b ** 2 - (4 * a * c)
print("D =", D)
D_sqrt = math.sqrt(D)

x1 = 0
x2 = 0

if D == 0:
    x1 = (-b / 2 * a)
    print("X =", x1)
elif D < 0:
    print("no solution")
else:
    x1 = (-b + D_sqrt) / 2 * a
    x2 = (-b - D_sqrt) / 2 * a
    print("X1 =", x1, ", X2 =", x2)
