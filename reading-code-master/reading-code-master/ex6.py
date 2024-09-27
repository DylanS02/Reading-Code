# Purpose: Creates a random string of random numbers and letters, length is the users choice

import random #Brings in the random module

def random_letter(): #Picks a random letter from the alphabet, both capitol and lowercase
    letters = 'abcdefghijklmnopqrstuvwxyz' #Stores a lowercase version of the alphabet
    letters = letters + letters.upper() #Attaches an uppercase version of the alphabet to the lowercase on, in order to have all letters
    return random.choice(letters) #Picks a random letter and returns it

def random_number(): #Picks a random number from 0-9
    numbers = '0123456789' #Creates a string containing the numbers 0-9
    return random.choice(numbers) # Picks a random number from numbers

howlong = input("How long do you want it to be? ") #Ask the user how long they want their randomly generated string to be
out = "" #creates a "blank" varible, will store the output later

for char in range(int(howlong)): # Counts up from 0 to howlong-1
    which = random.choice(["letter", "number"]) #picks a random number and letter
    if which == "letter": #checks if which picked letter
        out = out + random_letter() # adds a random letter to the output string 
    else: #checks if which picked number
        out = out + random_number() # adds a random number to the output string 

print(out) #displys the output string!!!!!!!!!!!!!!
