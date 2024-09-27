# Purpose: 

def get_input(): # Will gather new input until the user enters a blank input
    print("Please enter some text...") #Ask for input
    user_input = "" #pre-defines the input string
    while True: #loops infinitly until a break (user enters nothing)
        new_input = input(">>> ") # Takes in input and stores it in the varible 
        if new_input == "": #checks if the user entered nothing 
            break #ends the loop 
        user_input = user_input + "\n" + new_input #Adds the new input to a string of itelf plus a new line to seperate them
    return user_input # Returns the finalized string

def count_lines(str): #Counts the lines 
    return len(str.split("\n")) #Returns how many non-blank inputs the user entered 

def count_words(str): 
    words = {}
    str = str.replace("\n", " ")
    str = str.replace(",", " ")
    str = str.replace(".", " ")
    str_words = str.split()
    for word in str_words:
        words.setdefault(word, 0)
        words[word] = words[word] + 1
    return words

def count_letters(str): #
    all_letters = "abcdefghijklmmopqrstuvwxyz"
    letters = {}
    for letter in str.lower():
        if letter in all_letters:
            letters.setdefault(letter, 0)
            letters[letter] = letters[letter] + 1
    return letters

def dict_max(d):
    max_key = None
    max_value = 0
    for key in d.keys():
        if d[key] > max_value:
            max_key = key
            max_value = d[key]
    return max_key


user_input = get_input()
print("Number of lines: ", count_lines(user_input))
print("Most Common word: ", dict_max(count_words(user_input)))
print("Most Common letter: ", dict_max(count_letters(user_input)))
