import random
import string
import os

def disablerootlogin(): # disables ssh root login

  # Read file in read mode 'r'
  with open('/etc/ssh/sshd_config', 'r') as file:
    content = file.read()
  # Replace string
  content = content.replace('PermitRootLogin yes', 'PermitRootLogin no')
  # Write new content in write mode 'w'
  with open('/etc/ssh/sshd_config', 'w') as file:
    file.write(content)


def passwordchanger(): # changes all user's passwords listed in users.txt

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


def passwordgen(): # password generator utility for the passwordchanger function

    password_length = 20

    characters = string.ascii_letters + string.digits

    password = ""

    for index in range(password_length):
        password = password + random.choice(characters)

    return password


def passwdenforcer(): # enforces password requirements
    
    os.system("sudo apt-get install libpam-cracklib -y")
    os.system("sudo gedit /etc/login.defs")
    os.system("sudo gedit /etc/pam.d/common-password")

 
def mp3finder(): # finds all mp3 files

    print("finding .mp3s")
    os.system("cd /home")
    os.system('sudo find / -iname "*.mp3" -print')


def read_and_parse(filename):
    users = []
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if line.find("/nologin") == -1:
                if (line.find("/nologin") == -1) and (line.find("/bin/false") == -1) and (line.find("/bin/sync") == -1):
                    data.append(line.split(":")[0])
        data.sort()
        for item in data:
            users += item
    return users


def userfilesearch():

    users = read_and_parse("/etc/passwd")
    print(users)

    
