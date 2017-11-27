"""
Programmer: Ben Diegel
Program: MULTI-THREADING PROGRAM USED FOR BRUTE FORCE ATTACK
"""

import os


def main():
    os.system("test -e found.data && rm found.data") # tests to see if the found.data file exists already, if it does it
    userInput = input("Please enter a 4-digit password\n>>") # removes it
    writeFile = open('passwordToFind.txt', 'w') # this opens and preps the password file to be written to
    writeFile.write(userInput) # writes userInput from above to the file
    writeFile.close()

    os.system("python3 source.py &") #1 each statment runs a seperate python script with a shared userInput
    os.system("python3 source.py &") #2 this is the main logic behind the multi-threading
    os.system("python3 source.py &") #3 im totatlly cheesing it but it works okay 
    os.system("python3 source.py &") #4 more os.systems = more permutations 
    os.system("python3 source.py &") #5 but at the cost of more CPU 
    os.system("python3 source.py &") #6
    os.system("python3 source.py &") #7
    os.system("python3 source.py &") #8
    os.system("python3 source.py &") #9
    os.system("python3 source.py &") #10

    found = False # this bool is usless but the PKILL statment kills this script to so, oh well
    while(found == False):
        os.system("test -e found.data && pkill -f python") # if the new found.data is seen it stops all python scripts
                                                           # INCLUDING THIS ONE IT IS SELF-TERMINATING
main()