# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:41:22 2024

@author: sm689
"""


s1 = {1,2,3,4,'jack',3.4,'ram'}
print(s1)
s1[0]

print(type(s1))

s2 = set((1,2,3,4,5))
print(s2) 

s3 = set('Python')
print(s3)
#unordered 
#no duplicates
#heterogeneous
#growable
#mutable

s2.add(100)
s2.add(200)
print(s2)



A= {1,2,3,4,5}
B = {5,7,9,10}
C = {1,2,3,4,5,6,7,8,9,10}
A1= {1,2,3,4,5}

D =A.union(B)
print(D)
E = A.intersection(B)
print(E)
E1 = A1.intersection_update(B) #it will update the value in the A1
print(E1)
print(A1)
F=A.difference(B)
print(F)
G= A.difference(B)
print(G)



a1=A.issubset(B)
print(a1)

a11=A.issuperset(B)
print(a11)

b1 = A.isdisjoint(B)
print(b1)


dir(set)




#set operations

a={1,2,3}
b={4,5,6,3}
print(a|b)
print(a&b)
print(a-b) 
print(a^b) #symmetric diffrence,but take all elemnts except common ele
print(a<b) #like a subset 

print(a <= b)

print(a > b)

print(a >= b) 

print(a == b)

print(a!=b) 




#set methods
s1 = {10,20,30,40,50}

print(len(s1))
s1.add(100)
s1.add('mux')
s1.add('new')
print(s1)
s2 =s1.copy()


print(s2)
print(len(s2))
s1.update((5,6,7))
print(s1)


s1.add((70,80))
print(s1)
s1.add(70)
print(s1) 

s1.pop()
s1.pop()
s1.pop()
print(s1)

s1.discard(10)
s1.discard(70)
s1.discard(80)
s1.discard((70,80,90))
print(s1)

s1.remove('mux')
print(s1)
 


#set comprehesnions

s =set() #this is the set

for i in  range(10):
    s.add(i)
print(s)

#insted of this we canm also use
#set comprehesion also
#below

s1 ={x for x in range(10)}
print(s1)

s2 = {x**2 for x in range(25)}
print(s2)

s2 = {x**2 for x in [-2,-1,0,1,2 ]}
print(s2)

s3 = { x for x in (10,5,7,8,12,3) if x%2 ==0}
print(s3)


s4 = {x.upper() for x in 'philippines'}
print(s4) 



