import pandas as pd
df=pd.read_csv('q1.csv')
def findMean(df):
    h=df.iloc[0,1]-df.iloc[0,0]
    add=h/2
    df['xi']=df['lower']+add
    halflen=int(len(df)/2)
    a=df.loc[halflen,'xi']
    df['di']=(df['xi']-a)/h
    df['difi']=df['di']*df['freq']
    n=df['freq'].sum()
    mean=a+(h*(df['difi'].sum())/n)
    print(df)
    return mean


mean=findMean(df)
print(f'Mean is = {mean}')