# i create password generator program 

import random
pass_length = int(input("Enter the lenth of password : "))
upper = input("incude upper letter? (yes/no) : ").lower()
lower = input("include lower letter? (yes/no) : ").lower()        # taking input from user 
num   = input("include number? (yes/no) : ").lower()
sym   = input("include symbol? (yes/no) : ").lower()

char = ""
if upper == "yes":
    char += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lower == "yes":
    char += "abcdefghijklmnopqrstuvwxyz"
if num == "yes":                                             # checking condition 
    char += "1234567890"
if sym == "yes":
    char += "!@#$%^&*()_+"

if len(char) == 0:
    print("Please select at least one option")
else:
    password = ""
    for i in range (pass_length):
        password += random.choice(char)                    # create loop for password and choose randomly
    print(f"YOUR PASSWORD IS : {password}")

