# import pandas as pd 
# csv = pd.read_csv("employee2.csv")
# average = csv["Salary"].apply(lambda c : c/len(csv) ).mean()
# print(average)

n=int(input("Enter the number:"))

l=[]

found = False

for i in range(n):

    l.append(input())

c=input("Enter the value to be checked : ")

lst = lambda l:[(True) for x in l if c in x]

print(*lst(l))