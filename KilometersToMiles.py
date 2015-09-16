__author__ = 'trevorbillwaite'

# Introduction to Computer Science
# FarenheitToCelsius.py

# Program will prompt the user for a distance measured in kilometers, convert it to miles, and print out the results.

Km = eval(input("Please enter a distance in Kilometers: "))
multiplier = 0.62
M = Km * multiplier
print(Km, "Kilometers is equivalent to " ,M, "Miles.")
