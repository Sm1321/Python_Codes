# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 08:15:26 2024

@author: sm689
"""

import re

txt = 'rain is the spain'
x =  re.search("in",txt)
print(x)


d = 'hi'
pattern = 'hi hello nameste python programming language'
#it take sthe input parameters as ,search string and the pattern string 
x = re.search(d, pattern)

print(x)

#eg :- 2 
#it gives the index from starting to end of word ->re.search()
x = re.search('mowa','enti mowa ela unav?')
print(x)

#eg:-3
x = re.search("cow", "A cat and a rat can't be friends.")
print(x)

#re.search(exp,string)
# and the most often used method of this module. re.search(expr,s) checks a string s 
# for an occurrence of a substring which matches the regular expression expr. 

print(type(x))


"r.at"
x1 = re.search(' .at','at the en of,cat has a bat with a rat and wait the at what')
print(x1)
#r is used to avoid the backslash in patterns



if x1: #if we get none it will excurte the else ,ii found if execute
    print('Found',x1.group())
else:
    print("not found")





import re
a = " charlie and the chocolate fact"
b = " ayushi1.jain@gmail.com"
c = 'hello'
d = 'xyz,yz,xyyz,xxzzy,zyx,xxy'

match = re.search(r'\.',b ) 
print(match)

match = re.search(r'[a]',b ) 
print(match)


import re
string = 'abaabbaa'

match_iter = re.finditer('ba',string)

for match in match_iter:
    print(match )
    print(match.group())
    
    
     
import re
string = 'abaabbabbabaaabadabaa'

match_iter = re.findall('ba',string)
print(match_iter)

for match in match_iter:
    print(match )


#^->os ued to exclude the like a negation
pattern = r'[^a-z 0-9]'
data = "the priCE is 1024"

match_iyer = re.findall(pattern,data)

print(match_iyer)

#or
for match in match_iyer:
    print(match)
    
    

pattern = r'[a-z]'
data = "the priCE is 1024"

match_iyer = re.findall(pattern,data)

print(match_iyer) 
    
    
import re 
password = input("Enter the password:-")

patern = '[0 - 9 A-Z]'
if re.findall(pattern,password):
    print("valid passsword")     
else :
    print("invalid password")
    
   
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\
# The special sequences consist of "\\" and a character from the following list:
# \d  Matches any decimal digit; equivalent to the set [0-9].
# \D  is not of \d. It matches any non-digit character; equivalent to the set [^0-9].
# \s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
# \S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
# \w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
# \W  Matches the complement of \w.
# \b  Matches the empty string, but only at the start or end of a word.
# \B  Matches the empty string, but not at the start or end of a word.
# \\  Matches a literal backslash.
      
   
 #\d -> Matches the any digit character    
import re
text = "hello my phone number is  1230"
pat =r'\d'

ans = re.findall(pat,text) 
print(ans) 
  



#\D:- matches the any non-digit character
import re
text = "hello , my 1230"
pat =r'\D'

ans = re.findall(pat,text) 
print(ans) 

  

#\w:- matches the any word character
import re
text = "hello my phone number is  1230"
pat =r'\w'

ans = re.findall(pat,text) 
print(ans) 

#\W:- matches the any non-word character
import re
text = "hello my phone number is  1230 @56"
pat =r'\W'

ans = re.findall(pat,text) 
print(ans) 


#\s:- matches the whitespace character equivallent to \n,\t,\f,\v
import re
text = "hello my phone number is  1230 @56"
pat =r'\s'

ans = re.findall(pat,text) 
print(ans) 
 

#\S:-The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
import re
text = "hello my phone number is  1230 @56"
pat =r'\S'

ans = re.findall(pat,text) 
print(ans) 
 


# \b  Matches the empty string, but only at the start or end of a word.
import re
text = "hello my phone number is  1230 @56"
pat =r'\b'

ans = re.findall(pat,text) 
print(ans) 
  

  
# \B  Matches the empty string, but not at the start or end of a word.
import re
text = "hello my phone number is  1230 @56"
pat =r'\B'

ans = re.findall(pat,text) 
print(ans) 



# \\  Matches a literal backslash.
import re
text = "hello my phone number is  1230 @56"
pat =r'\\'

ans = re.findall(pat,text) 
print(ans) 




# . Matches all the characters.
import re
text = "hello to the regular expression topic"
pat =r'.'

ans = re.findall(pat,text) 
print(ans) 

#dot(.)
import re
data = "hello"
pattern = r'.'
matches = re.finditer(pattern,data)
for match in matches:
    print(match)
    
    


import re
data = "hello hi  hit hell geloeelell"
pattern = r'l+'
matches = re.finditer(pattern,data)
for match in matches:
    print(match)
    
import re
data = "hello hi  144cwsfegr144 eg1 44 dgfe544 e65sx4494 l"
pattern = r'\d+'
matches = re.finditer(pattern,data)
for match in matches:
    print(match)
    
    

import re
data = 'My name is mohan my email id is siddulamohan1321@gmail.com and my  another email id is sm689839@gmail.com'
pattern = r'\w+@\w+\.\w+'
ans= re.findall(pattern,data)
print(ans)




#uisng the ?
import re
data = 'colour and color are same color'
pattern = 'colou?r' #here u is not mandatory to take

matches = re.finditer(pattern,data)
for match  in matches:
    print(match)

matches= re.findall(pattern,data)
print(matches)


#check the valid uels using the ?

import re
pat = r'https?://\w+\.\w+'
urls  = ['http://Exam10ple.com','https://example.org','htttp://fileserver.net']

for url in urls:
    if (re.match(pat,url)):
        print("valid url:-",re.match(pat,url))
    else:
        print("not")



# |(pipe symbol)


import re
pattern = r'cat|dog'
text = "i have a cat and dog."
matches = re.findall(pattern,text)
print(matches)

import re
pattern = r'\d+ |\w+@\w+\.\w+'
data = 'sanket:-963258741 \n shant@gmail.com'
matches = re.findall(pattern,data)
print(matches)


    

#quantifers:-


#Ex:-
#+ -> 1 or more occurances
#* ->0 or more occurances
#{3} -> exactly 3 occurances
#{a,b} ->to finf the range of occurances
#{2,4}-> 2 to 4
#{2,} ->minimum 2 occurences (>=2)
#{,2} ->maximum 2 occurances (<=2)
 

import re
data = "90234$56741 56"
pattern = r'\d{2,5}' #two occuramces and 5 occurances
print(re.findall(pattern,data))



import re
data = "90234$56741 639 12"
pattern = r'\d{3,}'  #minimum 3 occurancea and more also
print(re.findall(pattern,data))

pt1 = r'\d{2}' #exactly two -two occurances
print(re.findall(pt1,data))


pt2 = r'\d{2,}' #minimum  2 ocuurances allowed
print(re.findall(pt2,data))



pt2 = r'\d{,4}' #starting with 0 occurance  and upto  4 ocuurances allowed
print(re.findall(pt2,data))

pt4 = r'\d{,3}' #starting with 0 occurance  and upto  4 ocuurances allowed
print(re.findall(pt4,data))


#we can use regular exp in 2 ways
#1.directly [patter(as string)]
#by using the expression objects

#by using the expression objects
#re.compile()
#re.compile(pattern,flags) ->flags are optional
import re
pattern =re.compile(r'python') #pattern to search
data = 'python is very poweful and its has the lot of features'

match = re.match(pattern,data)
print(match)
print(type(match))







import re
ans = "my name is nagendra,my age is 25"
b = re.findall('[a-z]',ans)
print(b)


b = re.findall('25$',ans)
print(b)







 

   