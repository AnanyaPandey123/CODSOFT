#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      akppa
#
# Created:     14-09-2024
# Copyright:   (c) akppa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Password Generator...........................................................

import random
import string

length = int(input("Enter the desired password length:"))
complexity = int(input('''Enter the level of complexity{0-3} where,
0: Only lowercase letter 1: Lowercase and uppercase letters
2: Lowercase, uppercase letters, and numbers
3: Lowercase, uppercase letters, numbers, and symbols'''))
characters = ""
if complexity >= 0:
    characters += string.ascii_lowercase
if complexity >= 1:
    characters += string.ascii_uppercase
if complexity >= 2:
    characters += string.digits
if complexity >= 3:
    characters += string.punctuation

password = "".join(random.choices(characters, k=length))

print("Your password is:",password)
