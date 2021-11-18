#include <iostream>
#include <cstdlib>
using namespace std;

double mean(double *a,int n) {
	double s = 0;
	for (int k = 0; k < n; k++) {
		s += a[k];
	}
	return s / n;
}

int main() {
	double A[] = { 3,6,5,2,3 }, B[] = {4,5,-2};
	cout << "Mean value for values of array 'A'= " << mean(A, 5) << "\nMean value for values of array 'B'= " << mean(B, 3) << endl;
	system("pause>nul");
	return 0;
}