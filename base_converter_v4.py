# Author: Hannah Lever
# Hannah's Base Converter: Integers of Bases 2-35

# take character, return int
def parse_digit(digit):
    # check if digit between 0 and 9, return input as int
    if ord(digit) >= 48 and ord(digit) <= 57:
        return int(digit)
    # check if lowercase letter, return integer value
    elif ord(digit) >= 97 and ord(digit) <= 122:
        return ord(digit) - 87
    # else: not convertable to int
    else:
        print("ERROR: Not a valid digit")
        return -1

# take int, return character
def encode_digit(digit)
    if digit >= 0 and digit <= 9:
        return str(digit)
    else if digit >= 10 and digit <= 35:
        return chr(digit + 87)
    else:
        print("ERROR: Value is less than 0 or greater than 35, cannot be converted")
        return -1
