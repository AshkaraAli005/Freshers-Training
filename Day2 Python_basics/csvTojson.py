import csv
import json
csvPath = input("Enter CSV file path : ")
jsonPath = input("Enter json file path : ")
askey = input('Enter primary key : ')
dataDict = {}
with open(csvPath ,'r') as csvHandler:
    reader = csv.DictReader(csvHandler)
    for row in reader:
        key = row[askey.lower()]
        dataDict[key] = row
with open(jsonPath, 'w') as jsonHandler:
    jsonHandler.write(json.dumps(dataDict, indent=4))