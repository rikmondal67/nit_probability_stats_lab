import pandas as pd
q3='q3.csv'

def findmean(data):
    df=pd.read_csv(data)
    mean=df['value'].sum()/df.shape[0]
    return mean
def standardDeviation(data,mean):
    df=pd.read_csv(data)
    df['sd']=(df['value']-mean)**2
    standard_deviation=df['sd'].sum()/df.shape[0]
    # print(standard_deviation)
    # print(df)
    return (standard_deviation**0.5)

print(f'mean={findmean(q3)}')
mean=findmean(q3)
print(f'standardDeviation={standardDeviation(q3,mean)}')