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

