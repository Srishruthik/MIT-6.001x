#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:27:50 2020

@author: shruthik
"""


# Take 1 number and see if this is bigger or equal to the second number
now = ''
alphabetical = ''
s = input('Enter SOmething:')
for i in range(len(s)):
 if (s[i] >= s[i-1]):
  now = now + s[i]
 else:
  now = s[i]
 if len(alphabetical) < len(now):
  alphabetical = now
print("Longest substring in alphabetical order is: " + alphabetical)
