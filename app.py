"""
This is a simple script that prints "Hello World".
"""
print("Hello world lokosman!")
students_count: int = 1000

print(type(students_count))
rating: float = 4.99
is_published: bool = False

x = [1, 2, 3]
print(id(x))

course = "Python Programming"
print(len(course))
print((course[0]))
print((course[-2]))

#slice in pythons
print((course[0:3]))
print((course[:3]))
print((course[0:]))
print(id(course))
# Escape Sequence in python
message = "Python \"Programming"
print(message)

first = "lokos"
last = "man"
full = f"{first} {last}"
print(full)
book = " Programming Books"
print(book.upper())
print(book.lower())
print(book.title())
print(book.strip())
# finding index in pthon
print(book.find("Pro"))
print(book.replace("P", "r"))
print("Programming" in book)

# Reprsent Numbers in python
x = 10
x = 0b10
print(bin(x))

#Hexadecimal in python
x = 0x12c
print(hex(x))

x = 1 + 2j
print(x)

#Working with Numbers
PI = -3.14
print(round(PI))
print(abs(PI))