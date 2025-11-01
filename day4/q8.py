import pandas as pd
from scipy.stats import norm
import numpy as np

def calculate_normal_fit():
    df = pd.read_csv('q8.csv')
    df['midpoint'] = (df['Lower'] + df['Upper']) / 2
    
    N = df['Freq'].sum()
    
    mean = (df['Freq'] * df['midpoint']).sum() / N
    
    df['diff_sq'] = (df['midpoint'] - mean) ** 2
    df['f_diff_sq'] = df['Freq'] * df['diff_sq']
    variance = df['f_diff_sq'].sum() / N
    std_dev = np.sqrt(variance)
    
    c = df['Upper'].iloc[0] - df['Lower'].iloc[0]
    
    
    print('\nEquation of the Normal Curve (Frequency Function)')
    amplitude = (N * c) / (std_dev * np.sqrt(2 * np.pi))
    print(f'y ≈ {amplitude:.2f} * exp(-0.5 * ((x - {mean:.3f}) / {std_dev:.3f})^2)')
    
    print('\nExpected Normal Frequencies')
    boundaries = np.array([df['Lower'].min() - 0.5] + df['Upper'].tolist())
    
    expected_frequencies = []
    
    for i in range(len(boundaries) - 1):
        z1 = (boundaries[i] - mean) / std_dev
        z2 = (boundaries[i+1] - mean) / std_dev
        
        prob_area = norm.cdf(z2) - norm.cdf(z1)
        expected_freq = N * prob_area
        expected_frequencies.append(expected_freq)
        
    df['Expected Freq'] = expected_frequencies
    
    print(df[['Lower', 'Upper', 'Freq', 'Expected Freq']].to_string(index=False))
    print(f'\nSum of Expected Frequencies: {df["Expected Freq"].sum():.1f}')


calculate_normal_fit()
