import pandas as pd
import numpy as np
import math
# from decimal import decimal,getcontext
df=pd.read_csv('q3.csv')

def findP(df):
    df['xf']=df['x']*df['freq']
    numerator=df['xf'].sum()
    denominator=df['freq'].sum()
    p=numerator/denominator
    p=(p/df.iloc[-1]['x'])
    return p


def fitBinomial(df):
    rval=7
    n=df.iloc[-1]['x'].round(rval)
    x=df.loc[0,'x'].round(rval) # x for the ncx
    N=df['freq'].sum().round(rval)
    df['(n-x)/(x+1)']=((n-df['x'])/(df['x']+1)).round(rval)
    p=findP(df)
    q=(1-p)
    df['(n-x)p/(x+1)q']=((df['(n-x)/(x+1)']*p)/q).round(rval)
    df['p(x)']=np.nan

    # print((math.comb(n,x)*(p**x)*(q**(n-x))))
    df.loc[0,'p(x)']=(math.comb(n,x)*(p**x)*(q**(n-x))).round(rval)
    
    for i in range(1,len(df)):
        df.loc[i,'p(x)']=(df.loc[(i-1),'(n-x)p/(x+1)q']*df.loc[(i-1),'p(x)']).round(rval)

    df['E']=(df['p(x)']*df['freq']).round(rval)

    df['p(x)']=df['p(x)'].round(rval)

    

    return df,p,q



df,p,q=fitBinomial(df)
print(df)


print(f'The Sum is {df['p(x)'].sum():.3f}')
print(f'P={p:.3f}')
print(f'q={q:.3f}')
print(f'p/q={(p/q)}')
print(f'sum of p is {df['p(x)'].sum():.9f}')
