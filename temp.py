
__author__ = 'trevorbillwaite'

# Introduction to Computer Science
# temp.py

# Program will compute and print a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C

# Declare Magic Numbers and Constants

# LOOPCOUNTER = 2
# name = "bob"

# Write program code here

# ask user if temperature is in Farenheit
# Convert to Celsius
# (F-32) * 5 / 9 = C

# output answer to user


# Input

# First Assignment

constant = 32
fraction = (9 / 5)
for C in range(0,101,10):
    F = (C * fraction) + constant
    print(C,F)
    
# Second Assignment

F = eval(input("Please enter a temperature in Farenheit: "))
fraction = (5 / 9)
C = (F - constant) * fraction
print("The temperature " ,F, "in Farenheit is equivalent to " ,C, "in Celsius.")



# Process

# Output

