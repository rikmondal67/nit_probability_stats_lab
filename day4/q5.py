import pandas as pd
import math

df=pd.read_csv('q5.csv')



def findData(df):
    rval=2
    df['x2']=(df['x']**2).round(rval)
    df['y2']=(df['y']**2).round(rval)

    N=len(df)

    mean_x=df['x'].sum().round(rval)/N
    mean_y=df['y'].sum().round(rval)/N

    # print(mean_x)

    df['xy']=df['x'].round(rval)*df['y'].round(rval)

    mean_xy=mean_x*mean_y

    cov=((df['xy'].sum()).round(rval)/N)-mean_xy.round(rval)

    # print(cov)

    sigma_x=(((df['x2'].sum()/N)-((mean_x)**2))**0.5).round(rval)
    sigma_y=(((df['y2'].sum()/N)-((mean_y)**2))**0.5).round(rval)

    r=cov/(sigma_x*sigma_y).round(rval)

    # print(mean_x)
    # print(mean_y)

    # print(r)

    # print(df)

    return r.round(rval),sigma_x.round(rval),sigma_y.round(rval),mean_x.round(rval),mean_y.round(rval),df

def predict(r,sigma_x,sigma_y,mean_x,mean_y,b_yx,x):
    y=mean_y+(b_yx*(x-mean_x))
    return y
    

r,sigma_x,sigma_y,mean_x,mean_y,df=findData(df)

print(f'The corelation coefficient is {r}')

b_yx=((r*sigma_y)/sigma_x).round(5)

print(f'The equation Line is : (y-{mean_y:.2f})={b_yx:.2f}*(x-{mean_x})')

user_input=int(input("enter the value of x"))

res=predict(r,sigma_x,sigma_y,mean_x,mean_y,b_yx,user_input)
print(f'The expected value of the sales is {res}')