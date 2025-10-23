import pandas as pd
data2='q2.csv'
def findMean(filename):
        
        df=pd.read_csv(filename)
        #print(df)
        df['xi']=((df.iloc[0,1]-df.iloc[0,0])/2)+df['lower']
        df['xi']=df['lower']
        middleRow=len(df)/2
        a=df.iloc[int(middleRow),0]
        # print(f'a={a}')
        h=(df.iloc[0,1]-df.iloc[0,0])
        # h=1
        df['di']=(df['xi']-a)/h
        df['difi']=df['di']*df['freq']
        mean=a+((h*df['difi'].sum())/df['freq'].sum())
        # print(mean)


     

        df['|xi-mean|fi']=(abs(df['xi']-mean))*df['freq']
        mean_deviation=df['|xi-mean|fi'].sum()/df['freq'].sum()
        print(df)

        print(f'\n\nMean={mean+2}')
        
        print(f'mean_deviation about mean = {mean_deviation}')

findMean(data2)
