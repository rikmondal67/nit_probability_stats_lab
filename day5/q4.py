import pandas as pd

df=pd.read_csv('q4.csv')

def findGoodness(df):
    df = df.copy() 


    df['tot_col'] = df.sum(axis=1)
    df.loc[len(df)] = df.sum(axis=0)

    # Total grand sum
    N = df.iloc[-1, -1]


    ea = pd.DataFrame(0.0, index=range(len(df)-1), columns=range(df.shape[1]-1))
    chi_table = pd.DataFrame(0.0, index=range(len(df)-1), columns=range(df.shape[1]-1))

    
    for i in range(len(df)-1):
        for j in range(df.shape[1]-1):
            ea.iloc[i, j] = (df.iloc[i, -1] * df.iloc[-1, j]) / N


    for i in range(len(df)-1):
        for j in range(df.shape[1]-1):
            observed = df.iloc[i, j]
            expected = ea.iloc[i, j]
            chi_table.iloc[i, j] = ((observed - expected) ** 2) / expected


    chi_square_value = chi_table.values.sum()


    print("Modified DataFrame (with totals):")
    print(df)
    print("\nExpected values (Ea):")
    print(ea)
    print("\nChi-square contributions:")
    print(chi_table)
    print(f"\nTotal Chi-square statistic: {chi_square_value:.4f}")
    print(f"Total observations (N): {N}")

    return chi_square_value

findGoodness(df)