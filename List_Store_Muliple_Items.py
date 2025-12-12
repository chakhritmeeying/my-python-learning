fruit = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 42, 3.14, True]

print(fruit[0])
print(fruit[1])
print(fruit[2])
print(len(fruit))
# len() function returns the number of items in a list but only use for String variable
# print(len(numbers))
# print(len(mixed))

for fruit in fruit:
    print(fruit)
for numbers in numbers:
    print(numbers)
for mixed in mixed:
    print(mixed)
