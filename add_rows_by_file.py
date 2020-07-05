#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: edoardottt
https://edoardoottavianelli.it
"""

import csv

def check_duplicate_readme():
    print("[-] Checking duplicates in README...")
    with open("creators.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0: line_count += 1
            else:
                creators.append(row[0])
    with open("README.md") as f:
        text = f.read()
    duplicates = []
    for creator in creators:
        creator = " " + format_user(creator) + " "
        if text.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates

def check_duplicate_creators():
    print("[-] Checking duplicates in creators...")
    with open("creators.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0: line_count += 1
            else:
                creators.append(row[0])
    duplicates = []
    for creator in creators:
        if creators.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates

def check_duplicate_scheduled():
    print("[-] Checking duplicates in scheduled...")
    creators = read_scheduled()
    duplicates = []
    for creator in creators:
        if creators.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates

def insert_users_readme(users,not_ok):
    for elem in not_ok: users.remove(elem)
    print("[-] Inserting users in README...")
    with open("README.md","a+") as f:
        for i in range(len(users)):
            elem = users[i]
            stri = stringed(elem)
            f.write(stri)
    print("[+] Added {} creators into README.".format(len(users)))

def insert_users_creators(users,not_ok):
    for elem in not_ok: users.remove(elem)
    print("[-] Inserting users in creators...")
    with open("creators.csv",'a') as f:
        for elem in users:
            f.write(elem + "," + "\n")
    print("[+] Added {} creators into creators.".format(len(users)))

def present_in_readme(users):
    print("[-] Checking if users already in README...")
    with open("README.md") as f:
        text = f.read()
    present = []
    for elem in users:
        if " " + format_user(elem) + " " in text: present.append(elem)
    return present

def present_in_creators(users):
    print("[-] Checking if users already in creators...")
    with open("creators.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0: line_count += 1
            else:
                creators.append(row[0])
    present = []
    for user in users:
        if user in creators:
            present.append(user)
    return present    

def read_scheduled():
    with open("scheduled.txt") as f:
        text = f.read().split()
    return text

def format_user(elem):
    result = elem.replace("_","\_")    
    return result
    
def stringed(elem):
    if "_" not in elem: stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |\n'
    else:
        elem_ok = format_user(elem)
        stri = '| '+elem_ok+' | '+'['+'https://instagram.com/'+elem_ok+'](https://instagram.com/'+elem+') |\n'
    return stri

def flush_scheduled():
    with open("scheduled.txt","w") as f:
        f.write("placeholder")
    print("[+] Scheduled flushed!")

def add_func():
    candidates = read_scheduled()
    if candidates[0] == "placeholder":
        print("[!] Scheduled empty.")
        return 0
    duplicates = check_duplicate_readme()
    if len(duplicates) > 0:
        print("[!] Duplicates found in README!")
        print(duplicates)
        return 0
    duplicates = check_duplicate_creators()
    if len(duplicates) > 0:
        print("[!] Duplicates found in creators!")
        print(duplicates)
        return 0
    duplicates = check_duplicate_scheduled()
    if len(duplicates) > 0:
        print("[!] Duplicates found in scheduled!")
        print(duplicates)
        return 0
    candidates = read_scheduled()
    not_ok = present_in_readme(candidates)
    if len(not_ok) > 0:
        print("[!] Users already in README!")
        print(not_ok)
    insert_users_readme(candidates,not_ok)
    not_ok = present_in_creators(candidates)
    if len(not_ok) > 0:
        print("[!] Users already in creators!")
        print(not_ok)
    insert_users_creators(candidates,not_ok)
    flush_scheduled()
    print("[#] Finished!")

if __name__ == "__main__":
    add_func()