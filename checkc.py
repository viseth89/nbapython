#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:45:42 2016

@author: visethsen
"""
oth = 0

name = input('Greetings, Please Enter Your Name : ')
print ()
print ('Hello ' + name + ' Thank You for Using our V-Pay System')

hrs=input('Please enter how many hours you have worked : ')
try:
    int(hrs)
except:
    hrs=input('Please enter a numeric number (Such as 40)')
    
rate = input('Please enter your rate of pay : ')
try:
    int(rate)
except:
    rate=input('Please enter your rate of pay as a number with no other symbols (Example 20.00)')

if int(hrs) > 40:
    oth = int(hrs) - 40
    otp = int(oth) * int(rate) * 1.5
    pay = int(rate) * int(hrs) + int(otp)
    print (pay)
else:
    print ('Pay = ' + int(rate)*int(hrs))
    

    
print (hrs)
