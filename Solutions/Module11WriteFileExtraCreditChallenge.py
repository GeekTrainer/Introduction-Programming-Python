
#Declare variables to hold the file name and access mode
fileName = "GuestList.txt"
accessMode = "w"

#Open the file for writing
myFile = open(fileName, accessMode)

#Write the guest names and ages to the file
for index in range(5) :
    name = input("Enter guest name: " )
    age = input("Enter guest age: " )
    myFile.write(name + "," + age  + "\n")

#Close the file
myFile.close()
