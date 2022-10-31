import random
import string
import os
import functions as func


if __name__ == '__main__':


    print("Want to enforce password requirements? (this is all manual input, make sure you know what you're looking for) Y/N:")
    run = input()
    if run.lower() == 'y':
        func.disablerootlogin()

    print("Want to enforce password requirements? (extremely untested and dangerous) Y/N:")
    run = input()
    if run.lower() == 'y':
        func.passwdenforcer()

    print("Want to change passwords? Y/N:")
    run = input()
    if run.lower() == 'y':
        func.passwordchanger()

    print("Want to find all mp3 files? Y/N:")
    run = input()
    if run.lower() == 'y':
        func.mp3finder()

    print("run updates? Y/N")
    run = input()
    if run.lower() == 'y':
        func.updates()

    