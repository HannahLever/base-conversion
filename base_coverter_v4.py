# Author: Hannah Lever
# Hannah's Base Converter: Integers of Bases 2-35

print(ord("0"))

def parse_digit(digit):
    if ord(digit) >= 48 and ord(digit) <= 57:
        return int(digit)
    elif ord(digit) >= 97 and ord(digit) <= 122:
        return ord(digit) - 87
    else:
        print("ERROR: not a valid digit")
        return -1

