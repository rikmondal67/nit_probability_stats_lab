import pandas as pd

df=pd.read_csv('q7.csv')

def findRank(df):
    rval=4
    df['rx']=df['x'].rank(method='average',ascending=False)
    df['ry']=df['y'].rank(method='average',ascending=False)

    df['di']=(df['rx']-df['ry']).round(rval)

    df['di2']=(df['di']**2).round(rval)

    n=df['rx'].max()

    #important syntax
    #converting the repeatation into a dictonary
    

    x_count=df['x'].value_counts().to_dict()
    y_count=df['y'].value_counts().to_dict()

    x_m=0
    y_m=0

    for key,value in x_count.items():
        if(value>1):
            x_m+=((value*((value**2)-1))/12)

    print(x_m)

    for key,value in y_count.items():
        if(value>1):
            y_m+=((value*((value**2)-1))/12)

    print(y_m)

    m=x_m+y_m

    n=len(df)


    r=(1-(6*((df['di2'].sum().round(rval))+m))/(n*((n**2)-1))).round(rval)

    # print(r)

    # print(df)

    return r.round(rval),df

r,df=findRank(df)

print(df)
print(f'The Coefficient Cofactor is {r}')
