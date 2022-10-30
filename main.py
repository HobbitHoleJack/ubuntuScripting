import random
import string
import os
import disablerootlogin.py as drl


def updates():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")

def passwordchanger():
    filepath = "users.txt"
    with open(filepath) as fp:
        lines = fp.read().splitlines()
    with open(filepath, "w") as fp:
        for line in lines:
            if '#' not in line:
                print(line + ":" + passwordgen(), file=fp)

    print("open up the users.txt file, are you ready to change their passwords? Y/N:")
    run = input()
    if run.lower() == 'y':
        os.system("sudo chpasswd < users.txt")

def passwordgen():
    password_length = 20

    characters = string.ascii_letters + string.digits

    password = ""

    for index in range(password_length):
        password = password + random.choice(characters)

    return password

def passwdenforcer(): 
    
    os.system("sudo apt-get install libpam-cracklib")
    os.system("sudo gedit /etc/login.defs") # can be automated
    os.system("sudo gedit /etc/pam.d/common-password") # cannot be automated

def mp3finder():
    print("finding .mp3s")
    os.system("cd /home")
    os.system('sudo find / -iname "*.mp3" -print')


if __name__ == '__main__':


    print("Want to enforce password requirements? (this is all manual input, make sure you know what you're looking for) Y/N:")
    run = input()
    if run.lower() == 'y':
        drl.disablerootlogin()

    print("Want to enforce password requirements? (this is all manual input, make sure you know what you're looking for) Y/N:")
    run = input()
    if run.lower() == 'y':
        passwdenforcer()

    print("Want to change passwords? Y/N:")
    run = input()
    if run.lower() == 'y':
        passwordchanger()

    print("Want to find all mp3 files? Y/N:")
    run = input()
    if run.lower() == 'y':
        mp3finder()

    print("run updates? Y/N")
    run = input()
    if run.lower() == 'y':
        updates()

    