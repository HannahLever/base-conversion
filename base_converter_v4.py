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
def encode_digit(digit):
    if digit >= 0 and digit <= 9:
        return str(digit)
    elif digit >= 10 and digit <= 35:
        return chr(digit + 87)
    else:
        print("ERROR: Value is less than 0 or greater than 35, cannot be converted")
        return -1

# take origin base and num (as string), return int
def to_dec(base, num):
    # store -/+ to treat num as positive through calculations
    if num[0] == '-':
        sign = -1
        num = num[1:]
    else:
        sign = 1
    # multiply each digit by place value, sum with previous digit values
    result = 0
    mult = 1
    while len(num) > 0:
        result += parse_digit(num[-1]) * mult
        num = num[:-1]
        mult = mult * base
    # restore -/+
    result = sign * result
    return result

# take target base and int num, return string in target base
def from_dec(base, num):
    # store -/+ to treat num as positive through calculations
    if num < 0:
        sign = '-'
        num = abs(num)
    else:
        sign = ''
    # use remainder method to get each digit, starting with greatest value
    result = ""
    while num > 0:
        result = encode_digit(num % base) + result
        num = num // base
    if result == "":
        result = "0"
    # restore '-' if starting integer was negative
    result = sign + result
    return result

# check that str num is valid in base
def base_check(base, num):
    # strip sign
    if num[0] == '-':
        num = num[1:]
    # check each character: if not a digit or if a digit not in current base: return false 
    while len(num) > 0:
        cur_digit = parse_digit(num[-1])
        if cur_digit == -1 or cur_digit > base - 1:
            return False
        num = num[:-1]
    #else: true
    return True

# take input with prompt message, check that input is a valid base, return as int
def get_base(message):
    valid_input = False
    while valid_input == False:
        try:
            base = int(input(message))
        except ValueError:
            print("Not a valid integer, please try again.")
            continue
        if base > 1 and base <= 36:     # check that base is supported
            valid_input = True
        else:
            print("Unsupported base, please try again.")
    return base

def main():
    print("Welcome to Hannah's integer base converter!\nSupported bases: 2-36\n")

    start_base = get_base("Initial base: ")
    end_base = get_base("Desired base: ")

    valid_input = False
    while valid_input == False:
        start_num = input("Integer to convert: ")
        if not base_check(start_base, start_num):
            print("Not a valid integer in initial base, please try again.")
        else:
            valid_input = True

    dec = to_dec(start_base, start_num)
    result = from_dec(end_base, dec)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
