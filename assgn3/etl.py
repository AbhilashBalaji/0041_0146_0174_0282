import pandas as pd
from os import getcwd
df = pd.read_csv(getcwd()+"/assgn3/iris.csv")
df['sepal_copy'] = df['sepal_length'] # Copy column created
df1 = pd.DataFrame()
#removing copy
for i in df.columns:
    for j in df.columns:
        if df[i].dtype == df[j].dtype and type(df[i][0]) is not str and i != j:
            if int(df[i].corr(df[j])) == 1 and df[i][0] == df[j][0]:
                break
            df1[i] = df[i]
            
print(df1)
