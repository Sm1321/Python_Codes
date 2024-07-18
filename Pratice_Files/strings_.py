# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:30:34 2024

@author: sm689
"""


s = 'hello'
s2 = 'e_/\#()'

type(s)
print(s)
print(s2) 

s1= 'hello'
s2 = input('Enter the string : -')
print(len(s2))
len(s1)

for i in s1:
    print(i)
    
#to traverse the string using for loop
for i in s1:
    print(i,end='')
    
 
    
s5 = "john's" #this will work
s4 = 'john's ' ##this will won't work

s6 = ''' hello 
   how are you '''  
         
print(s5)
print(s6)         



#operators on the string



s1 = 'hello'
s2 ='world'
s3 = s1 + s2
print(s3) 


s3 = 'hello world'
print(s3) 

s5 = 'hello' + str(15)
print(s5)


s6 = 'how' + 'are' + 'you'
print(s6)


s7 = 'hi' * 2
print(s7)  

s7 = 'hi' * 2.8  #it will not work , here
print(s7)   

s8 = 'hello world'
print(s8[-3])
print(s8[:-5])
print(s8[3])
print(s8[6])
for x in s8 :
    print(x,end='') 
       
print(s8[:8])
#revrsing the string using loop 
for i in range(len(s8) -1 , -1 , -1):
    print(s8[i])

 
for i in range( 0 , len(s8), 2): #skipping the index, places of size 2
    print(s8[i])


#slicing the string

 s1 = 'hello world'
 
print(s1[ : : 8]) 
print(s1[0 : len(s1) :1])

print(s1[0 : len(s1) :2]) 

print(s1[ : : 1])

print(s1[ : : ]) 

print(s1[3::]) 



print(s1[6 : 8 :]) 
 
print(s1[: : 2]) # it will print alternately
# sciling will escape the characters also

print(s1[: : -1])

print(s1[ -1 : - len(s1) -1  : -1])

print(s1[ -1 : : -1])

print(s1[ -1 : : -2 ]) 


print(s1[-1 : : -2])




s2 = 'hello world'
print('h'  in s2)
print('e'  in s2)
print('L'  in s2)
print('d' in s2)
print('o'  in s2)
print('W'  in s2)

s2 = 'hello world'
print('h'  not in s2)
print('e'  not in s2)
print('L'  not in s2)
print('d' not in s2)
print('o'  not in s2) 
print('W'  not in s2)





s = "hello how are you"
type(s) 

dir(s)
dir(int)


help(s.endswith)    

s1 = 'hello'
help(s1 . find)


#string Methods
s = 'hello, how are you'

print(s)

print(s.find('o')) 
print(s.find('how'))  
print(s.find('k'))  #if the character is not present then it 
                    # it will return the -1
print(s.find('are'))   
   


print(s.find('o',5)) # find the occurance of the next  'o' in string

print(s.find('h',8))   

print(s.find('e',5)) 


print(s.rfind('o'))
 
print(s.find('o', 0 , 15))  

print(s.index('o')) 


print(s.index('k')) 

#index will through the error if we don't have the char in it

print(s.rindex('o')) 

print(s.rindex('k')) 

print(s.rindex('o',0,15)) 



print(s.count('me')) 

print(s.count('my'))

print(s.count('how'))

print(s.count('o'))
print(s.count('y'))
print(s.count('h')) 


s='python'
print(s.ljust(3))  

print(s.rjust(10)) 

print(s.center(10))

print(s.center(10,'*')) 

print(s.center(20,'+')) 



s1 = s.rjust(20, '.')
print(s1) 



#remove the spaces 


s = '     python'
print(s)  



print(s.rstrip())
  print(s.strip())  
  
  
  
  
s1 = '....   ...  ++aaapython'
print(s1.lstrip() )
  
print(s1.rstrip('.'))
  
print(s1.rstrip('.+'))




s = "hello dear"
print(s.capitalize() )


s1 = s.capitalize()
print(s1)



s = 'HELLO dear'
print(s.capitalize()) 


s = 'HELLO dear'
print(s.lower())  

s = "hello dear"
print(s.lower() )



s = 'HELLO dear'
print(s.upper())  

s = "hello dear"
print(s.upper() )


s = "hello deAr"
print(s.upper() )





s = "hello deAr"
print(s.title() )

s = "hello dEAr"
print(s.title() )



s = "hello deAr"
print(s.swapcase() )

s = "hello dEAr"
print(s.swapcase() )


s = "hello how are YOU deAr"
print(s.casefold() )

s = "hello dEAr"
print(s.casefold() )



s1 = 'hello'
s2 = 'HELLO'

s1.lower() == s2.lower()  



#string methods --> Bool type


s = 'HELLO'
s.isupper()

s.islower()

s.istitle() #starting of the every letter must be the capital


s.islower() 




s1 = 'JiToPythonMowa'
print(s1.isupper())
print(s1.islower())
print(s1.istitle())

s2= 'hello1232pythonnum'
print(s2.isalnum())  #it shuold contain only the alphabet and numbers only
print(s1.isalpha()) #it should contain only the alphabet,not evern spaces and numbers
print(s2.isspace()) #it should contain only the spaces
 
s3 ='     '
print(s3.isspace())

s4 = '$@&)("12^Ab@f '
print(s4.isascii())


s5 ='\u03b2\u03b2\u03b3'
print(s5.isascii())
print(s5.isalnum()) 
print(s5.isalpha()) 
print(s5.isdigit()) 
print(s5) 


s6 = 'hello how are you'
print(s6.isprintable())
print(s6.isidentifier())

s6 = 'for'
print(s6.isprintable())
print(s6.isidentifier())


s6 = 'ad " " ok '
print(s6.isprintable())
print(s6.isidentifier())



s7 = '1024'
print(s7.isdecimal())
print(s7.isdigit()) 
print(s7.isnumeric())


 
s7 = '8\u00b2' #this is the  8 square in unicode
print(s7)
print(s7.isdecimal())
print(s7.isdigit()) 
print(s7.isnumeric())

s7 ='5\u00bd'
print(s7)
print(s7.isdecimal())
print(s7.isdigit()) 
print(s7.isnumeric())



#methods () 
s = 'python is very easy'

print(s.startswith('python'))
print(s.startswith('py'))
print(s.startswith('is',7))
print(s.startswith('is')) 
print(s.endswith('easy')) 
print(s.endswith('y')) 


print(s.removesuffix('ery'))         
print(s.removeprefix('py'))
print(s.removesuffix('sy')) 


s = 'python programming'

print(s.removeprefix('py'))         
print(s.removeprefix('java'))
print(s.removesuffix('ing')) 



s = 'python is very easy'
print(s.partition('is'))
print(s.partition('s')) #it will break the string into mutiple
print(s.rpartition('s')) 




# Methods
print(s.replace('is','will'))
s = 'a-b-c-d-e'
print(s)
print(s.replace('-',':-'))
print(s.replace('-',':-',2))
print(s.replace('k','m')) 

s = 'abcd@gmail.com'
print(s.replace('gmail','yahoo'))




s1 = 'xyz'
s2 ='abc'
print(s1.join(s2)) #axyzbxyzc,, blw it will join



l1 = ['john','smith','ajay']
s1 = '-'
print(s1.join(l1))


l1 = ['john','smith','ajay']
s1 = ','
print(l1)
print(s1.join(l1))


s ='john smith ajay'
print(s.split('h')) 
  
s ='john smith ajay'
print(s.rsplit('h')) 
  


s ='john\n\n smith\n\ ajay'
print(s.splitlines()) 
  
print(s.split())

#sort the string using sorted() method
str1 ='bncnqscinjvepkveax'
s1 =sorted(str1)
print(s1)
s2 = ''.join(s1)
print(s2) 


#display data in given format
item = input("enter the item :-") 
price = (input("Enter the price:-"))
total_len = len(item)+len(price)
print(total_len)
dots ='.'* (25 - total_len)
print(item+dots+price) 



#check if the password and confirm password are same

pass1 = input('Enter the password:-')
pass2 = input('Enter the password agian:-')
if pass1 == pass2:
    print("Yes they are Matching")
else:
    if pass1.casefold() == pass2.casefold():
        print("Please check for the cases and try again")
    else:
        print("NO they are Not Matchinh Try them Again")
        
    

#credit card number

cardno = input("Enter thr cardno :-")
lastdigits = cardno[15 : :]
four = '*' * 4 + ''
display_no = four * 3 +lastdigits
print(display_no) 




#checking a string is palindrome

s1 = input("enter the string :-")
rev = s1[ : : -1]
if s1 == rev:
    print('Palindrome')
else:
    print("not a palindrome ")    


#Anagram of the string

s1 = input("Enter the number :- ")
s2 = input("Enter thr other string:-")
if len(s1) != len(s2):
    print("NOt anagram" )
else:    
     for x in s1:
            if x not in s2:
                print("nOt anagram")
                break;
     else :
         print("Anagram !!!") 
                
                
                
                