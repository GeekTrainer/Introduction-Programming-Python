import csv

#Open my file
with open("Tasmania.txt","r") as animalFile :
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList :
        print(';'.join(currentRow))

        #for currentWord in currentRow :
        #    print(currentWord)



##Read file line by line
#firstAnimal = animalFile.readline()
#print(firstAnimal)
#secondAnimal = animalFile.readline()
#print(secondAnimal)

##read all file contents
#allFileContents = animalFile.read()
#print(allFileContents)
