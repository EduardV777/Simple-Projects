#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int exponent(int n,int x, int s=1, int k=1) {
	if (k > n) {
		return s;
	}
	else {
		s += s + pow(x, k) / k;
		k++;
		return exponent(n, x, s, k);
	}
}

int main() {
	int x, n;
	cout << "Enter the argument X to calculate the exponent for it: "; cin >> x; cout << "Enter n: "; cin >> n;
	cout << "Exponent result: " << exponent(n,x);
	cout << "\n\nCheck: " << exp(x);
	system("pause>nul");
	return 0;
}