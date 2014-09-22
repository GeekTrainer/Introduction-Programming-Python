#import libraries we will use
import sys

#Declare variables
filename = ""
fileContents = ""

#Ask the user for the filename
filename = input("PLease specify the name of the file to read ")

#open the file, since you may get an error when you attempt to open the file 
#For example the file specified may not exist
#put a try except statement around the command
try :   
    myFile = open(filename, "r")

    #I am using a boolean variable to determine if the file was found
    #That waythe code will only attempt to read the file if it was found succesfully
    fileFound = True

#Handle the FileNotFoundError
except FileNotFoundError :
    print("Could not locate file " + filename)
    fileFound = False

#Other errors could occur, perhaps the file is coorupte, or I do not have permissions on the file
except :
    error = sys.exc_info()
    print(error)
    fileFound = False

#if the file was opened successfully read the contents and display the contents to the user
if  fileFound :
    #Get the file contents into a string
    fileContents = myFile.read()
    print(fileContents)
#print the results 
