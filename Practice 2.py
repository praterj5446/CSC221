# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:17:07 2019

@author: prate
"""

""" Swap two numbers"""


def swap(a, b):
    """
    input two numbers
    output: the numbers in reverse order
    
    >swap(1,2)
    (2,1)
    
    """
    return b, a #TODO actually do this


first = int(input("Enter a number "))

second = int(input("Enter a number "))

print("Your numbers are: ")
print(first, second)

print("When I swap them, they are: ")

#this is "unpacking"
swapped = swap(first, second)
first = swapped[0]
second = swapped[1]
print(swap(first, second))