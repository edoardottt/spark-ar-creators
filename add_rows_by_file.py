#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
        if elem in t: ls.append(elem)
    if len(ls)!=0: return "Already inside: " + str(ls)
    count = 0
    with open(new_file,'a+') as f:
        for i in range(len(text)):
            count += 1
            elem = text[i]
            stri = stringed(elem)
            f.write(stri)
    print("Added {} creators".format(count))
    return 'OK'

def stringed(elem):
	if elem[-1]!='_': stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |\n'
	else:
		stri = '| '+elem+' | '+'['+'https://instagram.com/'+elem+'](https://instagram.com/'+elem+') |\n'
	return stri

print(add_func())