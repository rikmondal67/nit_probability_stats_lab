import pandas as pd
from fitting import *
df=pd.read_csv('q1.csv')
fb=fitting_binomial(df)

fb.fit()




