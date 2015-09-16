__author__ = 'trevorbillwaite'

# Introduction to Computer Science
# CelsiusToFarenheit.py

# Program will compute and print a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C

constant = 32
fraction = (9 / 5)
for C in range(0,101,10):
    F = (C * fraction) + constant
    print(C,F)