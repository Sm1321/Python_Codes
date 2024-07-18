# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:45:40 2024

@author: sm689
"""

dict1 = dict()

type(dict1)



dict1['apple'] = 'red'
dict1['mango'] = 'yellow'
dict1['grape'] = 'green'
dict1



for x in dict1.keys():
    print(x)
print('\n')

for x in dict1.values():
    print(x)
    
print('\n')

for x,y in dict1.items():
    print(x,y) 
 
    
 
dict2 = dict(((1,20),(2,40),(3,60)))
dict2 


dict2 = dict(('ab','cd','ef'))
dict2


dict2 = dict(([1,11,12],[2,22,23],[3,33,34]))
dict2

l1= [(1,2),(3,4),(5,6)]
dict2 = dict(l1) # losi to dict convertiong
dict2


l1 =['A','B','C']
l2 = ['apple','ball','cat']

dict3= dict(zip(l1,l2))
dict3
 

s1 = (7,8,9)
str1 = 'AJK'

dict3 = dict(zip(s1,str1))
dict3


l4 =[ 'A','B','C']

for item in enumerate(l4):
    print(item)
    


dict4 = dict(enumerate(l4))
dict4

#Looping out the dictionary

dict1 = {101:'prod',102:'ACCnts',103:'Sales and Marketing',104:'Invertory'}

for x in dict1:
    print(x)
    
    

for x in dict1:
    print(x,dict1[x]) 
        
    
for x in dict1:
     print(x,dict1.get(x)) 
 
        
dict1.keys()    
dict1.values()  
dict1.items()


  
#looping to the values
for k in dict1.keys():
    print(k,dict1[k]) 
 
#looping to the values    
for k in dict1.values():
    print(k)  
  

dict2 = {101:'prod',102:'ACCnts',103:'Sales and Marketing',104:'Invertory'}
    
dict3 = dict2
print(dict3)   

dict3[102]='mangement'  #we can upadte with this
dict3[105]='panning' #with this we can add
print(dict3)


dict3.update(dict1) #adding one dictionaty to another 
dict3

dict3.setdefault(102)
dict3.setdefault(110) #set default it will insert the key with none value
dict3


l2 = [11,22,33,44]
dict3 ={}
dict3.fromkeys(l2)
dict3

dict2.pop(101,'prod') #it will pop out the contents
dict2 
dict2.pop(102)
dict2.clear() 
dict2




#challanges in dictionary
"""
countries = {
             'A':['America','Alasaka','Argentina'],
             'B':['Bhutan','Braizil','Bahrain'],
             'C':['China','Costa Roca','Cuba']
            }

"""
countries = {}

for i in range(4):
    name = input('Enter the country name:-')
    if name[0].upper() not in countries:
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)
        #if again county name addded ,it will add into the existing one
        


print(countries)




def outer():
    def inner():
        print("inner")
    inner()    
        

outer()         





