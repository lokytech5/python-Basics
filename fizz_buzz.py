"""
This is a simple script that prints "Hello World".
"""


def fizz_buzz1(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"


print(fizz_buzz1(3))


def fizz_buzz2(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz2(3))
