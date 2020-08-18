'''
Created by Vedant Christian
Created on 18 / 08 / 2020
'''

terms = int(input("How many terms? "))

base = int(input("What is the base? "))

result = list(map(lambda x: base ** x, range(terms+1)))

print("The total terms is: ", terms)
print("The base is ", base)
for i in range(terms+1):
    print(base, "raied to the power", i, "is", result[i])