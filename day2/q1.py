import pandas as pd
dataset='q1.csv'
median=0
def findMean(filename):
        df=pd.read_csv(filename)
        # df['xi']=((df.iloc[0,1]-df.iloc[0,0])/2)+df['lower']
        df['xi']=df['lower']
        middleRow=len(df)/2
        a=df.iloc[int(middleRow),3]
        # h=(df.iloc[0,1]-df.iloc[0,0])
        h=1
        df['di']=(df['xi']-a)/h
        df['difi']=df['di']*df['freq']
        mean=a+((h*df['difi'].sum())/df['freq'].sum())
        # print(df.to_string(index=False))
        # print(f'\n\nMean={mean}')

        #find the median

        df['|xi-mean|fi']=(abs(df['xi']-mean))*df['freq']
        mean_deviation=df['|xi-mean|fi'].sum()/df['freq'].sum()
        print(df)
        print(f'\n\nMean={mean}')
        print(f'mean_deviation about mean = {mean_deviation}')


        df['|xi-median|fi']=(abs(df['xi']-median))*df['freq']
        print(df)
        median_deviation=df['|xi-median|fi'].sum()/df['freq'].sum()
        print(f'mean deviation about median={median_deviation}')

        

def findMedian(data):
        df=pd.read_csv(data)
        df['f<']=df['freq'].cumsum()
        n2=(df['freq'].sum())/2
        half_len=len(df)/2
        h=1

        # print(n2)
        
        lowerRows=df[df['f<']<n2]
        HigherRows=df[df['f<']>=n2]

        
       


        
        lowerRows=lowerRows.iloc[-1]
        HigherRows=HigherRows.iloc[0]

        # print(lowerRows)
        # print(HigherRows)
        global median
        median=HigherRows['lower']+(((n2-lowerRows['f<'])*h)/HigherRows['freq'])
        print(f'median={median}')
        

findMedian(dataset)
findMean(dataset)