#include <iostream>
#include <cstdlib>
using namespace std;

void BinomCoef(int n, int k, int *bnm) {
	bnm[0] = 1;
	for (; k < n; k++) {
		bnm[k+1]= bnm[k]*(n-k)/(k+1);
	}
	for (k = 0; k <= n; k++) {
		cout << bnm[k] << " || ";
	}
}

int main() {
	int n, k;
	cout << "Enter n: "; cin >> n; cout << "\nEnter k: "; cin >> k;
	int* bnm = new int[n];
	cout << endl << "Result: ["; BinomCoef(n, k, bnm); cout << "]\n";
	system("pause>nul");
	return 0;
}