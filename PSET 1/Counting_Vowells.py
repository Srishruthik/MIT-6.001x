#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:22:41 2020

@author: shruthik
"""


num_vowell = 0
s = input('ENTER SOMETHING: ')
for vowell in s:
    if vowell == 'a' or vowell == 'e' or vowell == 'i' or vowell == 'o' or vowell == 'u':
        num_vowell+=1
print(num_vowell)        
   