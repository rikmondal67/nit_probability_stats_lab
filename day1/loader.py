import pandas as pd
import numpy 
filename='q9.csv'
df=pd.read_csv(filename)
df['lower']=range(20,90,10)
df['upper']=range(30,100,10)
df['freq']=numpy.nan
# df['upper']=numpy.nan

print(df)

df.to_csv(filename,index=False)