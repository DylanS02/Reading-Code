# Purpose: It allows the user to find what postion a letter is in a message that the user inputs

def letter_places(str, letter): #defining the function letter_places
    places = [] #sets an sets that holds on to the stored places
    start = 0 #sets an intial place to look for the letter from 
    while True: #while true, the function runs infinitely until a break occurs
        where = str.find(letter,start) #where finds the first instance of the letter, begining the search at start of the message
        if (where == -1): #If the letter is not in the message, it ends the loop
            break #ends the loop
        places.append(where) #takes the recently found first instance of the letter and puts it at the end of the list.
        start = where + 1 #moves the start location proportional to the where variable
    return places #returns the loop

def nth(num): #creates a function to assign suffixes to numbers 
    if num == 1: #registers if the number is 1
        return str(num) + "st" #Returns the variable and adds the suffix "st"
    if num == 2: #registers if the number is 1
        return str(num) + "nd" #returns the variable and adds the suffix "nd"
    if num == 3: Registers if the number is 3
        return str(num) + "rd" #returns the variable and adds the suffix "th"
    return str(num) + "th" #returns the function (num)

user_input = input("Enter a message: ") #Asks the user for an input and states "Enter a message", prompting the user
user_letter = input("What letter are you looking for? ") #Asks the user after the first input what letter they are looking for"

places = letter_places(user_input, user_letter) #assigns the variable places to the entire list within the function letter_places

if len(places) == 0: #If there are no places that match what the user inputs, then it prints the message below
    print("That letter does not appear") #prints the "that letter does not appear" message if the place a user inputs does not exist in the list
else: #if the input is of a place within the list
    for place in places: #loops through the list of places
        print("That letter is the", nth(place+1), "letter") #prints the message "That letter is the", and then displays the number with its suffix to tell the user what place the letter is in the list.




