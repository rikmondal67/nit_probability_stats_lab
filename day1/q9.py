import pandas as pd
df=pd.read_csv('q9.csv')
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
    return mean,df
def findSD(df,mean):
    df['fi(xi-mean)^2']=(((df['xi']-mean)**2)*df['freq'])
    n=df['freq'].sum()
    numerator=df['fi(xi-mean)^2'].sum()
    sd=(numerator/n)**0.5
    return sd,df

mean,df=findMean(df)
sd,df=findSD(df,mean)

print(df.to_string())
print(f'Mean = {mean:.2f}')
print(f'Standard Deviation = {sd:.2f}')
