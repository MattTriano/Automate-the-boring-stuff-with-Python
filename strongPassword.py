#! python3
# strongPassword.py

# Strong Password Detection
# Write a function that uses regular expressions to make sure
# the password string it is passed is strong. A strong password
# is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has
# at least one digit. You may need to test the string against
# multiple regex patterns to validate its strength.

import pyperclip, re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least two capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9].*[0-9])                 # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])          # at least three lower case letters
    .{10,}                              # at least 10 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if (not mo):
        print("Not strong, bling blong")
        return False
    else:
        print("Long, Strong, and down to get the crypto on")
        return True


userInputPasswordCheck()
