def getNames():
    names = ['Christopher', 'Susan', 'Danny']
    newName = input('Enter last guest: ')
    names.append(newName)
    return names

def printNames(names):
    for name in names:
        print(name)
    return