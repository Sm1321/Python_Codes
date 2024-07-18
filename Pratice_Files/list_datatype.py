# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:56:20 2024

@author: sm689
"""
i = 0
list1=[5,6,7,8,9]
while i < (len(list1)):
    print(list1[i])
    i+=1
    
    
    
 l1 = [5 , 6, 7, 8 , 9 ]
 l1.append(10)
 l1.extend([10 , 20])
 print(l1)  
l1.insert(0,3)
l1.insert(1,4)
print(l1) 
print(l1)


l1.append(10)
l1.extend([20 , 30]) #extend will add the multiple values
l1.extend([40 , 50])
print(l1) 


l1.insert(0,3) #first place for the index value and other is the ele
l1.insert(1,4)
print(l1)


print(l1[len(l1):])
print(l1[len(l1)-3:])
l2 = l1.copy()
print(l1) 
print(l2)



l1 = [5,6,7,8,9]
l1.pop()
l1.pop()
print(l1)  


l1 = [5,6,7,8,9]
l1.pop()
l1.pop(2)
l1.pop()
print(l1) 


l1 = {5 , 6 ,7 ,8 ,9}
del l1[3]
print(l1)

l1 = {5 , 6 ,7 ,8 ,9}
l1.remove( l1[3])
print(l1)


l1 = [5 , 6 ,7 ,8 ,9,101,11,12,13,14,15]
l1.remove( l1[3]) #you can use the remove() 
del l1[3] #use can use del keyword 
print(l1)


del l1[0:2]
print(l1)


l1.clear()
print(l1)



l1.clear()
print(l1)
#diff syntax to delete the list
del l1[:]
print(l1)
l1.clear()
print(l1)
del l1[:]
print(l1)
l1[:] = [] 
print(l1)




l1 =[ 5,6,7,5,8,9,10,6,6,2]

print(l1.index(8))
print(l1.index(6))
print(l1.index(6,2))
print(l1.index(6,3)) 
print(l1)
print(l1.index(8))
print(l1.index(6))
print(l1.index(6,2)) #here,2 means after the 2nd index it will start
print(l1.index(5,1))
print(l1.index(5,2,6)) 


l1 =[ 5,6,7,5,8,9,10,6,6,2]
print(l1.count(8))  
print(l1.count(5))
print(l1.count(6))

l1 =[5,6,7,5,8,9,10,6,6,2]
l1.reverse() 
l1

 
print(l1.revese())
print(l1.reverse())

l1 =[ 5,6,7,5,8,9,10,6,6,2]
l1.sort()  
l1
print(l1.sort(revese=True))



l1 =[ 5,6,7,5,8,9,10,6,6,2]
l1.sort()
l1


l1 =[ 5,6,7,5,8,9,10,6,6,2]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)


l1 =[ 5,6,7,5,8,9,10,6,6,2]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

print(l1.reverse())
print(l1[:-1]) 


l2 = ['yy','jj','mm','BB','aa','ZZ']
l2.sort()
print(l2)
print(l2.sort(key = str.lower))
l2 

sorted(l2)



l1 = [5 , 6, 7, 8 , 9 ]
l1.append(10)
l1.extend([10 , 20])
print(l1)


#List 
l1 = [] #empty list
for x in range(10):
    l1.append(x)
    
print(l1)   

 #list comprehensions
 l2 = [ x for x in range(12) ]
 print(l2)
 
 
 l3 =[x**2 for x in range(1,6)]
 print(l3)
 
 l4 = [x for x in(10,20,3,1,5,6,7,8,9,21) if x %2==0]
 print(l4)
 
 l5 = [x.lower() for x in 'Python']
 print(l5)
 
 l6 = [x for x in ('abcdefghijklman5783#%3U&5') if x.isalpha() ]
 print(l6)
 
 
#l7 =['ajay','hare','ram','krishna']async def func_name(*args, **kwargs):
passdata = input('Enter names:-')
l7 = passdata.split()
print(l7)


l7 = [input('enter the names:-').split()]
l7



#nested list

a = [[1,2,3],[4,5,6],[7,8,9]]
b =[[9,8,7],[6,5,4],[3,2,1]]
c = []

for i in range(len(a)):
    s =[] #we took the empty list for storing the resultant
    for j in range(len(a[0])):
        s.append(a[i][j]+b[i][j])
        
    c.append((s))

print(c) 

#challange on list
#calculte the salary ,weekly working hours given in a list

works_hours = [int(x) for x in input('Enter hours per day in entire week,separeted by space:-').split()] 
wage = int(input('Enter the hourly wage:-'))
total = sum(works_hours)

salary = total +wage

print('salary is:-',salary)
 


#challange on list
#checking and removing if there is any duplication in alist


 l1 =[3,5,7,9,3,6,5,2,3,7,10]
 l2 =[]
 
 for x in l1:
     if x not in l2:
         l2.append(x)
         
print(l1)         
print(l2)




#using the one list only ,remove the duplicates
 l1 =[3,5,7,9,3,6,5,2,3,7,10]
 
 for x in l1:
     if l1.count(x)!=1:
         l1.reverse()
         l1.remove(x)
         l1.reverse()
         
print(l1)         


#challange -2
#usnig the list
#conctenate all intger from the list to a single number


l1 =[3,5,10,7,12]
s1 =''
for x in l1:
    s1+=str(x) 
    
print(int(s1))     




#challnge-3
l1 = ['pizza','nug','hotdog','noodles','pasta','burger']

l2 = ['burger','hotdog','noodles','pasta','nug','pizza']

index1 = 10
index2 = 10


for i in range(len(l1)):
    indx = l2.index(l1[i])
    

   
    if i + indx < index1 + index2:
        index1 = i
        index2 = indx
        
        
print(l1[index1],index1+index2)        



#challange-4
#overlapping elements of the two lists

l1 = [10,15,6,9,12,8,4]
l2= [14,6,19,4,7,10,11]

l3 =[]
for x in l1:
    if x in l2:
        l3.append(x)
        

print(l3)


#challange-5
#find the number of occurences of each item

l1 = ['A','B','C','D','E','A','B','E','B','D','E']

result = []

for item in l1:
    if item not in result:
        result.append(item)
        count=l1.count(item)
        result.append(count)
        
        
print(result)
 



#nested list,addition of a matrix

a = [[1,2,3],[4,5,6],[7,8,9]]
b =[[9,8,7],[6,5,4],[3,2,1]]
c = []

for i in range(len(a)):
    s =[] #we took the empty list for storing the resultant
    for j in range(len(a[0])):
        s.append(a[i][j]+b[i][j])
        
    c.append((s))

print(c)




#transpose of a matrix 
l1 =[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = []

for i in range(4):
    s=[]
    for j in range(3):
        s.append(l1[j][i])
        
        
    l2.append(s)
        
print(l2)        







        






  

