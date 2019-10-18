import pandas as pd 
df=pd.read_csv('iris.csv')
print(df.corr(method=pearson))
