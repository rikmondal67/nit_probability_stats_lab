import pandas as pd
from fitting import *
df=pd.read_csv('binomial_data.csv')
fb=fitting_binomial(df)
fb.fit()




