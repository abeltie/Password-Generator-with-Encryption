""" This file will generate random password for a specific web page
and save info (web URLs and passwords) in a log file.
"""

# import secrets
import string
from random import randrange, choice
from cryptography.fernet import Fernet

# let the user key in the web page for the password
while True:
    websiteIdentification = input("Website identification(This will be the file name of your saved credentials.):")
    website = 'Password for ' + websiteIdentification
    if websiteIdentification.isspace() is True or websiteIdentification == "":
            print("Please enter a valid URL for identification.")
    else:
        fileName = open(website, "w+")
        break

# insert the desired length of password
while True:
    try:
        passwordLength = int(input("Length of password (Longer password is more secured.):"))
        if passwordLength < 6:
            print("Please enter a value above 5.")
            continue
    except ValueError:
        print("Please enter an appropriate password length.")
        continue
    else:
        break

# let the user choose if special symbol is required
specialSymbol_req = input("Is special symbol (@, !, etc) required? (Y/N)")

if specialSymbol_req == "Y":
    specialSymbol = input("Which symbol do you intend to include?")
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(1, passwordLength+1))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            index = randrange(1, passwordLength)
            password = password[:index] + specialSymbol + password[index+1:]
            # print the password
            print(password)
            # write credentials to txt files
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(b'password')
            break

# ##decrease the input length of pw by one then adding a specific symbol at a random position ## #

elif specialSymbol_req == "N":
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(1, passwordLength+1))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            # print the password
            print(password)
            # write credentials to txt files
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(b'password')
            break

# user did not enter a valid input
elif specialSymbol_req != "Y" or "N":
    print("Please enter Y or N only.")

# write the generated key to a txt file
# unfinished
