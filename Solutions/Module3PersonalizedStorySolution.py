#initialize the variables
girldescription = " " 
boydescription = " " 
walkdescription = " " 
girlname = " "
boyname = " "
animal = " "
gift = " " 
answer = " "

#Ask the user to specify values for the variables
girlname = input("Enter a girl's name: ")
boyname = input("Enter a boy's name: " )
animal = input("Name a type of animal: " )
gift = input("Name something you find in the bathroom: ")
girldescription = input("Enter a description of a flower: ")
boydescription = input("Enter a description of a car: ")
walkdescription = input("Enter a description of how you might dance: " )
answer = input("What would you say to someone who gave you a cow: ")

#Display the story
#Don't forget to format the strings when they are displayed
print ("Once upon a time,")
print("there was a girl named " + girlname.capitalize() + ".")
print("One day, " + girlname.capitalize() + " was walking " + walkdescription.lower() + " down the street.")
print("Then she met a " + boydescription.lower() + " boy named " + boyname.capitalize() + ".")
print("He said, 'You are really " + girldescription.lower() + "!'")
print("She said '" + answer.capitalize() + ", " + boyname.capitalize() + ".'")
print("Then they both rode away on a " + animal.lower() + " and lived happily ever after.")
