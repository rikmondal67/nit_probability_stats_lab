import pandas as pd
df=pd.read_csv('q4.csv')
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
    

median=findMedian(df)
print(f'Median = {median:.2f}')
    