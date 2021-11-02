#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "Generator of binomial coefficients: " << endl << endl;
	const int size = 100;
	int bnm[size], n = 0, j = 0, k = 1; bnm[0] = 1;
	while (true) {
		cout << "Input a value for sub-index 'n' - "; cin >> n;
		if (n <= 1) {
			cout << endl << "Error: Sub-index 'n' must have a value higher than 1! Try again." << endl;
			continue;
		}
		else if (n > 99) {
			cout << endl << "Error: Sub-index 'n' must have a value lower than 99! Try again." << endl;
			continue;
		}
		else {
			break;
		}
	}
	cout << "Binomial coefficients: " << endl << endl;
	while (j <= n) {
		bnm[j + 1] = bnm[j]*(n - k) / (k + 1);
		cout << bnm[j]<<" || ";
		j++, k++;
	}
	cout << endl;
	system("pause");
	return 0;
}