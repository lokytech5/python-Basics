"""
This is a simple script that prints "Hello World".
"""
names = ["john", "Mary"]
found = False
for name in names:
    if name.startswith("o"):
        print("Found")
        break
else:
    print("Not found")
