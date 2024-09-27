# Purpose: Display the users name using Turtle writing 

from turtle import * #Brings in the turtle module and allows us to utalize turtle code

name = input("What is your name? ") #Get string input  from the user and assign it to the varible name

write(name, font=("Arial", 20, "normal")) #Use the turtle code to display the text the user entered in the font Arial with a size of 20
forward(200) #Moves the turtle cursor forward 200 pixels, underlines the name

done() #finishes the program 
