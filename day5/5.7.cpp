#include <bits/stdc++.h>
using namespace std;

int main(){
	double mean_y = 170, mean_x = 75, r = 0.60, sd_y = 6.0, sd_x = 6;
	// y: height
	// x: weight
	double byx = r*sd_y/sd_x;
	double bxy = r*sd_x/sd_y;
	double ht_amit = mean_y - byx*(mean_x-50);
	double wt_sumit = mean_x - bxy*(mean_y - 150); 
	cout << ht_amit << endl << wt_sumit << endl;
	return 0;
}

