import pandas as pd

df=pd.read_csv('q3.csv')



def findData(df):
    df['x2']=df['x']**2
    df['y2']=df['y']**2

    N=len(df)

    mean_x=df['x'].sum()/N
    mean_y=df['y'].sum()/N

    # print(mean_x)

    df['xy']=df['x']*df['y']

    mean_xy=mean_x*mean_y

    cov=((df['xy'].sum()/N)-mean_xy)

    # print(cov)

    sigma_x=((df['x2'].sum()/N)-((mean_x)**2))**0.5
    sigma_y=((df['y2'].sum()/N)-((mean_y)**2))**0.5

    r=cov/(sigma_x*sigma_y)

    # print(r)

    # print(df)

    return r,sigma_x,sigma_y,mean_x,mean_y,df

r,sigma_x,sigma_y,mean_x,mean_y,df=findData(df)

print(f'The corelation coefficient is {r}')

b_yx=(r*sigma_y)/sigma_x

print(f'The equation Line is : (y-{mean_y})={b_yx:.2f}*(x-{mean_x})')
    