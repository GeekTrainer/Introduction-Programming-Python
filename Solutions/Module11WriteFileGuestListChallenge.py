
#Declare variables to hold the file name and access mode
fileName = "GuestList.txt"
accessMode = "w"

#Open the file for writing
myFile = open(fileName, accessMode)

#Write the guest names and ages to the file

#I can write an entire record in one write statement
myFile.write("Doyle McCarty,27\n")
myFile.write("Jodi Mills,25\n")
myFile.write("Nicholas Rose,32\n")
#I could write the name and age in separate write statements
myFile.write("Kian Goddard")
myFile.write(",36\n")
myFile.write("Zuha Hanania")
myFile.write(",26\n")

#Close the file
myFile.close()

