#======================================================================DAteTime-Package==============================================================================
'''
Supplies classes for manipulating dates and times.
'''
from datetime import datetime
#<----------------------------------------------------------How do you get the current date and time in Python?--Start------------------------------------------------>

current_datetime = datetime.now()
print(current_datetime)  # Ex:- 2024-07-10 11:40:57.543957

#<----------------------------------------------------------How do you get the current date and time in Python?--End------------------------------------------------->

#<----------------------------------------------------------How can you get today's date in Python?--Start------------------------------------------------------------>
from datetime import date
today_date = date.today()
print(today_date)  # Ex:- 2024-07-10
#<----------------------------------------------------------How can you get today's date in Python?--End-------------------------------------------------------------->

 #<---------------------------------------------------------How do you create a new date object representing January 1, 2023--Start----------------------------------->
new_date = date(2023, 1, 1)
print(new_date)
 #<---------------------------------------------------------How do you create a new date object representing January 1, 2023--End------------------------------------->

 #<---------------------------------------------------------How can you convert a string into a datetime object?--Start----------------------------------------------->
date_string = '2023-06-15 12:45:35'
date_object =  datetime.strptime(date_string,'%Y-%m-%d %H:%M:%S')
print(date_object)
 #<---------------------------------------------------------How can you convert a string into a datetime object?--End------------------------------------------------->

 #<---------------------------------------------------------How do you calculate the difference between two dates?--Start--------------------------------------------->
date1 = date(2023,1,1)
date2 = date(2024,1,1)
delta = date2 -date1
print(delta.days)
 #<---------------------------------------------------------How do you calculate the difference between two dates?--End----------------------------------------------->

 #<---------------------------------------------------------How do you add or subtract days from a date?--Start------------------------------------------------------->
from datetime import date,timedelta
today = date.today()
new_date = today + timedelta(days=5)
print(new_date)
 #<---------------------------------------------------------How do you add or subtract days from a date?--End--------------------------------------------------------->

 #<---------------------------------------------------------How can you get the day of the week from a date?--Start---------------------------------------------------->
today = date.today()
day_of_week = today.strftime('%A')
print(day_of_week)
 #<---------------------------------------------------------How can you get the day of the week from a date?--End------------------------------------------------------>

 #<---------------------------------------------------------How do you create a time object representing 3:30 PM?--Start----------------------------------------------->
from datetime import time
time_obj = time(15,30)
print(time_obj)
 #<---------------------------------------------------------How do you create a time object representing 3:30 PM?--Start----------------------------------------------->
