import pandas as pd

df=pd.read_csv('q2.csv')

def findGoodness(df,tabulated_value):
    a=df.loc[0,'a']
    b=df.loc[0,'b']
    c=df.loc[0,'c']
    d=df.loc[0,'d']

    N=a+b+c+d

    numerator=N*(((a*d)-(b*c))**2)
    denominator=((a+b)*(a+c)*(c+d)*(b+d))

    chi2=(numerator/denominator).round(6)
    print(f'The chi2 value is = {chi2}')

    if(chi2<tabulated_value):
        return True
    return False

good=findGoodness(df,0.957)

if(good==True):
    print('The hypothesis may be accepted')
else:
    print("The Hypothesis Rejected")

