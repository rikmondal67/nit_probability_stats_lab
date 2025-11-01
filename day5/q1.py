import pandas as pd
filename='q1.csv'

df=pd.read_csv(filename)


def fitNormal(df):
    mid=df.iloc[0,1]-df.iloc[0,0]
    mid=mid/2

    df['xi']=df['lower']+mid

    a=df.loc[int(len(df))/2,'xi']
    
    h=df.iloc[0,0]-df.iloc[1,0]

    df['di']=(df['xi']-a)/h

    df['difi']=df['di']*df['fi']

    df['di2fi2']=(df['di']**2) * (df['fi']**2)


    df['xifi']=df['xi']*df['fi']

    N=df['fi'].sum()

    mean=df['xifi'].sum()/N

    df['xi2fi']=(df['xi']**2)*(df['fi'])

    variance=((df['xi2fi'].sum()/N)-(mean)**2)**1/2

    # print(variance)
    # print(mean)


    # print(df)
    return df,mean,variance

df,mean,variance=fitNormal(df)
print("The Table is")
print(df)
print(f'Mean is {mean}')
print(f'Variance is {variance}')