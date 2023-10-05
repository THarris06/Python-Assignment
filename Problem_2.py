# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:57:38 2023

@author: Tyson Harris
"""

print ("\nTip Calculator\n")

# Ask for the cost of the meal
cost = float(input("Cost of meal: "))

# Calculate and store each tip in it's own variable
tip_15 = cost * 0.15
tip_20 = cost * 0.20
tip_25 = cost * 0.25


# Print the tip amount and the total for each unique tip percent
print ("\n15%")
print ("Tip amount: {:.2f}".format(tip_15))
print ("Total amount: {:.2f}".format(cost + tip_15))

print ("\n20%")
print ("Tip amount: {:.2f}".format(tip_20))
print ("Total amount: {:.2f}".format(cost + tip_20))

print ("\n25%")
print ("Tip amount: {:.2f}".format(tip_25))
print ("Total amount: {:.2f}".format(cost + tip_25))


