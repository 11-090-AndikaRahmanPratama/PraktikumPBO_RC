height = int(input("Height: "))
for i in range(1, 1 + height):
    print(" " * (height - i) + "*" * (2 * i - 1))

