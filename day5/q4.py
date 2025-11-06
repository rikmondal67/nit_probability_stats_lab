#question on the ranking 

import pandas as pd

df=pd.read_csv('q5.csv')


def findGoodness(df):
    df['tot_cols']=df.sum(axis=1)
    df.loc[len(df)]=df.sum(axis=0)

    N=df.iloc[-1,-1]
    total=0

    expectation_table=pd.DataFrame(0.0,index=range(df.shape[0]-1),columns=range(df.shape[1]-1))

    for i in range (expectation_table.shape[0]):
        for j in range (expectation_table.shape[1]):
            expectation_table.loc[i,j]=(df.iloc[i,-1]*df.iloc[-1,j])/N

    for i in range (expectation_table.shape[0]):
        for j in range(expectation_table.shape[1]):
            numerator=(df.iloc[i,j]*expectation_table.iloc[i,j])**2
            denominator=expectation_table.iloc[i,j]
            total=total+(numerator/denominator)
            
    dct=expectation_table.values.sum()
    print(dct)
    # print(df)
    # print(expectation_table)



findGoodness(df)