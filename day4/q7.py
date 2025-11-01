import pandas as pd
df=pd.read_csv('q7.csv')
def correctValue(df,n,sum_x,sum_x2,sum_y,sum_y2,sum_xy):
    sum_x=sum_x-df['w_x'].sum()+df['c_x'].sum()
    sum_y=sum_y-df['w_y'].sum()+df['w_y'].sum()


    df['wx2']=df['w_x']**2
    df['wy2']=df['w_y']**2
    df['cx2']=df['c_x']**2
    df['cy2']=df['c_y']**2


    df['c_xy']=df['c_x']*df['c_y']
    df['w_xy']=df['w_x']*df['w_y']



    sum_x2=sum_x2-(df['wx2'].sum())+(df['cx2'].sum())
    sum_y2=sum_y2-(df['wy2'].sum())+(df['cy2'].sum())

    sum_xy=sum_xy-(df['w_xy'].sum())+(df['c_xy'].sum())

    print(df)

    mean_x=sum_x/n
    mean_y=sum_y/n

    cov=((sum_xy/n)-(mean_x*mean_y))
      
    sigma_x=((sum_x2/n)-(mean_x)**2)**0.5
    sigma_y=((sum_y2/n)-(mean_y)**2)**0.5

    r=cov/(sigma_x*sigma_y)

    return r





r=correctValue(df,25,125,650,100,460,508)
print(f'The r is {r}')