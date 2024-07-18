# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:16:39 2024

@author: sm689
"""

class cubiod:
    def __init__(self,l,b,h):
        print(id(self))
        self.bre=b
        self.len=l
        self.hei=h
    def lidareaa(self):
        return self.len * self.bre
    def total(self):
        return 2 * (self.len * self.bre +  self.bre * self.hei + self.len * self.hei )
    
    def volume(self):
        print(id(self))
        return self.len * self.bre * self.hei
    
    
    
#class is an blue print of an object  
    
d1 = cubiod(10 , 5 , 3)
print(d1.volume())
print(id(d1))

d2 = cubiod(20 , 10 ,5 ) 
print(d2.volume()) 
print(id(d2))   

d3 = cubiod(20 , 10 ,5 ) 
print(d2.total()) 
 
        
#self and Constructor    
#self is the referce to the object    
class cubiod:
      def __init__(self,l = 1,b = 2 ,h = 3):
          print(id(self))
          self.bre=b
          self.len=l
          self.hei=h
      def lidareaa(self):
          return self.len * self.bre
      def total(self):
          return 2 * (self.len * self.bre +  self.bre * self.hei + self.len * self.hei )
      
      def volume(self):
          print(id(self))
          return self.len * self.bre * self.hei
      








class rectangle:
    count = 0
    def __init__(self,lent = 1,bre = 1):
        self.lent = lent
        self.bre = bre 
        rectangle.count +=1   
    def perimeter(self):
        return 2 * (self.len + self.bre)
    def area(self):
        return self.len * self.bre 
    @staticmethod #this is static method
    def issquare(lent,bre):
        return lent == bre

        

r1 = rectangle(10,20)
print(rectangle.count) #this will help to find the how many classes will be created

r2 = rectangle(1,2) 

print(r2.issquare(10, 10) )



print(rectangle.issquare(2, 3))




class rectangle:
    count = 0
    def __init__(self,lent = 1,bre = 1):
        self.lent = lent
        self.bre = bre 
        rectangle.count +=1  
    def getLength(self):
            return self.lent
    def setLength(self,l):
            self.lent = l
            
    def perimeter(self):
        return 2 * (self.len + self.bre)
    def area(self):
        return self.lent * self.bre 
    @staticmethod #this is static method
    def issquare(lent,bre):
        return lent == bre

        
r = rectangle(10,5)
print(r.getLength())
r.setLength(15)
print(r.area())

r1 = rectangle(10,20)
print(rectangle.count) #this will help to find the how many classes will be created

r2 = rectangle(1,2) 

print(r2.issquare(10, 10) )



print(rectangle.issquare(2, 3))



#-0--=-=-=-=----=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#inheritance


class rectangle:
    count = 0
    def __init__(self,lent = 1,bre = 1):
        self.lent = lent
        self.bre = bre 
        rectangle.count +=1  
    def perimeter(self):
        return 2 * (self.len + self.bre)
    def area(self):
        return self.lent * self.bre 
    
    

   
class cubiod(rectangle):
    def __init__(self, lent ,bre ,h ):
        self.height = h
        self.lent = lent
        self.bre = bre  #we have to explicitly call the parent class constructor
   #or we can itialize in the child class or
   #initialize with the super() funnction     
        
        
        
        
    def volume(self):
        return self.lent * self.bre * self.height
    



c = cubiod(10,5,3)
print('volume is :- ',c.volume()) 

            