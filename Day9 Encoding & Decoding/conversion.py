files = input("Enter the file name : ") 
with open(files,"rb") as f1:
    data=f1.read()

encode_val=(data.decode("utf-8","ignore"))

print(encode_val)
print("encode successfully completed!!!!!!!!!!!!!!!!!!")

data1=encode_val

with open("output.txt","w",encoding="utf-8") as f2:
    f2.write(data1)