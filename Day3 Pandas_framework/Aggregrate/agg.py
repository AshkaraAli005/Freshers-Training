import pandas as pd

csv1 = input('Enter csv 1 path : ')
csv2 =input('Enter csv 2 path : ')
output =input('Enter output file path : ')
cf1 = pd.read_csv(csv1)
cf2= pd.read_csv(csv2)
cc = list(set(cf1) & set(cf2))
merged = pd.merge(cf1,cf2,on=cc,how="left")
result = merged.groupby(['Id' , 'Name' , 'City'])['Performance'].mean()
result.to_csv(output)