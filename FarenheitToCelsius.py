__author__ = 'trevorbillwaite'

# Introduction to Computer Science
# FarenheitToCelsius.py

# Program will ask for the user to input a temperature in Farenheit and then convert it to Celsius.

F = eval(input("Please enter a temperature in Farenheit: "))
constant = 32
fraction = (5 / 9)
C = (F - constant) * fraction
print("The temperature " ,F, "in Farenheit is equivalent to " ,C, "in Celsius.")