import math
import csv
import numpy as np
from scipy.stats import norm


def Phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def read_csv(file_name):
    lower = []
    upper = []
    freq = []
    with open(file_name, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lower.append(float(row[0]))
            upper.append(float(row[1]))
            freq.append(float(row[2]))
    return lower, upper, freq

# Write output to CSV
def write_output(file_name, mean, sd, max_area, expected_sum, expected_frequencies):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mean", mean])
        writer.writerow(["Standard Deviation", sd])
        writer.writerow(["Max Area", max_area])
        writer.writerow(["Expected Sum", expected_sum])
        writer.writerow(["Expected Frequencies"] + expected_frequencies)

# Main function
def main():
    lower, upper, freq = read_csv('q9.csv')  # Load data from CSV file
    n = len(lower)
    
    # Calculate midpoints and other statistics
    mid = [(l + u) / 2 for l, u in zip(lower, upper)]
    sum_fx = sum(m * f for m, f in zip(mid, freq))
    N = sum(freq)
    
    mean = sum_fx / N  # Mean
    
    sum_fdx2 = sum(f * (m - mean)**2 for m, f in zip(mid, freq))
    sd = math.sqrt(sum_fdx2 / N)  # Standard deviation
    
    expected = []
    for l, u in zip(lower, upper):
        z1 = (l - mean) / sd
        z2 = (u - mean) / sd
        p = Phi(z2) - Phi(z1)
        expected.append(N * p)
    
    # Output Results
    print(f"Mean (x̄): {mean:.4f}")
    print(f"Standard Deviation (σ): {sd:.4f}")
    
    # Equation of the Normal Curve
    print(f"\nEquation of Normal Curve:\n")
    print(f"f(x) = (1 / ({sd:.4f} * sqrt(2π))) * exp(-((x - {mean:.4f})^2) / (2 * {sd:.4f}^2))")

    # Max area given by the curve
    max_area = 2000 / (math.sqrt(2 * math.pi) * sd)
    print(f"\nMax area given by curve: {max_area:.4f}")

    # Expected Sum
    expected_sum = sum(expected)
    print(f"Expected Sum: {expected_sum:.4f}")

    # Write output to CSV
    write_output('output.csv', mean, sd, max_area, expected_sum, expected)

if __name__ == '__main__':
    main()
