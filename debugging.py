"""
This is a simple script that prints "Hello World".
"""
def multiply (*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")