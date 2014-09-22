#Import the libraries we need for the program
import fileinput

#This is the main function, by declaring a main function and then calling it after all the function definitions
#We can list the functions in our code in the order we want, if we didn't have a mainfunction() we would have needed to list all the functions
#our code called first, which might be a bit hard to read.
def mainFunction():

    #Because this is a fairly long piece of code to write, we have broken up the work into a number of functions
    #To try and make it a little easier to read

    #Step 1 - Ask the user to enter their text message
    #By using a print and then an input statement you give a fresh new line to type in their text message
    print("Please enter the message (no punctuation please):")
    txtMessage = input(">") 

    #Step 2 use the split function to get a list that contains all the words in the text message
    messageWords = txtMessage.split()

    #The translationFileName should contain the name of the file that contains the list of Text message abbreviations
    #and their corresponding translations
    translationFileName = "Translations.txt"

    #call the function we created below to make sure our translation file exists
    # If the file is found it will return a 0
    # If the file is not found it will return a 1
    fileFound = fileCheck(translationFileName)

    if fileFound == 0 :

        #Step 3 a) b) c) Call the function we created below to get back two lists, a list of the abbreviations and a list of the translations
        allAbbreviations, allTranslations = dictionaryList(translationFileName) 

        #Step 3 d) e) Call the function we created below to get back a string containing the translated text message
        translatedMessage = compare(messageWords, allAbbreviations, allTranslations) # the final list of words for the message

        #Step 4) Print the translated message to the user
        print(translatedMessage)
    else : 
        print("Could not translate message, file containing translation terms could not be located.")

#This function will check if a specified file exists.
#If the file exists it will not display any error messages
#If the file does not exist it will display an error message and restart the program.
#Accepts one parameter
#   filename the name of the file to check exists
#Returns one value
#   0 indicates the file was succesfully located
#   1 indicates the file could not be located
def fileCheck(fileName):
    try:
        fileObj = open(fileName) #will try to open the file specified
        return 0
    except IOError: #will handle the exception
        print("Could not locate the file " + fileName)
        return 1

#This function accepts the name of a file that contains abbreviations and translations
#It will return two lists - one containing all the abbreviations, the other containing the translations
#Accepts one parameter
#   fileName    the name of the file containing the abbreviations and translations
#Returns two values
#   A list of abbreviations from the file
#   A list of translations from the file
# This function assumes the file will have the format
#   abbreviation - definition
def dictionaryList(fileName):

    #Declare the lists to be populated and returned
    allAbbreviations = []
    allTranslations = []

    #Step 3 a) open the file
    fileObj = open(fileName)

    for line in iter(fileObj): #This for loop will read the file line by line
        #Take each line in the file and split it into a list of words 
        #LOL - Laughing out Loud will return a list containing ["LOL","-","Laughing","Out","Loud"]
        wordsInTheLine = line.split() 

        #Step 3 b)The first word in the list is the abbreviation, add that to our list of allAbbreviations
        allAbbreviations.append(wordsInTheLine[0])

        #Step 3 c) Now this is the tricky part because we need to take all the remaining words in the list and together they make up our translation
        # e.g. if the line in the file returned ["LOL","-","Laughing","Out","Loud"]
        # we need to combine the words "Laughing","Out","Loud" to get our translation
        #It would be easier if we just had one word translations then we could just add words[1] to our translations list
        #But solving problems isn't always easy!

        translation = ""

        #Find out how many words total are in the line read from the file
        totalNumberOfWords = len(wordsInTheLine)

        #Start with the word at position 2 in the list, this allows us to skip the abbreviation and the hyphen 
        for x in range(2,totalNumberOfWords):
            #now take each word starting with the third word (index 2) until the last word and concatentate them together
            #with a space between each word
            translation = translation + wordsInTheLine[x] + " " 
        
        #add the translation to our list of translations    
        allTranslations.append(translation)

    #return the two lists: the list of abbreviations and the list of translations
    return (allAbbreviations, allTranslations)


#this function will go through each word in the message
#And search for it in the list of abbreviations
#If found in the list of abbreviations it will fetch the corresponding translation (same index number) from the list of translations
#then it will concatenate each of the translations to create the translated text message
#This function accepts three parameters
#   messageWords - this is the list of words in the text message to be translated
#   allAbbreviations - this is the list containing all possible text message abbreviations we can translate
#   allTranslations - this is the list containing all the translations for each text message abbreviation
#This function returns one value
#   finalMessage    - a string that is the translated text message
def compare(messageWords, allAbbreviations, allTranslations):
    
    finalMessage = ""
    
    #Step 3 d) Create a loop that will execute once for each word in our list of words in the text message
    for wordPosition in range(0, len(messageWords)):
        #Fetch the next word from our list of words in the text message
        currentWord = messageWords[wordPosition]

        try :
            #3 d) search the abbreviation list for the current word
            matchPosition = allAbbreviations.index(currentWord.upper())

            #3 e) If you find a match get the translation from the list of definitions
            finalMessage = finalMessage + " " + allTranslations[matchPosition]
        except :
            #If no match is found by the index() search an exception is raised, which means no match was found
            #If no match was found just display the original word in the final message
            finalMessage = finalMessage + " " + currentWord 
            
    return (finalMessage)

mainFunction()