# Using the Math Module for Calculations with Rounded Results

import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Perform calculations using math module
sqr = round(math.sqrt(num), 2)   # Rounded to 2 decimal places
logg = round(math.log(num), 2)     # Natural logarithm (base e)
sine = round(math.sin(num), 2)    # Sine of the number in radians

# 3. Display results
print("Square root of", num, "is:", sqr)
print("Natural logarithm of", num, "is:", logg)
print("Sine of", num, "is:", sine)

print('\t\t\t Thankyou!')
