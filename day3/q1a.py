import pandas as pd
import numpy as np
import math
# from decimal import decimal,getcontext
df=pd.read_csv('q1.csv')

def findP(df):
    df['xf']=df['x']*df['freq']
    numerator=df['xf'].sum()
    denominator=df['freq'].sum()
    p=numerator/denominator
    p=(p/df.iloc[-1]['x'])
    return p


def fitBinomial(df):
    n=df.iloc[-1]['x'].round(4)
    x=df.loc[0,'x'].round(4) # x for the ncx
    N=df['freq'].sum().round(4)
    df['(n-x)/(x+1)']=((n-df['x'])/(df['x']+1)).round(4)
    p=findP(df)
    q=(1-p)
    df['(n-x)p/(x+1)q']=((df['(n-x)/(x+1)']*p)/q).round(4)
    df['p(x)']=np.nan

    # print((math.comb(n,x)*(p**x)*(q**(n-x))))
    df.loc[0,'p(x)']=(math.comb(n,x)*(p**x)*(q**(n-x))).round(4)
    
    for i in range(1,len(df)):
        df.loc[i,'p(x)']=(df.loc[(i-1),'(n-x)p/(x+1)q']*df.loc[(i-1),'p(x)']).round(4)

    df['E']=(df['p(x)']*df['freq']).round(4)

    df['p(x)']=df['p(x)'].round(4)

    

    return df,p,q



df,p,q=fitBinomial(df)
print(df)


print(f'The Sum is {df['p(x)'].sum():.4f}')
print(f'P={p:.2f}')
print(f'q={q:.2f}')
print(f'p/q={(p/q)}')
