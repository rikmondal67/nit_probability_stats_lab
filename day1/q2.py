import pandas as pd
df=pd.read_csv('q2.csv')
def findMean(df):
    # h=df.iloc[0,1]-df.iloc[0,0]
    h=1
    # add=h/2
    add=0
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
print(f'Mean is = {mean:.2f}')