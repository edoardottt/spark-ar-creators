#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================

> @author: edoardottt
> https://edoardottt.com
> https://github.com/edoardottt/spark-ar-creators
> https://instagram.com/edoardottt

================================

MIT License

Copyright (c) edoardottt

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
import sys


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def check_duplicate_readme():
    """
    Check if in the README.md file there
    are some duplicate profiles.
    """
    print("[-] Checking duplicates in README file...")
    with open("creators.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                creators.append(row[0])
    with open("README.md", encoding="utf8") as f:
        text = f.read()
    duplicates = []
    for creator in creators:
        spaced_creator = " " + creator + " "
        formatted_creator = " " + format_user(creator) + " "
        if (
            text.count(spaced_creator) > 1 or text.count(formatted_creator) > 1
        ) and creator not in duplicates:
            duplicates.append(creator)
    return duplicates


def check_duplicate_creators():
    """
    Check if in the creators.csv file there
    are some duplicate profiles.
    """
    print("[-] Checking duplicates in creators file...")
    with open("creators.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                creators.append(row[0])
    duplicates = []
    for creator in creators:
        if creators.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates


def check_duplicate_scheduled():
    """
    Check if in the scheduled file there
    are some duplicate profiles.
    """
    print("[-] Checking duplicates in scheduled file...")
    creators = read_scheduled()
    duplicates = []
    for creator in creators:
        if creators.count(creator) > 1 and creator not in duplicates:
            duplicates.append(creator)
    return duplicates


def check_missing_creators():
    """
    Check if there are creators in the creators.csv file
    not present in the README file.
    """
    print("[-] Checking if creators are not in README...")
    with open("creators.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                creators.append(row[0])
    with open("README.md", encoding="utf8") as f:
        text = f.read()
    readmes = []
    for elem in creators:
        if elem in text:
            readmes.append(elem)
    return list(set(creators) - set(readmes))


def insert_users_readme(users, not_ok):
    print("[-] Inserting users in README...")
    count = 0
    with open("README.md", "a+", encoding="utf8") as f:
        for i in range(len(users)):
            elem = users[i]
            if elem not in not_ok:
                count += 1
                stri = stringed(elem)
                f.write(stri)
    print(
        bcolors.OKGREEN
        + "[+] Added {} creators into README file.".format(count)
        + bcolors.ENDC
    )


def insert_users_creators(users, not_ok):
    print("[-] Inserting users in creators...")
    count = 0
    with open("creators.csv", "a") as f:
        for elem in users:
            if elem not in not_ok:
                count += 1
                f.write(elem + "," + "\n")
    print(
        bcolors.OKGREEN
        + "[+] Added {} creators into creators file.".format(count)
        + bcolors.ENDC
    )


def present_in_readme(users):
    """
    Check if in the README.md file
    if some of the scheduled profiles are
    already in.
    """
    print("[-] Checking if users already in README...")
    with open("README.md", encoding="utf8") as f:
        text = f.read()
    present = []
    for elem in users:
        if " " + format_user(elem) + " " in text:
            present.append(elem)
    return present


def present_in_creators(users):
    """
    Check if in the creators.csv file
    if some of the scheduled profiles are
    already in.
    """
    print("[-] Checking if users already in creators...")
    with open("creators.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        creators = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                creators.append(row[0])
    present = []
    for user in users:
        if user in creators:
            present.append(user)
    return present


def read_scheduled():
    with open("scheduled.txt", encoding="utf8") as f:
        text = f.read().split()
    return text


def format_user(elem):
    result = elem.replace("_", r"\_")
    return result


def stringed(elem):
    """
    Format the link to Instagram Profiles with correct escape character
    sequences to display correctly in the README.md
    """
    if "_" not in elem:
        stri = "| " + elem + " | " + "https://instagram.com/" + elem + " |\n"
    else:
        elem_ok = format_user(elem)
        stri = (
            "| "
            + elem_ok
            + " | "
            + "["
            + "https://instagram.com/"
            + elem_ok
            + "](https://instagram.com/"
            + elem
            + ") |\n"
        )
    return stri


def flush_scheduled():
    with open("scheduled.txt", "w", encoding="utf8") as f:
        f.write("placeholder")
    print("[+] Scheduled flushed!")


def print_banner():
    print(bcolors.HEADER + "========================================" + bcolors.ENDC)
    print(bcolors.HEADER + "            SPARK AR CREATORS           " + bcolors.ENDC)
    print(bcolors.HEADER + "========================================" + bcolors.ENDC)
    print("")
    print(bcolors.BOLD + "    > @author: edoardottt" + bcolors.ENDC)
    print("")
    print(bcolors.OKGREEN + "    > https://www.edoardottt.com")
    print(
        bcolors.OKCYAN
        + "    > https://github.com/edoardottt/spark-ar-creators"
        + bcolors.ENDC
    )
    print(bcolors.OKBLUE + "    > https://instagram.com/edoardottt" + bcolors.ENDC)
    print("")


def count_creators():
    with open("creators.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            line_count += 1
        return line_count - 1


def checks():
    creators_count = count_creators()
    print("[-] {} creators".format(creators_count))

    candidates = read_scheduled()

    # - scheduled file is empty -
    if candidates[0] == "placeholder":
        print(bcolors.FAIL + "[!] Scheduled empty." + bcolors.FAIL)
        sys.exit()

    duplicates = check_duplicate_readme()

    if len(duplicates) > 0:
        print(bcolors.WARNING + "[!] Duplicates found in README!" + bcolors.ENDC)
        print(duplicates)
        sys.exit()

    duplicates = check_duplicate_creators()

    if len(duplicates) > 0:
        print(bcolors.WARNING + "[!] Duplicates found in creators!" + bcolors.ENDC)
        print(duplicates)
        sys.exit()

    duplicates = check_duplicate_scheduled()

    if len(duplicates) > 0:
        print(bcolors.WARNING + "[!] Duplicates found in scheduled!" + bcolors.ENDC)
        print(duplicates)
        sys.exit()

    missing = check_missing_creators()

    if len(missing) > 0:
        print(
            bcolors.WARNING
            + "[!] Creators found in csv and not in README!"
            + bcolors.ENDC
        )
        print(missing)
        sys.exit()
    return candidates


def add_func():
    """
    This function adds users to the list
    """
    print_banner()

    candidates = checks()

    not_ok = present_in_readme(candidates)

    if len(not_ok) > 0:
        print(bcolors.WARNING + "[!] Users already in README!" + bcolors.ENDC)
        print(not_ok)

    insert_users_readme(candidates, not_ok)

    not_ok = present_in_creators(candidates)

    if len(not_ok) > 0:
        print(bcolors.WARNING + "[!] Users already in creators!" + bcolors.ENDC)
        print(not_ok)

    insert_users_creators(candidates, not_ok)

    flush_scheduled()

    creators_count = count_creators()
    print("[-] {} creators".format(creators_count))

    print(bcolors.OKGREEN + "[#] Finished!" + bcolors.ENDC)


def remove_func():
    """
    This function removes users to the list
    """
    print_banner()

    candidates = checks()

    creators = []

    with open("creators.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                creators.append(row[0])

    with open("creators.csv", "w+") as f:
        f.write("ig_username" + "," + "\n")
        for elem in creators:
            if elem not in candidates:
                f.write(elem + "," + "\n")

    with open("README.md", "w+", encoding="utf8") as f:
        init_readme = """<h1 align="center">
✨🎭 Spark AR Creators 🎭✨
</h1>

<p align="center">
<b>List of 9500 (and counting) Spark AR Creators. Open an issue or contact me if you want to be added</b>
</p>
<!-- badges -->
<p align="center">
    <!-- mainteinance -->
      <a href="https://edoardottt.com">
        <img src="https://github.com/edoardottt/images/blob/main/spark\
-ar-creators/maintained-yes.svg" alt="Mainteinance yes" />
      </a>
      <!-- pr-welcome -->
      <a href="https://edoardottt.com">
        <img src="https://github.com/edoardottt/images/blob/main/spark\
-ar-creators/pr-welcome.svg" alt="pr welcome" />
      </a>
    <!-- ask me anything -->
      <a href="https://edoardottt.com">
        <img src="https://github.com/edoardottt/images/blob/main/spark\
-ar-creators/ask-me-anything.svg" alt="ask me anything" />
      </a>
    <!-- made with python -->
      <a href="https://edoardottt.com">
        <img src="https://github.com/edoardottt/images/blob/main/spark\
-ar-creators/made-with-python.svg" alt="made-with-python" />
      </a>
</p>

| Username | Link to Profile |
| --- | --- |
"""
        f.write(init_readme)
        for i in range(len(creators)):
            elem = creators[i]
            if elem not in candidates:
                stri = stringed(elem)
                f.write(stri)

    flush_scheduled()

    creators_count = count_creators()
    print("[-] {} creators".format(creators_count))

    print(bcolors.OKGREEN + "[#] Finished!" + bcolors.ENDC)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python helper.py { action }")
        print("action can be add or remove")
        sys.exit()
    if sys.argv[1] == "add":
        add_func()
    elif sys.argv[1] == "remove":
        remove_func()
    else:
        print("usage: python helper.py { action }")
        print("action can be add or remove")
