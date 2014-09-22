#Import the turtle drawing library
import turtle

#Declare variables to hold the information the user enters and set the variables to initial values
penColor = 'black'
lineLength = 0
angle = 0

#Ask user for values for pen color, line length, and angle
#Don't forget to convert the numeric values to integers!
lineLength = int(input("How long would you like to make the line? (specify 0 to stop drawing) " ))
penColor = input("What pen color would you like to use? (black, blue, red, green): ")
angle = int(input("What angle would you like? (0-360): "))

while lineLength != 0 :
    #Draw a line using the values entered by the user
    turtle.color(penColor)
    turtle.right(angle)
    turtle.forward(lineLength)
   
    #Don't forget to ask for new values inside the loop, otherwise lineLength will never change
    #And your loop could execute forever, like mine did the first time I wrote this code!
    #Luckily if yo udo accidentally code an infinite loop you can just click the Stop Debugging button in Visual Studio
    lineLength = int(input("How long would you like to make the line? (specify 0 to stop drawing) " ))
    #If they enter a length of zero then they want to stop drawing, so don't ask for the pen color and angle
    if lineLength != 0 :
        penColor = input("What pen color would you like to use? (black, blue, red, green): ")
        angle = int(input("What angle would you like? (0-360): "))

print("You are an amazing artist!")
