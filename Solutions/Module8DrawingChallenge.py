#Import the turtle library
import turtle

#Declare your variables
nbrSides = 0
lengthOfLine = 20

#Ask user how many sides they want for their object
#Don't forget to convert that value into a integer
#if you convert to float the for loop will give you an error because range values must be integers
nbrSides = int(input("How many sides do you want on your object? " ))

#Create a loop to draw the object
for side in range(0,nbrSides) :
    turtle.forward(lengthOfLine)
    #the angle to turn depends on the number of sides of the object
    turtle.right(360/nbrSides)

    #This is the double bonus challenge, a nested loop that draws a smaller version of the object inside
    for side in range(0,nbrSides) :
        turtle.forward(lengthOfLine/2)
        turtle.right(360/nbrSides)




