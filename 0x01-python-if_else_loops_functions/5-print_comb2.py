#!/usr/bin/python3

for num in range(100):
    if num < 10:
        print("0", end="")
    print("{}".format(num), end="")
    if num < 99:
        print(", ", end="")
    else:
        print()
