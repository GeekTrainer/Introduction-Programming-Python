fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'

data = input('Please enter file info')

file = open(fileName, mode = WRITE)
file.write(data)
file.close()

#file = open(fileName, mode = WRITE)
#file.write('Susan, 29\n')
#file.write('Christopher, 31')
#file.close()

print('File written successfully')