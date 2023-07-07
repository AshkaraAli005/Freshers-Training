
import csv

import requests

respons=requests.get("http://api.coincap.io/v2/assets")

first=respons.json()

header1,outdata=["rank","id","name"],[]

for x in first["data"]:

    list1=[x['rank'],x['id'],x['name']]

    outdata.append(list1)

with open("output.csv","w") as f1:

    writ=csv.writer(f1)

    writ.writerow(header1)

    writ.writerows(outdata)

print("CSV file updated..")