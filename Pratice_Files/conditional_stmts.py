# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:25:37 2024

@author: sm689
"""
#example program 
a = int(input('enter a number '))

if a < 0 :
    print('nagative')
else :
    print('positive')    
    
    
    
#example program 
marks = int(input('enter the marks :-')) 
if marks > 0 and marks < 100:
     print("marks in between the 0 to 100 ")
else:
    print("not in between the range")
    
person = input('enter the gender of male') 
if person == 'M' or person == 'G':
    print('he is person')
else:
    print('not a person')    
    

#example program
age = int(input('Enter the age :- '))

if age >= 18 and age <= 68:
    print("eligible to work ")
else:
    print('not eligible ') 
    
    
    
    
#example program
maths = int(input('enter the maths marks :-')) 
phy = int(input('enter the maths marks :-')) 
che = int(input('enter the maths marks :-')) 

if maths >= 45 and phy >= 45 and che >= 45:
    print("yes student has passed the 3 subject ")
else:
    print("no not passed 3 sub")    
    
    
    
#example program

username = input('enter the username :=')

if username == 'john'  or username =='smith':
    print('Authorised')
else:
    print('Not Authrised') 
    
    
 #example program 

ch=input('enter any chracter vowel here :-')

if ch == 'a' or ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
   print('vowel it is ')
else: 
    print('not a vowel ')    
    
    
#example program     with elif

john = int(input('enter the age:-')) 
smith = int(input('enter the age:-')) 
ajay = int(input('enter the age:-')) 

if john > smith and john >ajay:
    print('johan age is greater') 
elif smith >ajay and smith > john:
    print('smith age is gretaer than all')
else:
    print('ajay has the greater age')

#example program
john = int(input('enter the age:-')) 
smith = int(input('enter the age:-')) 
ajay = int(input('enter the age:-')) 

if john > smith and john > ajay:
    print('johan age is greater') 
else:
    if smith >ajay and smith > john:
        print('smith age is gretaer than all')
    else:
        print('ajay has the greater age') 


