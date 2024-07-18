# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:30:43 2024

@author: sm689
"""
#time module
import time as t
t.time() #this many seconds passes from the 1st jan onwards
#gives the localtime
#yeat,month,day,hour.....
t.localtime()
 

lt = t.localtime()
type(lt)

#print the year
lt.tm_year
#print the month
lt.tm_mday
#print the hour
lt.tm_hour




import datetime
#creating the date and time
dt1 = datetime.datetime(2010,1,1,10,10,10)
dt1

dt2 = datetime.datetime(day = 1,month = 1,year = 2011,hour = 10,minute=10,second = 10)
dt2

print(dt2 - dt1 )

dt2 > dt1
#comparing dates
dt2 > dt1

dat1 = datetime.date(2015,1,1)
tim1 = datetime.time(10,10,10)
#combining the dates and times
dt3 = datetime.datetime.combine(dat1 ,tim1)
dt3


tim11 = datetime.time(10,10,10)
tim22 = datetime.time(11,11,11)
#we can't compare the times
tim11 -tim22

#we can compare the times
tim11 > tim22


#we can compare the times
tim11 < tim22

























