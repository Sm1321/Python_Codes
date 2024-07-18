# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:25:13 2024

@author: sm689
"""

file = open("C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata.txt.txt",'r')
str1 = file.read(5)
print(str1)
#from the previous point it start the reading 
str1 = file.read(10)
print(str1)


# another way to open file
with open( "C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata.txt.txt" ,'r') as file:
  xy  = file.read() 

xy





#Modes of opening file::
    
    
file1 = open("C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata2.txt.txt",'w')

file1.write('Hello !\n ')
file1.write('how are you\n')
file1.write('you are doing the task')

file1.close()

file1 = open("C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata2.txt.txt",'a')
file1.write('i am learning python !\n ')
file1.write('it si very easy\n')
file1.write('I am pratising everything')

file1.close()


file1 = open("C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata2.txt.txt",'r+')
str1 = file1.read(15)
print(str1)
file1.write('Good Bye')
file1.close()  




#-----=-=-=-=-=-=-------------------------------------------

file = open("C:\\Users\\sm689\\Desktop\\python_udemy_course\\mydata3.txt.txt",'x')

file.write('i am learning python !\n ')
file.write('it is very easy\n')

str1 = file.read(5)
print(str1)
 




















