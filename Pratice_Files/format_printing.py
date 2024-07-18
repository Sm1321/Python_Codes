# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:26:32 2024

@author: sm689
"""

rollno = 10
name = 'Ram'
avg = 86.29714
print('Student name is %s, his roll no is %d  and average is %f'%(name,rollno,avg))

print('Student name is %s' %name )

print('Student name is %10s'%name)  


print('roll number is %8d' %rollno)



print('roll number is % - 8d' %rollno)

print('roll number is % - 8d and' %rollno)



print('%2.5f' %avg)
print('%2.3f' %avg)


a = 22
b = 7
c = a /b
print('Division of {} and {} is {} '.format(a,b,c)) 

print('Division of {0} and {1} is {2} '.format(a,b,c)) 


print('Division of {2} and {1} is {0} '.format(c,b,a)) 



print('Division of {0:10} and {1:15} is {2:2.4} '.format(a,b,c)) 

print('Division of {0:<10} and {1:^15} is {2:>2.4} '.format(a,b,c)) 


print( f'Division of {a:10} and {b:^15} is {c:2.4} ') 





#import re
from re import*
match('a','a').group()

match('a|b','a').group() 

match('[abc]','abcd').group()

match('[abc]','bcd').group() 


match('[abc]+','bcd').group() 

match('[abc]+','abcababadabbcd').group()



