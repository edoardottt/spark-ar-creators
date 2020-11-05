#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

================================

@author: edoardottt
https://edoardoottavianelli.it
https://github.com/edoardottt/spark-ar-creators

================================

MIT License

Copyright (c) 2020 edoardottt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

================================

DISCLAIMER:

Spark-AR is a registered mark as Copyright (c) 2016-present, Facebook, Inc.
https://sparkar.facebook.com/ar-studio/

================================

"""

import csv

def check_duplicate_readme():
    """
    Check for duplicate duplicate duplicates.

    Args:
    """
    print("[-] Checking duplicates in README...")
    with open("creators.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0: line_count += 1
            else:
                creators.append(row[0])
    with open("README.md", encoding="utf8") as f:
        text = f.read()
    duplicates = []
    for creator in creators:
        spaced_creator = " " + creator + " "
        formatted_creator = " " + format_user(creator) + " "
        if (text.count(spaced_creator) > 1 or text.count(formatted_creator) > 1) and creator not in duplicates:
            duplicates.append(creator)
    return duplicates

def check_duplicate_creators():
    """
    Check for duplicate duplicate duplicates.

    Args:
    """
    print("[-] Checking duplicates in creators...")
    with open("creators.csv",encoding="utf8") as csv_file:
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
    """
    Return a list of duplicates are duplicated.

    Args:
    """
    print("[-] Checking duplicates in scheduled...")
    creators = read_scheduled()
    duplicates = []
    for creator in creators:
        if creators.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates

def insert_users_readme(users,not_ok):
    """
    Insert the users readme.

    Args:
        users: (todo): write your description
        not_ok: (todo): write your description
    """
    print("[-] Inserting users in README...")
    count = 0
    with open("README.md","a+",encoding="utf8") as f:
        for i in range(len(users)):
            elem = users[i]
            if elem not in not_ok:
                count += 1
                stri = stringed(elem)
                f.write(stri)
    print("[+] Added {} creators into README.".format(count))

def insert_users_creators(users,not_ok):
    """
    Inserts the user can add_creates.

    Args:
        users: (todo): write your description
        not_ok: (bool): write your description
    """
    print("[-] Inserting users in creators...")
    count = 0
    with open("creators.csv",'a') as f:
        for elem in users:
            if elem not in not_ok:
                count += 1
                f.write(elem + "," + "\n")
    print("[+] Added {} creators into creators.".format(count))

def present_in_readme(users):
    """
    Returns a list of readme is readme

    Args:
        users: (todo): write your description
    """
    print("[-] Checking if users already in README...")
    with open("README.md",encoding="utf8") as f:
        text = f.read()
    present = []
    for elem in users:
        if " " + format_user(elem) + " " in text: present.append(elem)
    return present

def present_in_creators(users):
    """
    Returns a list of dictionaries containing all user.

    Args:
        users: (todo): write your description
    """
    print("[-] Checking if users already in creators...")
    with open("creators.csv",encoding="utf8") as csv_file:
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
    """
    Reads the scheduler.

    Args:
    """
    with open("scheduled.txt",encoding="utf8") as f:
        text = f.read().split()
    return text

def format_user(elem):
    """
    Format a user.

    Args:
        elem: (str): write your description
    """
    result = elem.replace("_","\_")    
    return result
    
def stringed(elem):
    """
    Return a string representation of an element.

    Args:
        elem: (str): write your description
    """
    if "_" not in elem: stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |\n'
    else:
        elem_ok = format_user(elem)
        stri = '| '+elem_ok+' | '+'['+'https://instagram.com/'+elem_ok+'](https://instagram.com/'+elem+') |\n'
    return stri

def flush_scheduled():
    """
    Flush scheduled scheduled scheduled scheduler.

    Args:
    """
    with open("scheduled.txt","w",encoding="utf8") as f:
        f.write("placeholder")
    print("[+] Scheduled flushed!")

def add_func():
    """
    Add a new function.

    Args:
    """
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