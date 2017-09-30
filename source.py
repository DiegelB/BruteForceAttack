"""
Programmer: Ben Diegel
Program: Brute Force Passoword Cracker
Notes: This program uses brute force to find the correct password
that is saved in the passwordToFind.txt file. 
"""

import random
import datetime

# These are the lists that contain all of the letters or numbers that the 
# script randomizes
alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',
         'z','x','c','v','b','n','m']
num = ['1','2','3','4','5','6','7','8','9','0']

global PASS_SIZE 
PASS_SIZE = 4 # size of the password length

# this function decides wheter it will randomize an alpha or numerical character for 
# any given position. It is passed the lists alpha and num
def posGenerator(alpha, num):
    choice = random.randint(1, 6)
    if(choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5):
        return random.choice(alpha)
    else:
        return random.choice(num)

# this is the main module that creates the password and saves the correct password/time/and permutations
# to file
def bruteAttack():
    readFile = open('passwordToFind.txt', 'r') # opens file to read real password
    userInput = readFile.read(PASS_SIZE)
    found = False # used for the main loops
    counter = 1 # counts the number of guess it made (permutations)

    timeStart = datetime.datetime.now() # this signifies the start of the loop


    while(found == False):
        pos1 = posGenerator(alpha, num) # each pos variable stands for a different position withint
        pos2 = posGenerator(alpha, num) # the password    
        pos3 = posGenerator(alpha, num)
        pos4 = posGenerator(alpha, num)
        #pos5 = posGenerator(alpha, num)
        #pos6 = posGenerator(alpha, num)
        #pos7 = posGenerator(alpha, num)
        #pos8 = posGenerator(alpha, num)

        # this combines all the generated characters into its guessed password
        passWord = pos1 + pos2 + pos3 + pos4 #+ pos5 #+ pos6 #+ pos7 #+ pos8 
        print(passWord) # main line to print each guess

        # this statment tests to see if the guessed password matches the password found in 
        # passwordToFind.txt
        if(userInput == passWord):
            found = True # if it is found it stops the loop
            timeEnd = datetime.datetime.now() # it stops the time
            timeTook = timeEnd - timeStart # it finds how long it took overall
            print("Your password is " + passWord) 
            print("It took me " + str(counter) + " different permutations")
            print("That took " + str(timeTook)+ "(hh:mm:ss)")
            print("Saved to PasswordCrack.data")
            
            # this statment saves the password to a mass-password folder
            writeFile = open('PasswordCrack.data', 'a')
            writeFile.write("Password: " + passWord + "\n")
            writeFile.write(str(counter) + " different permutations\n")
            writeFile.write("Time took: " + str(timeTook) + "(hh:mm:ss)\n\n")
            writeFile.close()

            # this save file is used to stop all parallel python scripts
            # once multiProgram.py sees that this file was created, it kills
            # all python scripts using os.system
            multiFile = open('found.data','w')
            multiFile.write("Password: " + passWord + "\n")
            multiFile.write(str(counter) + " different permutations\n")
            multiFile.write("Time took: " + str(timeTook) + "(hh:mm:ss)\n\n")
            multiFile.close()
            multiFile
        else: # if the guessed password does not match the real one it adds to the permutation counter
            found = False
            counter = counter + 1

bruteAttack()