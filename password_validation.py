#7. Write a Python program to check the validity of password input by users. Go to the editor. 
# Hint: import the module re and use re.search to find characters.

import re

password = input('''
Your password should match the following criteria
1 lowercase letter between [a-z] and 1 uppercase letter between [A-Z]
At least 1 number between [0-9]
At least 1 special character [$#@]
Minimum length 6 characters
Maximum length 16 characters
Please enter your password here:
''')

pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{6,16}$")
x = re.search(pattern, password)
if x == None:
    print("This password is not valid")
else:
    print("New password is set")