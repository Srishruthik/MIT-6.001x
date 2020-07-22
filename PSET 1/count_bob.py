#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:25:37 2020

@author: shruthik
"""


count = 0
s = input('Enter')
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
        
print(count)