number = input("Type number: ")

# 01-1
length = len(number)
counter = 0

while counter < length:
    print(number[counter])
    counter += 1

# 01-2
for x in number:
    print(x)

# 02-1
a = int(input("First number: "))
b = int(input("Second number: "))

c = a
a = b
b = c

print(a, b)

# 02-2
a = int(input("First number: "))
b = int(input("Second number: "))

a = a + b
b = a - b
a = a - b

print(a, b)

# 03-1
age = int(input("Your age: "))

if age < 18:
    print("Sorry")
else:
    print("Success")
