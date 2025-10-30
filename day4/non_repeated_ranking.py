import pandas as pd

df=pd.read_csv('q2.csv')

def findRank(df):
    df['rx']=df['x'].rank(ascending=False)
    df['ry']=df['y'].rank(ascending=False)

    df['di']=df['rx']-df['ry']

    df['di2']=df['di']**2

    n=df['rx'].max()



    r=1-(6*(df['di2'].sum()))/(n*((n**2)-1))

    # print(r)

    # print(df)

    return r.round(5),df

r,df=findRank(df)

print(df)
print(f'The Coefficient Cofactor is {r}')