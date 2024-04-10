#!/usr/bin/python3

import hashlib
import os

def crack_hash(type_of_hash, file_path, hashtodecrypt):
    if not os.path.exists(file_path):
        print("[!!!] THAT FILE/PATH DOESN'T EXIST")
        return

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if type_of_hash.lower() == 'md5':
                hash_obj = hashlib.md5(line.encode())
            elif type_of_hash.lower() == 'sha1':
                hash_obj = hashlib.sha1(line.encode())
            elif type_of_hash.lower() == 'sha256':
                hash_obj = hashlib.sha256(line.encode())
            elif type_of_hash.lower() == 'sha512':
                hash_obj = hashlib.sha512(line.encode())
            else:
                print("[!!!] Unsupported hash type:", type_of_hash)
                return

            hashed_guess = hash_obj.hexdigest()
            if hashed_guess == hashtodecrypt:
                print("[+] The password is", line)
                return

    print("[-] Password not found")

if __name__ == "__main__":
    type_of_hash = input("Which type of hash would you like to bruteforce? ")
    file_path = input("Enter the path to file you intend to bruteforce: ")
    hashtodecrypt = input("Enter the hash value to bruteforce: ")

    crack_hash(type_of_hash, file_path, hashtodecrypt)
