import csv
dict1 = {}

with open('employee3.csv','r') as data:

    value = csv.DictReader(data)

    for item in value:
        dict1[item["Id"]] = item
emp = input("Enter the Key :")
for object in dict1[emp]:

    print(object + " : "+ dict1[emp][object] )

