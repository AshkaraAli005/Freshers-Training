import csv

class Employee():

    def __init__(self,id,name,city):

        self.id = id

        self.name = name

        self.city = city

list1 = []

with open('employee3.csv','r') as data:

    value = csv.DictReader(data)

    for item in value:

        emp = Employee(int(item['Id']),item['Name'],item['City'])

        list1.append(emp)

for object in list1:

    print(object.id," ",object.name," ",object.city)

