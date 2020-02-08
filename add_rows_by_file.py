#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:01:42 2020

@author: edoardottt
https://edoardoottavianelli.it
"""

import sys
def add_func():
    word = sys.argv[1]
    new_file = 'README.md'
    with open(word) as f:
        text = f.read().split()
    with open(new_file) as f:
        t = f.read()
    ls = []
    for elem in text:
        if elem in t: ls.add(elem)
    if len(ls)!=0: return 'Delete '+str(ls)
    with open(new_file,'a+') as f:
        for i in range(len(text)):
            elem = text[i]
            stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |'
            if i!=len(text)-1: stri+='\n'
            f.write(stri)
    return 'OK'
print(add_func())