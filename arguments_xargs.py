"""
This is a simple script that prints "Hello World".
"""
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user)


save_user(id=1, name="admin")