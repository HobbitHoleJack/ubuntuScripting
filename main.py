import random
import string
import os
import functions as func


if __name__ == '__main__':

    os.system("sudo ufw enable") # no choice for you
    # always enable ufw 

    print("Want to disable ssh root login? Y/N:")
    run = input()
    if run.lower() == 'y':
        func.disablerootlogin()
    run = ""

    print("Want to enforce password requirements? (extremely untested and dangerous) Y/N:")
    run = input()
    if run.lower() == 'y':
        func.passwdenforcer()
    run = ""

    print("Want to change passwords? Y/N:")
    run = input()
    if run.lower() == 'y':
        func.passwordchanger()
    run = ""

    print("Want to find all mp3 files? Y/N:")
    run = input()
    if run.lower() == 'y':
        func.mp3finder()
    run = ""

    print("run updates? Y/N")
    run = input()
    if run.lower() == 'y':
        func.updates()
    run = ""

    print("Add A user? Y/N")
    run = input()
    if run.lower == 'y':
        func.adduser()
    run = ""
