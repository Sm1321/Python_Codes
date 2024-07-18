# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:19:39 2024

@author: sm689
"""

count = 0
while count < 10:
    print('hi')
    count+=1
    
    
    
count = 0
while count < 10:
        print(count + 1 ,'hi')
        count+= 1
        

# it will add the summation of all the digits of the
#given number
n = int(input('enter a number :-')) 
r = 0
while n > 0:
    r = n % 10 + r #taking the reminder of the number
    n = n // 10   #floor division     
print(r) 


#multiplication table 

n = 5
cnt = 1
while cnt <= 10:
    print(n,'X',cnt,'=',n*cnt)
    cnt+=1
    




#count the number of digits in a number

n = int(input('enter the number :-'))
c = 0
while n > 0:
    n//=10
    c+=1
print(c)     
 

#reversig the number
n = int(input('enter the number :-'))

rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev *10 + r
    
print('Reverse the number is :- ') 
print(rev)  


#palindrome of a number
n = int(input('enter the number :-'))
org_num = n
rev = 0 
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev *10 + r

if rev == org_num:
    print('it is palindrome')
else:
    print('no not a plaindrome')
    
    
    
    
    
    
 # sum of numbers program


num_of_nos = int(input('Enter count of the  number of number ')) 

sum_ = 0
count = 0
 

while count < num_of_nos:
    n = int(input('Enter a number'))
    sum_ = sum_ +n
    count =count + 1
print(sum_) 


#print the positve and negative number 

nums_of_nos = int(input('Enter the number of number ')) 

Psum = 0 
Nsum = 0
count = 0
while count < num_of_nos:
    n = int(input('enter a Number '))
    if n > 0:
        Psum = Psum + n
    else:
        Nsum = Nsum + n
    count=count + 1 

 
print('positive sum is :',Psum)
print('positive sum is :',Nsum) 
    


#find the maximum numbers , in the given list of numbers 
numbr = int(input('enter the number')) 
max_nbr = 0
count=0
while count < numbr - 1: 
    n=int(input('enter the number '))
    if n > max_nbr:
        max_nbr = n
    count+=1
    
print(max_nbr)    
    
    
               



import random
n= random.randint(1,10) 
guess = 0

while guess != n:
    guess=int(input('Guess a number')) 
    
    
    if guess < n:
        print('It is smaller') 
    elif guess > n:
        print('It is larger') 
    else:
        print("correct guess ")
        
    
#infinte loop program

#using of the break statment
while True :
    n = int(input('Enter e number'))
    if n > 0 :
        print('Positive')
    elif n < 0:
        print('Negative') 
    else :
        break 
    
   #usimg of the continue statment 
count = 0
while count < 10 :
    n = int(input('Enter the number ;-'))
    if n % 3 == 0 :
        continue
    print(n)
    count += 1
    
    
    
    
    
 #uisng the pass statment
count = 0
while count < 10 :
    n = int(input('Enter the number:-'))
    if n % 3 == 0 :
        pass #pass means do nothing ,
    else:    
        print(n)
    count += 1 
    
    
  #else site example-2   
count = 1

while count <= 10:
    print(count)
    count+=1
else:
    print('printed all 10 numbers')
    
    
    print('end of the program')

   
  #else site example-2  
    
count = 1

while count <= 10:
    print(count)
    count+=1
    if count > 50:
        break
else:
    print('printed all 10 numbers')
    
    print('end of the program')
  
      
 # for loop 

msg ='hello'
for x in msg :
    print(x)
    
    


range(10) # 0 to 10

range(5,10) # 5 6 7 8 9


range(1,10,2) # 1 3 5 7  9 


range(10 , 0 ,-1) # 10 9 8 7 6 5 4 3 2 1 


for i in range(1,10): # 1 to 9
    print(i) 
   
    
for i in range(5,10):
    print(i)    
    


for i in range(9,10):
    print(i) 


# print multiplication table using python

n=5
for count in range(1,10):
    print(n,'X',count,'=',count*n)
    
 #factorial using the given number
f=1
n = 5
for c in range(1,n+1):
    f=f*c 
    
print(f)     
 
# Ap series using for loop


a= int(input("Enter the intial number ")) 
d = int(input("enter the common diffrence foe series")) 
n = int(input("enter thr upto thr nth number ")) 

for t in range( a ,a + n * d , d):
    print(t)




#print n terms of fiboancci series 
a = 0
b = 1
n = int(input('enter the number : -')) 
for i in range(n):
    print( a ) 
    c = a + b
    a = b
    b = c


#find the factors of a number 
n = int(input('enter the number : -')) 
for i in range(1 , n + 1 ) :
    if n % i == 0:
        print('factors are :-',i)
        

#find the prime or not
count = 0 
n = int(input('enter the number : -')) 
for i in range(1 , n + 1 ) :
    if n % i == 0:
        count += 1

if count == 2:
    print('it is prime')
    
else:
    print('it is not prime')    





# for loop with else 
for i in range(0,10):
    print(i)
else:
    print('for completed properly')  
    
    
#for loop with pass
for i in range(0 , 10 ): 
    pass #it will do nothing ,it will pass to the next step
 
print('Program ended') 
    

#for with use of the continue

for i in range(0 , 10 ): 
    if i % 5 == 0:
        continue
    print(i) 


 
# nested loops
for i in range(0 , 5):
    for j in range(0 , 5):
        print('(', i , j ,')',end=' ') 
    print("")    
    
    
  #nested for loop     
for i in range(0 , 5):
    for j in range(0 , 5):
        if i <=j:
            print('*',end=' ') 
    print("")    
        
    
   #for loop using the string 
s1 = 'abc'
s2 = 'xyz'
for i in s1:
    for j in s2:
        print(i,j,end='')
    print('') 
    
    
    
#prime numbers from  1 to 100
n = 100
count = 0
for i in range(1 , n+1):
    if n % i == 0:
        count+=1    
    if count == 2:
        print(n)
        
        
        
#start patterns using loops
for i in range( 0 , 5 ):
    print('* ' * 5)        
        
for i in range(0 , 5):
    for j in range(0 , 5):
        if i >= j:
            print("* ",end='')
        print('')    
    
 #with one loop also we can print the star's   
for i in range(5 , 0 , -1):
        print('* ' * i)
        
        
#match case with simple if and else..
day = int(input('Enter Day number')) 
if day == 1:
    print('sunday')
elif day == 2:
    print('tuesday')
elif day == 3:
    print('wednesday')    
elif day == 4:
    print('Thyrsday')
elif day == 5:
    print('Friday')
elif day == 6:
    print("Sat")
else day == '7':
    print('holiday')
    
 #match case   
day = int(input('Enter Day number')) 

match day:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesay')
    case 5:
        print('thusday')
    case 6: 
        print('friday')
    case 7: 
         print('satday')
    case _:
        print('holiday') 
        
        
        
        
        
        

   
        
   



    
        
    