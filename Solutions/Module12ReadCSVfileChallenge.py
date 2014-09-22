#import the csv library which contains functions to help you work with CSV files
import csv 

#Declare variables to hold the file name and access mode
fileName = "GuestList.txt"
accessMode = "r"

#open the file 
with open(fileName, accessMode) as myCSVFile:
    #Read the file contents 
    #specify that we are using a comma to separate the values in the file
    dataFromFile = csv.reader(myCSVFile, delimiter =",")

    #Create a for loop that will run once for each row in the list
    for row in dataFromFile :
        #print an entire row at a time in a list format
        print(row) 

        #print the entire row separating the values in the list with a comma
        print (', '.join(row))

        #Print each indivudal value in each row
        for value in row :
            print(value + "\n")

#Close the file
myCSVFile.close()