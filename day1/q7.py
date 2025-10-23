import pandas as pd
df=pd.read_csv('q7.csv')
def findMode(df):
    h=df.loc[0,'upper']-df.loc[0,'lower']
    modalid=df['freq'].idxmax()
    modal=df.loc[modalid]
    premodal=df.loc[modalid-1]
    postmodal=df.loc[modalid+1]
    delta1=modal['freq']-premodal['freq']
    delta2=modal['freq']-postmodal['freq']
    # denominator=(2*modal['freq'])-premodal['freq']-postmodal['freq']
    # print(denominator)
    # print(premodal)
    # print(postmodal)
    # print(modal)
    mode=(modal['lower']+((modal['freq']-premodal['freq'])/((2*modal['freq'])-premodal['freq']-postmodal['freq']))*h)
    return mode
    # print(modalid)

mode=findMode(df)
print(f'Mode = {mode:.2f}')