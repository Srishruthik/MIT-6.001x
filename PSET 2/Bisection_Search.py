#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:40:58 2020

@author: shruthik
"""


balance = 320000
annualInterestRate = 0.2
current_balance = balance
monthlyinterest = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = balance * ((1 + (annualInterestRate / 12.0)) ** 12) / 12


while abs(balance) >= 0.01:
    balance = current_balance 
    current_payment = (lowerBound + upperBound)/2.0
    
    for i in range(12):      
        balance = balance - current_payment
        balance += balance * monthlyinterest
    if balance < 0:
         upperBound = current_payment
    elif balance > 0:
       lowerBound = current_payment
    else:
        break
print("Lowest Payment: " + str(round(current_payment,2)))
