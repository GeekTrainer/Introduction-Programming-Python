#Define this function
#When someone calls this function, execute this code
def main():
    names = getNames()
    printNames(names)
    return

def getNames():
    names = ['Christopher', 'Susan', 'Danny']
    newName = input('Enter last guest: ')
    names.append(newName)
    return names

def printNames(names):
    for name in names:
        print(name)
    return

#Execute the main function
#In order to do that the function must be created
#Start the program
main() 
