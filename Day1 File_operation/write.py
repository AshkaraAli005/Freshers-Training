import os.path
filePath = input("File Path : ") #Getting path as input
print("Enter 'END' to terminate ...")
is_exists = os.path.exists(filePath)

while (True):#checking whether text is not empty
        fileText = input()  #Getting the data as input
        file = open(filePath , 'a')
         
        if (fileText.lower() == 'end'): #To stop entering the text type END
            break
        file.write(fileText+'\n') 
        file.close()
print(f'Changes are made in file :{str(filePath)}')
