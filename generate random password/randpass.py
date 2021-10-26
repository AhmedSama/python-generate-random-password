import random
from sys import argv

# vars
default_range = 15
commands = ["-s","-m","-w","-n","-p","randpass.py"]
lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = lowerLetters.upper()
punc = ".),#$%(&*-_+="
numbers = "1234567890"
# util functions
def usage():
    print("usage : ")
    print("\t-l ")
    print("\t\t length of the password")
    print("\t-n")
    print("\t\t if you want numers in the generated password")
    print("\t-p\n\t\t if you want panctuation marks in your generated password")
    print("example : ")
    print("python randpass.py -l 10")
    print("python randpass.py -l 15 -n")
    print("python randpass.py -l 11 -p")
    print("python randpass.py -l 23 -n -p")

def make_pass(r):
    pwd = ""
    if "-n" not in argv and "-p" not in argv:
        for _ in range(r):
            randy = random.randint(0, 1)
            if(randy == 0):
                pwd += random.choice(lowerLetters)
            elif(randy == 1):
                pwd += random.choice(upperLetters)
        print(pwd)
        return
    if "-p" not in argv:
        for _ in range(r):
            randy = random.randint(0, 2)
            if(randy == 0):
                pwd += random.choice(lowerLetters)
            elif(randy == 1):
                pwd += random.choice(upperLetters)
            elif(randy == 2):
                pwd += random.choice(numbers)
        print(pwd)
        return
    if "-n" not in argv:
        for _ in range(r):
            randy = random.randint(0, 2)
            if(randy == 0):
                pwd += random.choice(lowerLetters)
            elif(randy == 1):
                pwd += random.choice(upperLetters)
            elif(randy == 2):
                pwd += random.choice(punc)
        print(pwd)
        return
    else:
        for _ in range(r):
            randy = random.randint(0, 3)
            if(randy == 0):
                pwd += random.choice(lowerLetters)
            elif(randy == 1):
                pwd += random.choice(upperLetters)
            elif(randy == 2):
                pwd += random.choice(numbers)
            elif(randy == 3):
                pwd += random.choice(punc)
        print(pwd)
        return

def inCommands():
    for arg in argv:
        if arg not in commands:
            return False
    return True

# main function
def gen_rand_pass():
    if(len(argv)==1):
        usage()
        return
    if "-l" not in argv:
        if len(argv) > 0 and inCommands() == False:
            usage()
            return
        make_pass(default_range)
    elif "-l" in argv:
        try:
            length = int(argv[2])
            make_pass(length)
        except Exception as e:
            usage()
            return
gen_rand_pass()

