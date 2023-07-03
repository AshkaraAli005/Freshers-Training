import os.path
filePath = input("File Path : ") #Getting path as input
is_exists = os.path.exists(filePath)

while (True):
        fileText = input()
        file = open(filePath , 'a')
         
        if (fileText.lower() == 'end'):
            break
        file.write(fileText+'\n')
        file.close()
print(f'Changes are made in file :{str(filePath)}')
