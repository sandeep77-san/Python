
## basic questions
## read the input to list
#a = list(map(int, input().rstrip().split())) ## rstrip removes white spaces
#b = list(map(int, input().rstrip().split()))
### basic operation
#format(2, '.6f')
#round(2.33333, 6)
## strings
#course = 'Python'
#print(course[:])
#print(course[-1])
#print(course[1:])
#print(course[1:3])
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('s'))
# print(course.replace('is', 'are'))
# print('is' in course)

## formatted strings
#first = 'San'
#last = 'Deep'
#msg = f'{first} [{last}] is a coder'
#print(msg)
#msg2 = f'{first}is{last}'
#print(msg2)

# swapping
#x = 1
#y = 2
#x, y = y, x
## ternary operation
#x,y = 40,50
#big = x if x>y else y
#print(big)

## dictionary
#t = {'a', 'b', 'c'}
#d  = {1, 2, 3}
#zip(t,d)
#x = dict(zip(t,d))
#print(x)
#print(x['a'])
#A0 = x
#A1 = range(10)
#A2 = sorted[i for i in A1 if i in A0]
#A3 = sorted[A0[i] for i in A0]
#A4 = [i for i in A1 if i in A3]
#A5 = {i:i*i for i in A1}

###split(), sub(), subn()
#import re
#string = 'sanhsanhsanh'
#pattern = 'san'
#y = string.split(pattern)
#print(string)
#print(y)
#z = re.subn('a', pattern, string)
#print(z)



#for i in range(1,11):
#    print(i)

# for i in xrange(10) ## x range puts one value at a time in RAM
# for i in range(10) ## range puts all values at a time in RAM

# pattern print
#i =1
#while i<=5:
#    print('*'*i)
#    i = i+1
#print('sandeep'*2)

# car game
#started = False
#while True:
#    command = input('> ').lower()
#    if command == 'help':
#        print('''
#start - start the car
#stop - to stop the car
#quit - to exit
#         ''')
#    elif command == 'start':
#        if not started:
#            print('car started..ready to go!')
#            started = True
#        else:
#            print('Hey car already started')
#    elif command == 'stop':
#        if started:
#            print('car stopped.')
#            started = False
#        else:
#            print('Hey car already stopped')
#    elif command == 'quit':
#        break
#    else:
#         print("I don't understand that")
#
#
# find uniques in a list
#numbers = [5, 2, 4, 6, 5, 4, 3]
#uniques = []
#for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
#print(uniques)

# find duplicates in a list
#list = [1,4,5,3,4,5,6]
#print(list[1:])
#duplicate = []
#i = 1;
#for num in list:
#    if num in list[i:]:
#        duplicate.append(num)
#    i = i + 1
#print(duplicate)
#print(list)
            
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

# fibonacci series (0,1,1,2,3,5,8,13,21,34)
#fibonacci = []
#a = 0
#b = 1
#for i in range(20):
#    fibonacci.append(a)
#    a, b = a+b, a
#print(fibonacci)

# fibonacci generator
#def feb(num):
#    a, b = 0, 1
#    for i in range(num):
#        print(a)
#        a, b = a+b, a
#print(feb(10))

# basic python data types
##lists learn about zip 
#list = [1,2,3,4,5,6]
#list.append(56)
#print(list)
##tuples
#tuple = (1,2,3,4)
#tuple.append(45) ## error, we cant change elements in tuples , are immutable, no pop and push operations,static memory allocation
#print(tuple)

#list = [[1,3,2],(1,2,3)]
#list[0].append(4)
#list[1].append(4)
#print(list[0])
#print(list[1])

## dictionary
#dict = {'Name': 'sandeep', 'Age': '24'}
#print(dict)
#print(dict['Name'])
#for values in dict:
#    print(values)
    
#sets
#set = {1,2,3,3,5,6}  
#for i in set:
#    print(i)  # set prints always uniques from a list

# list comprehensions ## for better redability of lists
#list = [1,2,3,4,5,6,7]
#my_list=[]
#for num in list:
#    my_list.append(num)
#print(my_list)
#my_list2 = [num for num in list] #list comprenhension
#print(my_list2)

##shallow and deep copy
#A = [1,2,3,4]
#B = A  ## shallow copy (it copies reference pointer and values in original will be modified if we do any operation on copied variable)
#B.append(6)
#print(A),print(B)
#print(id(A),id(B)) ## same reference pointer
#C = [1,2,3,4]
#D = C.copy() ## deep copy (it just copy the values in it in different location not the reference pointer )
#D.append(7)
#print(C), print(D)
#print(id(C),id(D)) ## 
## random function in numpy
#import numpy as np
#x = np.random.random(5)
#print(x)

## shuffle
#from random import shuffle
#list =[1,2,3,4,5]
#shuffle(list)
#print(list)

## numpy questions
##How to get indices of N max values in numpy array
#import numpy as np
#array = np.array([1,5,4,2,6,3])
#print(array.argsort()) ## print index of sorted values in main array
#print(array.argsort()[-3:][::-1])

## difference between numpy array and list
## list effective in general purpose insertion deltion , concatation etc
# numpy for vectorized operation(matrix operations),FFT, convolutions, linear algebra
## numpy cant store different data types in single array
## scipy is built on top of numpy
#list1 = [1,2,3]
#list2 = [4,5,6]
#print(list1 + list2)
#import numpy as np
#arry1 = np.array(list1)
#arry2 = np.array(list2)
#print(arry1 + arry2)
#arry3 = np.array([1.0,'2',3.0])
#print(arry3)

#how to find indices if a values in array is bigger than threshould
#import numpy as np
#A = np.array([[1,4,3], [4,5,6], [7,8,9]])
#print(A>3)
#print(np.nonzero(A>3))

## chnage column name in pandas
#import pandas as pd
#d = {'name' : ['san', 'deep'], 'Age' : [12, 34]}
#dataFrame = pd.DataFrame(data = d, index = [10,11])
#print(dataFrame)
#dataFrame.rename(columns = {'name' : 'man'}, inplace = True)
#print(dataFrame)
#dataFrame.columns = ['Nam', 'Aggee']
#print(dataFrame)
#
### how to iterate to get index and values 
#for index, row in dataFrame.iterrows():
#    print(index)
#    print(row)

## print only finite values in data frame
#import pandas as pd
#import numpy as np
#d = {'name' : ['san', 'deep' , None], 'Age' : [12, 34, None]}
#dataFrame = pd.DataFrame(data=d)
#print(dataFrame)
#dataFrame = dataFrame[np.isfinite(dataFrame['Age'])]
#print(dataFrame)
#print(dataFrame.isnull())

## read and write binary files using python (usefull for reading image file and sound files)
#import struct
#f = open(file-name, 'rb')
#s = f.read(8)
#f.write(s)


## get the current directory
#import os
#print(os.getcwd())
#os.chdir('C:\Users\insapab\Desktop\Python\Projects\Interview questions\python2')
#print(os.getcwd())
#print(os.listdir(os.getcwd()))

# Functions do specific things, classes are specific things. Classes often have methods, 
#which are functions that are associated with a particular class, and do things associated
 #with the thing that the class is - but if all you want is to do something, a function is all you need
#A class is basically a definition of an Object , function is mere code

## basics of OOPs (class and objects) concentrate more here
#class point:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#    def eat(self):
#        return print('eat')
#P = point(1,2)
#print(P)
#point.eat()
    

#class Car():
#    pass
#
#honda = Car()
#bajaj = Car()
#honda.name = 'City'
#honda.price = 10000
#
#bajaj.name = 'Pulser'
#bajaj.price = 100000
## above old methods in C#, other programming lanquages constructure method is being used where as in python OOPs will be used like below
## in above Car is class, honda, bajaj are objects and name,price are variable for all the objects 

#class Car():
#    def __init__(self, name, price): ## init is the constructure here which intialize values of the variables and self is referenece to ojbect which is going to be called 
#        self.name = name  # reference the oject 
#        self.price = price # reference the oject 
#    # for the object goinging to call for this class, the above constructure says please add above variables to it which generralize the requirement
#        
#honda = Car('City', 100000)
#bajaj = Car('Pulser', 20000)
#print(honda.name)
#print(honda.__dict__)
#honda.cc = 1500
#print(honda.__dict__)

# i want to have price increase based on year for all the model

#class Car():
#    def __init__(self, name, price, year):
#        self.name = name
#        self.price = price
#        self.year = year
#        
#    def price_inc(self):
#        self.price = int((self.price)*(1+ 0.01*self.year))
#        
#    def name_change(self, new_name):
#        self.name = new_name
#
#honda = Car('City', 100000, 4)
#bajaj = Car('Pulser', 90000, 5)
#print(honda.price)
#print(bajaj.price)
#honda.price_inc()
#bajaj.price_inc()
#print(honda.price)
#print(bajaj.price)
#honda.name_change('Ertiga')
#print(honda.name)
#print(honda.__dict__)

## OOPS concepts in python : Inheritance, Encapsulation and Abstraction
# Inheritance 
# A class which inherit attribute or behavoiur method from anothe class called Super class
# A class which inherit from super class is called as sub class
## methods : Single inheritance, multi level inheritance, Hierarcial inheritance, Multiple inheritance
#class SuperCar(Car):   ## SuperCar is Super class and Car is subclass
#    pass
#
#honda = SuperCar('City', 100000, 4)
#print(honda.__dict__)
#
### building class or already exsisting class
#class SuperCar(Car):
#    def __init__(self, name, price, year, cc):
#        super.__init__(name, price, year) ## intead of defining again like Car class we use super.__init__ method
#        self.cc =cc
        
##Encapsulation (securing data by hiding the implementation to user, bind data and code together as single unit)

## Abstraction (hide the implementation details only provides functionality to users car manufactuirng and driver)
        

##multi threading in python

## monkey patching (changing class or module at run time)
#class Car(object):
#    def fun(self):
#        return (print('san'))
#        
#def name(self):
#    return (print('deep'))
#x = Car() ## instantiation of class
#x.fun()
#Car.fun = name
#x.fun()

#import numpy as np
#import pandas as pd
#from numpy.random import rand
#df = pd.DataFrame(rand(100, 1), columns=['value'])
#print(df.head())
#
#
#for i in range(1,4):
#    d = {'value':[1,2,3,4]}
#    dummyframe = pd.DataFrame(data = d)
#    df = df.append(dummyframe)
#    print(len(df))
#    df.loc[(i*10+20):, 'class'] = 'temp'+ str(i)
#    #if i ==2:
#        #df.loc[40:, 'class'] = 'temp'+ str(i)
#    #df.loc[30:, 'class'] = 'temp'+ str(i)
#    
#df.boxplot(column='value', by='class')

#import pandas as pd
#df = pd.DataFrame(rand(100, 1), columns=['value'])
##print(len(df))
##df.ix[:23, 'class']='A'
#df.loc[20:, 'class']='B'
#print(len(df.loc[20:,'class']))
#d = {'value':[1,2,3,4]}
#dummyframe = pd.DataFrame(data = d)
#df = df.append(dummyframe)
#print(len(df))
#df.loc[100:, 'class']='C'
#print(len(df.loc[15:,'class']))
#df.boxplot(column='value', by='class')



from datetime import datetime
curr = datetime.now()
print(curr)
struct_time = datetime.strftime(curr, '%Y/%m/%d %H:%M:%S')
print(struct_time)

from datetime import datetime
datetime_string = '2011/11/27 4:32:51'
datetime_object = datetime.strptime(datetime_string, '%Y/%m/%d %H:%M:%S')
print(datetime_object)