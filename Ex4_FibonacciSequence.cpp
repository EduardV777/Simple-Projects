#include <iostream>
#include <cstdlib>
using namespace std;
int Fibo() {
	int n = 0; int k = 0;
	while (true) {
		cout << "How much numbers of the fibonacci sequence do you want displayed? - "; cin >> n;
		if (n <= 0) {
			cout << "Error: That's invalid amount of numbers selected. Try again." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	int fibo[900]; fibo[0] = 1; fibo[1] = 1;
	cout << "Fibonnaci Sequence: " << endl;
	while (k <= n) {
		if (k == 0) {
			cout << fibo[0]<<" || ";
		}
		else if (k == 1) {
			cout << fibo[1] << " || ";
		}
		else {
			fibo[k] = fibo[k - 1] + fibo[k - 2];
			cout << fibo[k] << " || ";	
		}
		k++;
	}
	return 0;
}

int main() {
	cout << "//Generator of the fibonacci seqeuence//" << endl << endl;
	Fibo();
	system("pause");
	return 0;
}