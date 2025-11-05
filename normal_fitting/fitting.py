from scipy.stats import norm



class fit_binomial:
    def __init__(self,df):
        self.dframe=df

    def printdf(self):
        print(self.dframe)

    def makeContinuous(self):
        low=self.dframe.iloc[0,1]
        high=self.dframe.iloc[1,0]
        difference=(high-low)/2
        self.dframe['lower']=self.dframe['lower']-difference
        self.dframe['upper']=self.dframe['upper']+difference
        
    def findMeanVariance(self):
        df=self.dframe.copy()
       
        
        df['xi']=(df['lower']+((df['upper']-df['lower'])/2))
        df['xifi']=df['xi']*df['freq']
        self.N=df['freq'].sum()
        sum_xifi=df['xifi'].sum()
        self.mean=sum_xifi/self.N
        
        df['xi2fi']=(df['xi']**2)*(df['freq'])
        self.variance=((df['xi2fi'].sum()/self.N))-(self.mean)**2
        self.sigma=(self.variance)**0.5
        # print(N)
        # print(df['xifi'].sum())
        # print(df)
        return self.mean,self.variance
        


    def addPhi(self):
        self.dframe['phi1']=norm.cdf(self.dframe['z1'])
        self.dframe['phi2']=norm.cdf(self.dframe['z2'])
        self.dframe['del_phi']=self.dframe['phi2']-self.dframe['phi1']
        

    def addZ(self):
        self.dframe['z1']=((self.dframe['lower']-self.mean)/self.sigma)
        self.dframe['z2']=((self.dframe['upper']-self.mean)/self.sigma)

    def ndelta(self):
        self.dframe['N_del_phi']=self.dframe['del_phi']*self.N
        # print(self.dframe['N_del_phi'].sum())

class fitting_binomial:
    def __init__(self,df):
        self.newdf=fit_binomial(df)

    
    def fit(self):
        self.newdf.makeContinuous()
        self.newdf.findMeanVariance()
        self.newdf.addZ()
        self.newdf.addPhi()
        self.newdf.ndelta()
        self.newdf.printdf()

