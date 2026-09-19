# Write a python program to find remainder when a number is divided by z.
divisor = 6
print()
number = float(input(f"Enter the Number to be divided by {divisor} : "))
print("------------------------------------------------------")
normaldivision = round(number / divisor ,2)
flooredDivision = number // divisor
remainder = number % divisor

print(f"Dividing Inputted Number {number} with divisor {divisor}--> {normaldivision}")
print(f"Getting Divisor from upper Division --> {flooredDivision}")
print(f"Getting Remainder from upper Division --> {remainder}")