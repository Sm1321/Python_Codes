# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:06:56 2024

@author: sm689
"""

def fun_name():
    return True

fun_name()



def add3(a ,b, c):
    r =a + b + c 
    return r 


print(add3(10 , 15 ,5))


r =add3(1 , 3 , 5)
print(r)  


#they are act as call by referce only 
def add3(a ,b, c):
    print('inside the function',id(a),id(b),id(c))
        
x , y ,z = 10 , 15 , 5
 
print('outside function:-',id(x),id(y),id(z))
 
print(add3(x,y,z)) #it will print NONE if nothing is printed




#position arguments
def net_sal(basic , allowance ,deduction):
    net = basic +allowance -deduction
    return net

print(net_sal(8000,6000,2000))


#keyword Arguments

print(net_sal(deduction=2000,basic =8000,allowance =6000))


#default Arguments

def add(a,b,c):
    return a+b+c
print(add(10,2,5))



def add(a,b=0,c=0):
    return a+b+c

print(add(10,5,2))
print(add(5,7))
print(add(5))
print(add(a=10,b=5,c=2))
print(add(b=5,c=2,a=10))


def additem(item , l=[]):
    l.append(item)
    return l

l1=[2,3,4,5]
print(additem(6,l1))

print(additem(22))
print(additem(24))
print(additem(25))


print(additem(7,l1))
print(additem(8,l1))
print(additem(9,l1))
print(additem(10,l1))
print(additem(31))




def add(a , b , c , d , e , f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f



r= add(f= 9,e=8,a=2,c=7,b=5,d=4)
print(r)



#if we write slash they will become the positional only
def add(a , b,/, c , d , e , f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f

r = add(2 ,5,f=9,e=8,c=7,d=4)
print(r)


#position a ,b
#after slash /-> it will be the any
#after star * -> it will become the keyword
def add(a , b,/, c , d,* , e , f):
    print(a,b,c,d,e,f)
    return a+b+c+d+e+f
r = add(2 ,5,9,8,7,4)
r = add(2 ,5,f=9,e=8,c=7,d=4)
print(r)
r= add(2 , 5,6,7, f=9,e=8)
print(r)


#it will print the varible length 
def functs(*ars):
    print(ars)
    
functs(10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170)
functs(10,20,'hi') 
functs('hello','python','prog',10,20,30)







#Varialbe Length Arguments

def fun2(a,b,c):
    print("the resut:-",a,c,b)
    print(b)
        
fun2(100,200,300) 

 

#multiple Return values
def fun3(a,b,c):
    return (a+1,b+1,c+1)

fun3(1,2,3) 


#  *args will take the variable length arguments,irrespitive to the 
def dfuns(a,b,*argmts):
    print(a,b,argmts)
    
dfuns('a','b',1,'yo','hi ',10,56,96) 


  
def dfuns1(*argmts,a,b):
    print(argmts,a,b)
dfuns1('a','b',1,'yo','hi ',10,a=56,b=96) 
 




def  fun4(a,b,c):
    print(a,b,c)

str1 = 'sky'
fun4(*str1)    


#key word arguments length arguments
def func5(**kwargs):
    print(kwargs)
    print(type(kwargs))
 
def func51(**kwargs):
    for x in kwargs:
        print(x,kwargs[x]) 
        
    
func5(names = 'Ajay',roll =10,addr ='Delhi')
  
func51(names = 'Ajay',roll =10,addr ='Delhi')
      



#mixed Arguments 
def fun6(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
    
    
fun6(0,0,10,20,30,40,50,{'hi':1,'roll':10,'addr':'Delhi'})    





#iterators 
#an iterator is an object that contaion a countable numbers of values
#An iterator is an object that can be iterated upon,meaning that 
                           #you can traverse through all the values
                           
l = [1,2,3,4,5,6]

itr=iter(l)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) 





def f():
    global a
    print(a)
    a = "hello"
    print(a)
a = "world"
f()


print(a) 
print(a) ;print(a) 






#inverting the dictionary

def invert(d):
    newd ={}
    for k,v in d.items():
        newd[v]=k
        
    return newd

d1 = {'a':10,'b':20,'c':30,'d':40}
d2 = invert(d1)
print(d1)
print('\n')
print(d2)  