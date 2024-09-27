# Purpose: Creates a list of resturants, chooses a resturant and draws a star next to it.

import random #imports the random module to use random code
from turtle import * #imports the turtle function

def star(size, star_color): #Creates a star
    old_color = fillcolor() #Assigns the variable old_color as fill_color and stores what the color of the pen was before the start of star function
    fillcolor(star_color) #sets the fill color to whatever was stated within the function's arguments
    begin_fill() #starts drawing the star
    for i in range(5): #loops the points five times
        forward(size) #starts drawing the point of the star indicated by the size
        left(72) #turns the pen 72 degrees
        forward(size) #starts drawing the point of the star indicated by the size
        right(144) #turns the pen 144 degrees
    end_fill() #ends drawing the star
    fillcolor(old_color) #changes the pen color to back to what it was before the star function was called

def get_restaurants(): #drags a resturant from the list resturants when the user inputs a resturant
    restaurant_list = [] #assigns the variable "resturant_list" to an input to get called back on
    while True: #starts a loop if the resturant is listed in the list
        rest = input("What is a restaurant you like? ") #asks the user to list a returant
        if rest == "": #If the user does not input anything
            return restaurant_list #returns the list
        restaurant_list.append(rest) #adds the new input to the end of the list

def draw_list(restaurants, choice): #displays the list and puts a star next to the randomly chosen resturant
    for rest in restaurants: #loops through the resturant list
        write(rest, font=("Arial", 20, "normal")) #writes the resturant in Arial font size 20 in normal text
        if rest == choice: #checks if the resturant it is currently writing is the same as the chosen one
            penup(); back(50); left(90); forward(25); right(90); pendown() #Moves the pen back to the start of the written word to draw the star
            star(20, "red") #calls the star function in order to draw a red star next to the randomly chosen resturant
            penup(); right(90); forward(25); left(90); forward(50); pendown() #moves the pen back to front of the word
        penup(); right(90); forward(50); left(90); pendown() #moves the pen down to the next word



rest_list = get_restaurants() #returns the list of the get_resturants into the variable rest_list
rest_list.sort() #sorts the list into alpabetical order
to_go_to = random.choice(rest_list) #picks a random resturant within the list and assigns it as the variable to_go_to
draw_list(rest_list, to_go_to) #prints out the resturant list and adds a red star to the randomly picked resturant

done() #ends the entire program

        
