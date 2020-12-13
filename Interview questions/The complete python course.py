# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:07:00 2020

@author: INSAPAB
"""
import numpy as np
# short cut for commenting is Ctrl+/

# Name = 'John smith'
# Age = 20
# New = True
# print(Name, Age, New)

# name = input("What is your name? ")
# print("Hi " + name)
# favClr = input("What is your favourite colour? ")
# print(name + " likes " + favClr)

# birth_year = int(input("Birth year: "))
# age = 2019 - birth_year
# print(type(age))
# print(age)

# weight_pounds = float(input("How much(Pounds)? "))
# weight_kg = 0.453582*weight_pounds
# print("Weight_kg: ", weight_kg)

# course = 'Python for "beginners"'
# print(course)

# course = '''
# Hi,
#     please find the attachment.
# Best Regards,
# Sandeep Pabbathi
# '''
# # print(course[-2]) # get the charceter at that index
# another = course[:]
# #print(course[0:])
# print(another)

# name = 'Sandeep'
# print(name[1:-1])

# formatted strings
# first = 'San'
# last = 'Deep'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# # opeartion on strings
# course = 'My name is sandeep'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('s'))
# print(course.replace('is', 'are'))
# print('is' in course)

#  # airthmetic operation
# print(10 + 3)
# print(10/3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 3
# x+=3
# # print(x)
# import math
# x = 22
# print(math.cos(x))

# if elif else stmts
# is_hot = False
# is_cold = False
# if is_hot:
#     print('Its is hot day')
#     print('Drink lot of water')
# elif is_cold:
#     print('Its cold day')
# else:
#     print('its a lovely day')
# print('Enjoy your day')

# price = float(input('price of the house: '))
# good_credit = False
# if good_credit:
#     down_payment = float(0.1*price)
#     print(f'down payment:  $ {down_payment}')
# else:
#     down_payment = float(0.2 * price)
#     print(f'down payment: ${down_payment}')

# logical and or not operations
# has_high_income = True
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print('selected')
# else:
#     print('Not selected')

# comparators
# temp = 25
# if temp > 30:
#     print('Its hot day')
# elif temp < 10:
#     print('Its cold day')
# else:
#     print ('Its normal day')

# name = 'SAN'
# if len(name) < 3:
#     print('name must be at least 3 characters')
# elif len(name) > 50:
#     print('name can be at least 50 characters')
# else:
#     print('name looks good')

# weight converter
# weight = float(input('weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     converted = weight*0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight/0.45
#     print(f'You are {converted} pounds')

# while loop
# i =1
# while i<=5:
#     print('*'*i)
#     i = i+1
# print('Done')

# guessing game:
# secrete_number = 9
# count = 1
# guess_limit =3
# while count <= guess_limit:
#     guess_number = int(input('guess: '))
#     if guess_number == secrete_number:
#         print('you win!')
#         break
#     count = count + 1
# else:
#     print('you loose!')

## car game
# started = False
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''
# start - start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == 'start':
#         if not started:
#             print('car started..ready to go!')
#             started = True
#         else:
#             print('Hey car already started')
#     elif command == 'stop':
#         if started:
#             print('car stopped.')
#             started = False
#         else:
#             print('Hey car already stopped')
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that")

##for loops

# for item in 'Python':
#     print(item)
# for item in ['San', 'sandy', 'suri']:
#     print(item)
# for item in range(10):
#     print(item)
# for item in range(1,10,3):
#     print(item)

# price = [10, 20, 30]
# total = 0
# for i in price:
#     total = total + i
# print('total: ', total)

##nested loops

# for i in range(4):
#     for j in range(3):
#         print(f'({i},{j})')

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     output = ''
#     for j in range(1, i+1, 1):
#         output += 'x'
#     print(output)

# names = ['san', 'sun', 'son', 'sin']
# print(names[2:])

## largest number in a list
# numbers = [1, 4, 5, 13, 7, 3, 19]
# length = len(numbers)
# max_number = 0
# for i in range(length):
#     if max_number < numbers[i]:
#         max_number = numbers[i]
# print(max_number)

## 2D list
# matrix = [
#             [1, 2, 3],
#             [2, 4, 5],
#             [3, 4, 5]
# ]
# # print(matrix[0][2])
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5,2]
# numbers.append(20)
# print(numbers)
# numbers.insert(3, 10)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# # numbers.pop()
# # print(numbers)
# print(numbers.index(10))
# print(5 in numbers)
# print(numbers.count(10))
# numbers.sort()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# # remove duplicates in a list
#
# numbers = [5, 2, 4, 6, 5, 4, 3]
# uniques =[]
# for num in numbers:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)

## tuples unlike list we cant add and modify the items
# numbers = (1, 2, 3)
# print(numbers[2])

# ## unpacking
# coordinate = (1, 3, 5)
# x, y, z = coordinate
# print(y)
#
# coordinate = [1, 3, 5]
# x, y, z = coordinate
# print(y)

# ## dictionary
#
# customer = {
#     "name": "Sandeep",
#     "Age": 30,
# }
# print(customer["name"])
# customer["name"] = "San"
# print(customer.get("name"))

## exercise
# number = input("Phone: ")
# NumDict = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }
# Output = ""
# for ch in number:
#         Output += NumDict.get(ch, "!") + " "
# print(Output)

# Emoji converter
# msg = input(">")
#word = msg.split(' ')
#Emojis = {
 #   ":)": "smily face",
 #   ":(": "sad face"
#}
#output = ""
#for word in Emojis:
#    output += Emojis.get(word, word) + " "
#print(output)

#print("Hello world")

##fizz_buzz algorithm interveiw

# def fizz_buzz(input):
#     if (input % 15) == 0:
#         output = "FizzBuzz"
#     elif (input % 3) == 0:
#         output = "Fizz"
#     elif (input % 5) == 0:
#         output = "Buzz"
#     else:
#         output = input
#     return output
#
# print(fizz_buzz(31))

# swapping two variables
# x = 10
# y = 11
# x, y = y, x
# print(x, y)

# array
# from array import array
# numbers = array("i", [1, 2, 3])
# numbers.insert(0, 0.5)
# print(numbers)

#sets
# numbers = [1, 1, 3, 3, 4, 6, 2]
# uniques = set(numbers)
# uniques2 ={7, 8}
# print(uniques | uniques2)
# uniques.add(5)
# print(len(uniques))

#comprehension (on sets dicts not on tuples)

# values = {x*2 for x in range(5)}
# print(values)

#unpacking
# first = {"x": 1}
# second = {"x": 2, "y": 10}
# combined = {**first, **second, "z": 3}
# print(combined)

#interview questions find most repeated letter in sentense

# sentence = "this is a common interview question"
# uniques = list(set(sentence))
# print(len(uniques))
# print(uniques)
# count = [0] * len(uniques)
# print(count)
#
# for i in range(len(uniques)):
#     for j in range(len(sentence)):
#         if sentence[j] == uniques[i]:
#             count[i] += 1
# print(uniques)
# print(count)
# print(uniques[count.index(max(count))])

#another method
# sentence = "this is a common interview question"
# char_freq = {}
# for char in sentence:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
# char_freqsorted = sorted(char_freq.items(), key=lambda  kv:kv[1], reverse=True)
# print(char_freqsorted[0])

# handling exceptions
# try:
#     with open('app.py') as file:
#         print(":File opened.")
#     age = int(input("Age: "))
#     xfactor = 10/age
#     except (ValueError, ZeroDivisionError)
#         print("You didnt enter a valid  age.")
#     else:
#         print("No exceptions were thrown.")
#     finally:
#         file.close()

# creating class
#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y
#    def __str__(self):
#        return f"({self.x}, {self.y})"
#    def draw(self):
#        print(f"Point ({self.x}, {self.y})")
#point = Point(1, 2)
#point.draw()
#print(point)
#another = Point(1, 2)
#another.draw()
#print(point == another)
 
# custom container
#class TagCloud:
#    def __init__(self):
#        self.tags = {}
#    def add(self, tag):
#        self.tags[tag] = self.tags.get(tag, 0) + 1
#    def __getitem__(self, tag):
#        return self.tags.get(tag.lower(), 0)
#
#cloud = TagCloud()
#cloud.add("Python")
#cloud.add("python")
#cloud.add("python")
#print(cloud.tags)
#cloud["Python"]
#print(cloud.tags)

# properties
#class product:
#    def __init__(self, price):
#        self.set_price(price)
#    def get_price(self):
#        return self.__price
#    def set_price(self, value):
#        if value< 0:
#            raise ValueError("Price cannot be negative")
#        self.__price = value
#    price = property(get_price, set_price)
#
#product = product(10)
#print(product.price)
 
# inheritance
#class Animal:
#    def eat(self):
#        print("eat")
#class mammal(Animal):
#    def walk(self):
#        print("walk")
#class fish(Animal):
#    def swim(self):
#        print("swim")
#m = mammal()
#print(m.eat())
#print(isinstance(m, Animal))
#print(isinstance(m, object))
#print(issubclass(mammal, object))

# modules
##from sales import class_tax
#from sales import class_tax, class_shopping
###from sales import *
#class_tax()
#class_shopping()

## another way importing module
#from ecommerce import sales
#sales.class_tax()
##import sys
##print(sys.path)
#print(dir(sales))
#print(sales)
#def hello():
#    x = 1
#    y = 3
#    """Print "Hello World" and return None."""
#    print(f' "hello world", {x}, {y}')
#hello()

#Now run this using the debugger (Debug ‣ Debug), 
#press the Step button until the highlighted line 
#reaches the demo(0) function call, then press the 
#Step into to inspect this function. Keep pressing 
#the Step button to execute the next lines. Then, 
#modify x by typing x = 10 in the debugger prompt. 
#You should see x changing in the Variable Explorer
# and when its value is printed as part of the demo()
# function. (The printed output appears between your debugger commands and responses).
#def demo(x):
#    for i in range(5):
#        print("i = {}, x = {}".format(i, x))
#        x = x + 1-
#
#demo(0)
 
 
 # plotting in console
#matplotlib inline
#import matlpotlib.pyplot as plt
#plt.plot(range(10), 'o')
 
 
#a = np.array([1, 2, 3])
#b = np.array([[1], [2], [3]])
#print(a)
#print(b)
#c = np.dot(a,b)
#d = np.multiply(a,b)
#print(c,d)

#
# importing pandas as pd 
#import pandas as pd
#
#A =[[0, 1, 2],
#    [3, 4, 0],
#    [6, 7, 8],
#    [7, 0, 9]]
#
#arr6 = np.arange(15).reshape(3, 5)
#print(arr6)
#print(arr6.shape[0])
#print(arr6[0,1])
#for i in range(arr6.shape[0]):
#    for j in range(arr6.shape[1]):
#        if arr6[i,j] == 0:
#            arr6[i,j] = True
#        else:
#            arr6[i,j] = False
#
#print(arr6)
#print(arr6[1,0])
#print(arr6.iloc[0:3])
##A[A <5] = 0
#print(arr6)
#for item in array:
#    if item == 0:
#        array[item] = 11
#print(A)

#np.array.replace(0,10)


#cancer_data = pd.read_csv(r"C:\Users\insapab\Desktop\Python\The complete python course\cancer dataset.csv")
#print(cancer_data)
#print(cancer_data[0,1])

from pathlib import path
path("C:\Users\insapab\Desktop\Python\The complete python course\san.py")
