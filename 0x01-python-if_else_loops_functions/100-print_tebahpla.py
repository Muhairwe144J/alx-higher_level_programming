#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 == 1:
        print(chr(char - 32), end="")
    else:
        print(chr(char), end="")
