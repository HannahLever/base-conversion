# Author: Hannah Lever
# Date: 7\8 Mar 2025
# Hannah's Base Converter: Integers of Bases 2-10

def to_dec(base, num):
    # store -/+ to treat num as positive through calculations
    sign = int(num / abs(num))
    num = abs(num)

    result = 0
    mult = 1
    while num > 0:
        result += (num % 10) * mult
        num = num // 10
        mult = mult * base

    # restore -/+
    result = sign * result
    return result

def from_dec(base, num):
    # store -/+ to treat num as positive through calculations
    sign = int(num / abs(num))
    num = abs(num)
    
    result = ""
    while num > 0:
        result = str(num % base) + result
        num = num // base

    # restore - if starting integer was negative
    result = sign * int(result)
    return result

def base_check(base, num):
    # check each digit: if greater than highest digit of base return False
    while num > 0:
        if num % 10 > base - 1:
            return False
        num = num // 10
    #else: true
    return True

def get_base(message):
    valid_input = False
    while valid_input == False:
        try:
            base = int(input(message))
        except ValueError:
            print("Not a valid integer, please try again.")
            continue
        if base <= 10 and base > 0:
            valid_input = True
        else:
            print("Unsupported base, please try again.")
    return base

print("Welcome to Hannah's integer base converter!\nSupported bases: 1-10\n")


start_base = get_base("Initial base: ")
end_base = get_base("Desired base: ")

valid_input = False
while valid_input == False:
    try:
        start_int = int(input("Integer to convert: "))
    except ValueError:
        print("Not a valid integer, please try again.")
        continue
    if not base_check(start_base, start_int):
        print("Not a valid integer in initial base, please try again.")
    else:
        valid_input = True
