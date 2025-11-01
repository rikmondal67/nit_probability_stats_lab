#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;


double Phi(double z) {
    return 0.5 * (1.0 + erf(z / sqrt(2.0)));
}

int main() {
   
    vector<double> lower = {10.5, 20.5, 30.5, 40.5, 50.5, 60.5, 70.5};
    vector<double> upper = {20.5,30.5 , 40.5, 50.5, 60.5, 70.5, 80.5};
    vector<double> freq  = {12, 28, 40, 60, 32, 20, 8};

    int n = lower.size();
    vector<double> mid(n), expected(n);
    
    
    double sum_fx = 0.0, N = 0.0;
    for (int i = 0; i < n; i++) {
        mid[i] = (lower[i] + upper[i]) / 2.0;
        sum_fx += mid[i] * freq[i];
        N += freq[i];
    }
    double mean = sum_fx / N;

   
    double sum_fdx2 = 0.0;
    for (int i = 0; i < n; i++) {
        double d = mid[i] - mean;
        sum_fdx2 += freq[i] * d * d;
    }
    double sd = sqrt(sum_fdx2 / N);

  
    for (int i = 0; i < n; i++) {
        double z1 = (lower[i] - mean) / sd;
        double z2 = (upper[i] - mean) / sd;
        double p = Phi(z2) - Phi(z1);   
        expected[i] = N * p;           
    }

   
    cout << fixed << setprecision(4);
    cout << "Mean (x̄): " << mean << endl;
    cout << "Standard Deviation (σ): " << sd << endl;
    cout << "\nEquation of Normal Curve:\n";
    cout << "f(x) = (1 / (" << sd << " * sqrt(2π))) * exp(-((x - " 
         << mean << ")^2) / (2 * " << sd << "^2))" << endl;
     
     double ans = 2000/ (sqrt(2 * 3.14) * sd);
     cout<<"Max area given by curve : "<<ans<<endl;
    double ssum = 0;
    for (int i = 0; i < n; i++) {
        ssum += expected[i];
    }
    cout<<"Expected Sum: "<<ssum<<" "<<endl;

    return 0;
}

