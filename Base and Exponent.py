# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 17:51:58 2020

@author: 14chr
"""
terms = int(input("How many terms? "))

base = int(input("What is the base? "))

result = list(map(lambda x: base ** x, range(terms+1)))

print("The total terms is: ", terms)
print("The base is ", base)
for i in range(terms+1):
    print(base, "raied to the power", i, "is", result[i])