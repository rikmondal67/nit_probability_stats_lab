import pandas as pd
import numpy 
filename='q5.csv'
df=pd.read_csv(filename)
df['lower']=range(135,180,5)
df['upper']=range(140,176,5)
df['freq']=numpy.nan
# df['upper']=numpy.nan

print(df)

df.to_csv(filename,index=False)