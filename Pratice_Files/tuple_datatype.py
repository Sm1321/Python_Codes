# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:01:40 2024

@author: sm689
"""

t1 = ('jack',38.5,45,5+9j,45)
print(t1)

print(type(t1))
print(t1[2])

#error wheb we try to update
t1[2]=85 #assigment operations will be not allowed

t1 = (1,2,3,4,5)
print(t1)

t3=(10)  #thus will be the integer 
print(t3)
print(type(t3))


t3=(10,)  #if we use the commas ,then it will be the tuple 
print(t3)
print(type(t3))




t4 =tuple(1,2,3,4,5) # we have to use the double sruare brackets 

print(type(t4))
print(t4)


t4 =tuple((1,2,3,4,5))
print(t4)


t5 = tuple([1,2,3,4,5])
print(type(t5))
t5

t6 = tuple('Python')
print(type(t6))

t7 = tuple((1,2,3))
print(type(t7))

t8 = 10,20,30,40 #this is a packing a tuple  
#it is also a tuple..
print(type(t8))


a =10
a,b=10,28
a,b,c,d=10,20,30,40


a,b,c = 'SKY'
print(a)
print(b)
print(c)

a,b,*c=t1 #to unpack more number of variables in the * 
a

 

#tuple comprehension& Methods

l1 = (x for x in range(10))
print(l1)


t1 = (x for x in range(10))
print(t1)


t1 = tuple(x for x in range(10)) #we have to keep in  the tuple comprehension
t1

t3 = (*(x for x in 'python'),)
t3


#Tuple Iteration and operators

t1 = ('jack',45,3806,False,5+6j,'joll',45)
for x in t1:
    print(x)
    
    
t1[3:len(t1):-1]    

t1[-3:-len(t1):-1]  

#tuple concatenation
t2 = (1,2,3)
t3 = (4,5,6)

t2 + t3

t1+tuple([4,5,6])

t2 * 3

temp = t1*3 
temp



