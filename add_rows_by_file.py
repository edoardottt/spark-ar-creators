#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:01:42 2020

@author: edoardottt
https://edoardoottavianelli.it
"""

import sys

word = sys.argv[1]
new_file = 'new_rows.txt'
with open(word) as f:
    text = f.read().split()
with open(new_file,'w+') as f:
    for i in range(len(text)):
        elem = text[i]
        stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |'
        if i!=len(text)-1: stri+='\n'
        f.write(stri)
    