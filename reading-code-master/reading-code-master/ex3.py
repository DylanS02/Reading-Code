# Purpose: 


from turtle import * #Brings in the turtle module and allows us to utalize turtle code

def bar(bar_color): #Creates a function called bar that takes one argument 
    old_fill = fillcolor() #Sets the varible to the fill color, will switch at runtime, contain what the color was before run
    old_pen = pencolor() #Sets the pen color to the current color, will switch at runtime, contain what the color was before run
    color(bar_color) #sets the color with the taken argument
    begin_fill() #Makes sure that fill is achived 
    forward(300) #Moves the cursor forward 300 pixels 
    left(90) #Turns the curser left 90 degrees
    forward(10) #Moves the cursor forward 10 pixels 
    left(90) #turns the cursor left 90 degrees
    forward(300) #Moves the cursor forward 300 pixels 
    left(90) #turns the cursor left 90 degrees
    forward(10) #Moves the cursor forward 10 pixels 
    left(90) #turns the cursor left 90 degrees
    end_fill() #Stops filling the drawing
    color(old_pen, old_fill) #Sets a new color back to the old varibles stored at the start of the function

def box(box_color): #Defines a varible that draws a box, takes one argument
    color(box_color) #sets the pen color to the taken argument
    begin_fill() #starts fill
    for i in range(4): #loops 4 times
        forward(70) #moves the pen forward 70 pixels 
        right(90) #turns right 90 degrees
    end_fill() #ends fill AFTER loop


def next(): #Creates a function that takes no argument, moves the pen over
    penup() #Prevents drawing until pendown() 
    right(90) #turns the pen 90 degrees
    forward(10) #Moves the pen forward 10 pixels
    left(90) #Turns the pen left 90 degrees (resets position)
    pendown() #puts pen down so drawing can begin again

speed(9) #sets speed of the pen to 9

for i in range(6): #loops 6 times 
    bar("red") #Calls the bar function giving it the argument "red"
    next() #runs the next function to move the pen over and reset position
    bar("white") #Calls the bar function giving it the argument "white"
    next() #runs the next function to move the pen over and reset position
bar("red") #Calls the bar function giving it the argument "red", adds our 13th bar
next() #runs the next function to move the pen over and reset position

penup(); goto(0,11); pendown() #Sets pen cordionits to 0,11, without drawing 
box("blue") #runs the box function with the argument "blue", making a blue box

done() #finished the drawing but does not close the drawing window
