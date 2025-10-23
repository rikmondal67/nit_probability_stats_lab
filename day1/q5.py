import pandas as pd
df=pd.read_csv('q5.csv')
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

def findMedian(df):
    df['f<']=df['freq'].cumsum()
    n=df['freq'].sum()
    n2=n/2
    upperClass=df[df['f<']>=n2]
    lowerClass=df[df['f<']<n2]
    upperRow=upperClass.iloc[0]
    lowerRow=lowerClass.iloc[-1]
    h=upperRow['upper']-upperRow['lower']
    median=upperRow['lower']+((n2-lowerRow['f<'])*h)/upperRow['freq']
    return median
    
mean=findMean(df)
median=findMedian(df)
print(f'Mean = {mean:.2f}')
print(f'Median = {median:.2f}')
    