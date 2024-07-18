# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:21:03 2024

@author: sm689
"""
#fractions in math library
import fractions as fc
f1 =fc.Fraction(10,5)
print(f1)
print('{}'.format(f1))


f2 = fc.Fraction(11,2)
print(f2)
print('{}'.format(f2))

list1 = [(10,2),(5,2),(6,4),(12,3)]

for n,d in list1:
    print('{}'.format(fc.Fraction(n,d))) 
    
    
#random  

import random as rd
rd.random() #givens the random number

rd.uniform(1,10) #random number bwteen the 1 to 10,also float

rd.randint(1,10)  #intger numbers from the 1 to 10
rd.randint(2,20) #integer number from the 2 to 20

rd.randrange(1,25,2)
#1 ,3,5,7,9,11, --- 23 



#this seed is used to repeat the random numbers again and again
rd.seed(10)
rd.random() #we get the same random number once agian   




l =[1,3,5,7,8,9,1,0,2,56,3,1]
rd.choice(l) #it will take random number from list

#it will take the random numbers from the number,where (k = 3)
#with 3 elements it will choose the random from the list 
rd.choices(l,k = 3)

#this will shuffle the list
rd.shuffle(l)
print(l)


#it will get the random bimary bits number of 2^3 = 8(0,7)
rd.getrandbits(3)












import math as m
#take uppwer value
m.ceil(12.5)
#take the less value
m.floor(12.9)

#we get the remainder
m.fmod(12,7)
#both are same-> remainder and fmod
m.remainder(12,9)


#sqrt
m.sqrt(29) #it will give the float result

m.isqrt(23) #it will give th inter value as output

m.pow(2,10)# 2^10 ->1024
#gcd of two numbers
m.gcd(1,3)
#permuataion and combination
m.perm(5,2) #5p2->20
m.comb(5,2) #5C2 -> 10

#it will give the product of numbers
m.prod([1,2,3,4,5])


#it wil add the all numberas
m.fsum([1,5,2,3,4])



m.radians(180)


m.degree(30)



m.sin(m.radians(30))

m.cos(m.radians(30))

m.tan(m.radians(45))



m.log(1024)

m.log10(1024)


m.log2(1024)

#pie value
m.pi
#e value
m.e
#nan 
m.nan
#infinity value
m.inf




 
    
 #statics
import statistics as st 
st.mean([1,2,3,4,5])  

st.median([1,2,3])

st.median_high([1,2,3,4,5])

  
st.median_low([1,2,3,4,5,6])


st.mode([1,2,1,2,1,2,1,1,1,1,2,6,1,1])

st.variance([1,2,3,4,5])

st.stdev([3,4,5]) 



import os

os.path.exists('C:\\Users\\sm689\\Desktop\\360_digi_course\\Study_materials')

os.path.isfile("C:\\Users\\sm689\\Desktop\\360_digi_course\\Study_materials   ") 

os.path.isdir(" C:\\Users\\sm689\\Desktop\\360_digi_course\\Study_materials  ")

