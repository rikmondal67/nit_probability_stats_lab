import pandas as pd
q4='q4.csv'

def findmean(data):
    df=pd.read_csv(data)
    df['xifi']=df['value']*df['freq']
    print(df)
    mean=df['xifi'].sum()/df['freq'].sum()

    #for standard deviation

    df['sd']=((df['value']-mean)**2)*df['freq']
    standard_deviation=df['sd'].sum()/df['freq'].sum()
    standard_deviation=(standard_deviation**0.5)
    print(standard_deviation)
    print(mean)
    # return [mean,standard_deviation]



def standardDeviation(data,mean):
    df=pd.read_csv(data)
    df['sd']=(df['value']-mean)**2
    standard_deviation=df['sd'].sum()/df.shape[0]
    # print(standard_deviation)
    # print(df)
    return (standard_deviation**0.5)

# print(f'mean={findmean(q3)}')
# mean=findmean(q3)
findmean(q4)
# print(f'standardDeviation={standardDeviation(q3,mean)}')