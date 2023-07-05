import pandas as pd
csvFile1 = input('Enter csv1 file path : ')
csvFile2 = input('Enter csv2 file path : ')
mergedFile = input("Enter merged file path : ")

cf1 = pd.read_csv(csvFile1)
cf2 = pd.read_csv(csvFile2)
cc = list(set(cf1) & set(cf2))
combined = pd.merge(cf1,cf2,on = cc,how='inner')
combined.to_csv(mergedFile)