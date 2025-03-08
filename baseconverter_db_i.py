# Author: Hannah Lever
# Date: 7 Mar 2025
# Hannah's Base Converter: Decimal & Binary Integers

def bin2dec(num):
    # store -/+ to treat num as positive through calculations
    sign = num / abs(num)
    num = abs(num)
    
    result = 0
    mult = 1 # multiplier for binary place value
    while num > 0:
        result += (num % 10) * mult 
        num = num // 10
        mult = mult * 2

    # restore -/+
    result = result * sign
    return int(result)

def dec2bin(num):
    # store -/+ to treat num as positive through calculations
    sign = num / abs(num)
    num = abs(num)
    
    result = 0
    while num > 0:
        result = result * 10
        result += num % 2
        num = num // 2

    # restore -/+
    result = result * sign
    return int(result)

def bincheck(num):
    # check each digit: if not 0 or 1, return false
    while num > 0:
        if num % 10 > 1:
            return False
        num = num // 10
    # else: true
    return True

print("Welcome to Hannah's integer base converter!\nSupported bases: 10, 2")

# Get starting base from user
valid_input = False
while valid_input == False:
    start_base = input("Would you like to convert a decimal or a binary integer (d/b)? ").lower()
    if start_base == "d" or start_base == "b":
        valid_input = True
    else:
        print("Invalid input, try again.")

# Get starting value from user
valid_input = False
while valid_input == False:
    start_int = input("Enter the integer you would like to convert: ")
    try:
        start_int = int(start_int)
        valid_input = True
    except ValueError:
        print("Not a valid integer, please try again.")
        continue
    if start_base == "b" and not bincheck(start_int):
        valid_input = False
        print("Not a valid binary integer, please try again.")

# Run appropriate conversion
if start_base == "d":
    result_int = dec2bin(start_int)
elif start_base == "b":
    result_int = bin2dec(start_int)

print(f"Result: {result_int}")
