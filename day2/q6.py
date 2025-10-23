import pandas as pd
dataset='q6.csv'
median=0
q3=0
q1=0
def findq1(data):
        df=pd.read_csv(data)
        df['f<']=df['freq'].cumsum()
        n2=(df['freq'].sum())/4
        half_len=len(df)/2
        h=df.iloc[0,1]-df.iloc[0,0]

        # print(n2)
        
        lowerRows=df[df['f<']<n2]
        HigherRows=df[df['f<']>=n2]

        
       


        
        lowerRows=lowerRows.iloc[-1]
        HigherRows=HigherRows.iloc[0]

        # print(lowerRows)
        # print(HigherRows)
        global median
        median=HigherRows['lower']+(((n2-lowerRows['f<'])*h)/HigherRows['freq'])
        print(f'q1={median}')
        return median

def findq3(data):
        df=pd.read_csv(data)
        df['f<']=df['freq'].cumsum()
        n2=(df['freq'].sum())*3/4
        half_len=len(df)/2
        h=df.iloc[0,1]-df.iloc[0,0]

        # print(n2)
        
        lowerRows=df[df['f<']<n2]
        HigherRows=df[df['f<']>=n2]

        
       


        
        lowerRows=lowerRows.iloc[-1]
        HigherRows=HigherRows.iloc[0]

        # print(lowerRows)
        # print(HigherRows)
        global median
        median=HigherRows['lower']+(((n2-lowerRows['f<'])*h)/HigherRows['freq'])
        print(f'q3={median}')
        return median

def findN(filename):
        df=pd.read_csv(filename)
        sum=df['freq'].sum()
        return sum

def findMedian(data):
        df=pd.read_csv(data)
        df['f<']=df['freq'].cumsum()
        n2=(df['freq'].sum())/2
        half_len=len(df)/2
        h=df.iloc[0,1]-df.iloc[0,0]

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
        return median

def quartiledeviation(val1:float,val2:float)->float:
        val1=float(val1)
        val2=float(val2)
        qd=(val1-val2)/2
        coeff=(val1-val2)/(val1+val2)
        # print(f'quartile deviation = {qd}')
        # print(f'coefficient = {qd}')
        return coeff,qd


def findQ(data,val):
        df=pd.read_csv(data)
        df['f<']=df['freq'].cumsum()
        # n2=(df['freq'].sum())/2
        n2=val
        half_len=len(df)/val
        h=df.iloc[0,1]-df.iloc[0,0]

        # print(n2)
        
        lowerRows=df[df['f<']<n2]
        HigherRows=df[df['f<']>=n2]

        
       


        
        lowerRows=lowerRows.iloc[-1]
        HigherRows=HigherRows.iloc[0]

        # print(lowerRows)
        # print(HigherRows)
        global median
        median=HigherRows['lower']+(((n2-lowerRows['f<'])*h)/HigherRows['freq'])
        # print(f'median={median}')
        return median
 

# q1=findq1(dataset)
# q3=findq3(dataset)
# findMedian(dataset)
# quartiledeviation(q3,q1)
n=(findN(dataset))

n1=n/4
n3=(3*n)/4

q1=findQ(dataset,n1)
q3=findQ(dataset,n3)
print(f'q1={q1:.3f}')
print(f'q3={q3:.3f}')
qd=quartiledeviation(q3,q1)
print(f'Quartile Deviation{qd[1]:.2f}')
print(f'Coeffecient of the quartile deviation{qd[0]:.2f}')

# findMean(dataset)