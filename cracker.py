#/usr/bin/python3

import hashlib
import os

type_of_hash = str(input("Which type of hash would you like to bruteforce? "))
file_path = str(input("Enter the path to file you intend to bruteforce >  "))
hashtodecrypt = str(input("Enter the hash value to bruteforce >  "))

if os.path.exists(file_path) == False:
	print("[!!!] THAT FILE/PATH DOESN'T EXIST")
	exit(1)

with open(file_path, 'r') as file:
    for line in file.readlines():
        if typ
