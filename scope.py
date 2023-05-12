"""
This is a simple script that prints "Hello World".
"""
message = "a"


def greet():
    global message
    message = "b"


greet()
print(message)
