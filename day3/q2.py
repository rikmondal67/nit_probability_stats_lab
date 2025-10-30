import pandas as pd
import numpy as np
import math
df=pd.read_csv('q2.csv')
def fitPoisson(df):
    df['xf']=df['x']*df['freq']
    mean=df['xf'].sum()
    mean=(mean/(df['freq'].sum()))
    # print(mean)
    df['mean/x+1']=mean/(df['x']+1)
    df['p(x)']=np.nan
    p0=math.exp(-mean)
    print(f'mean={mean}')
    print(f'p0={p0}')
    df.loc[0,'p(x)']=p0
    for i in range(1,len(df)):
        df.loc[i,'p(x)']=df.loc[i,'mean/x+1']*df.loc[i-1,'p(x)']

    
   


    # print((mean))

    # print(df)


    
fitPoisson(df)

