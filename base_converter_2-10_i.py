# Author: Hannah Lever
# Date: 7\8 Mar 2025
# Hannah's Base Converter: Integers of Bases 2-10

def to_dec(base, num):
    # store -/+ to treat num as positive through calculations
    sign = num / abs(num)
    num = abs(num)

    result = 0
    mult = 1
    while num > 0:
        result += (num % 10) * mult
        num = num // 10
        mult = mult * base

    # restore -/+
    result = result * sign
    return int(result)


