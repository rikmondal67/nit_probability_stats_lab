import pandas as pd

file='repeated_rank.csv'
df=pd.read_csv(file)

class findRank:
    def __init__(self,df):
        self.df=df.copy()
    def rank(self):
        self.df['rx']=self.df['x'].rank(ascending=False,method='average')
        self.df['ry']=self.df['y'].rank(ascending=False,method='average')
        self.df['di']=self.df['rx']-self.df['ry']
        self.df['di2']=self.df['di']**2
        n=len(df)
        self.x_dict={}
        self.y_dict={}
        self.x_dict=self.df['x'].value_counts().to_dict()
        self.y_dict=self.df['y'].value_counts().to_dict()
        self.x_m=0
        self.y_m=0
        for key,value in self.x_dict.items():
            if(value>1):
                self.x_m+=(value*((value**2)-1))
        for key,value in self.y_dict.items():
            if(value>1):
                self.y_m+=(value*((value**2)-1))
        self.x_m/=12
        self.y_m/=12
        self.total=self.x_m+self.y_m
        self.rank_value=1-6*((self.df['di2'].sum()+self.total)/(n*((n**2)-1)))
        
        return self.rank_value
        

q=findRank(df)
rank=q.rank()
print(q.df)
print(f"The rank of the given Data is {rank:.4f}")
