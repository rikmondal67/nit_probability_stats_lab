import pandas as pd
q5='q5.csv'

def findMean(filename):
        df=pd.read_csv(filename)
        df['xi']=((df.iloc[0,1]-df.iloc[0,0])/2)+df['lower']
        # df['xi']=df['lower']
        middleRow=len(df)/2
        a=df.iloc[int(middleRow),3]
        h=(df.iloc[0,1]-df.iloc[0,0])
        # h=1
        df['di']=(df['xi']-a)/h
        df['difi']=df['di']*df['freq']
        mean=a+((h*df['difi'].sum())/df['freq'].sum())
        print(df)
        # print(mean)

        df['(xi-mean)^2fi']=((df['xi']-mean)**2)*df['freq']
        standard_deviation=df['(xi-mean)^2fi'].sum()
        standard_deviation=standard_deviation/df['freq'].sum()
        standard_deviation=standard_deviation**0.5
        print(f'standard_deviation={standard_deviation}')



mean=findMean(q5)


