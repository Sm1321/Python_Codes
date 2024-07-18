# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:48:59 2024

@author: sm689
"""

l = [10,20,23,4,40,50]

try:
    index = int(input("Enter the index :-"))
    print(l[index])
    print('End of try block')
except:
    print("Invalid index") 
    
    
print("Terminated gracefully/sucesss")     


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=--==-=-=-=-=-=--

l = [10,20,23,4,40,50]

try:
    index = int(input("Enter the index :-"))
    print(l[index])
    print('End of try block')
except IndexError as msg:
    print("Invalid index",msg) 
except ValueError:
    print("enter only integer value")  
except :
    print("some error happend")     
    
    
    
    
print("Terminated gracefully/sucesss")     


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



l = [10,20,23,4,40,50]

try:
    index = int(input("Enter the index :-"))
    print(l[index])
    print('End of try block')
except (IndexError,ValueError) as msg:
    print(msg)  
   

print("Terminated gracefully/sucesss")     




#try - except - else block

print('before try block')

try : 
    a = int(input("Enter the numerator"))
    b = int(input("Enter the denominator"))
    c = a // b
    print('Try Block executed successfully')
except ZeroDivisionError as err:
    print(err)
else:
    print("Division is ",c)


print('Outside try exept -else')



#try except else finally

print('before try block')

try : 
    a = int(input("Enter the numerator"))
    b = int(input("Enter the denominator"))
    c = a // b
    print('Try Block executed successfully')
except ZeroDivisionError as err:
    print(err)
else:
    print("Division is ",c)
finally:
    print('Finally Block')
    

print("outside try - except - else - finally")












#program to print the first 10 even numbers ,using while loop...

count = 1
number = 0

print("First 10 even numbers:")
while count <= 10:
    if number % 2 == 0:
        print(number)
        count += 1
    number += 1


#Python program that prints the first 10 odd numbers using a while loop:

count = 1
number = 1

print("First 10 odd numbers:")
while count <= 10:
    print(number)
    count += 1
    number += 2
    
    
#Write a program to print the first 10 natural numbers.
count = 1

print("First 10 natural numbers:")
while count <= 10:
    print(count)
    count += 1


#Python program to print the first 10 whole numbers

count = -10

print("First 10 whole numbers:")
while count <= 10:
    print(count)
    count += 1





# Python program to print the 3 table using a while loop:
number = 1

print("3 Table:")
while number <= 10:
    result = 3 * number
    print("3 *", number, "=", result)
    number += 1


    