# Author: Hannah Lever
# Date: 7 Mar 2025
# Hannah's Base Converter!

def bin2dec(num):
    sign = num / abs(num)
    num = abs(num)
    result = 0
    mult = 1 
    while num > 0:
        result += (num % 10) * mult 
        num = num // 10
        mult = mult * 2
    result = result * sign
    return int(result)

def dec2bin(num):
    sign = num / abs(num)
    num = abs(num)
    result = 0
    while num > 0:
        result = result * 10
        result += num % 2
        num = num // 2
    result = result * sign
    return int(result)

print("Welcome to Hannah's integer base converter!\nCurrently supported bases: 10, 2")

valid_input = False
while valid_input == False:
    start_base = input("Would you like to convert a decimal or a binary integer (d/b)? ").lower()
    if start_base == "d" or start_base == "b": valid_input = True
    else : print("Invalid input, try again.")

start_int = int(input("Enter the integer you would like to convert: "))
if start_base == "d":
    result_int = dec2bin(start_int)
elif start_base == "b":
    result_int = bin2dec(start_int)

print(f"Result: {result_int}")
