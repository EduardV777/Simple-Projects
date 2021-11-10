#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main() {
	int n, k = 1;
	double x;
	cout << "Calculating sinus for argument 'x':" << endl << endl;
	cout << "How much numbers do you want to process? - "; cin >> n; cout << endl;
	for (; k <= n; k++) {
		cout << endl << "Enter value for 'x': "; cin >> x;
		cout << endl << "sin(" << x << ") = " << sin(x) << endl;
	}
	cout << endl << "Action finished!" << endl;
	system("pause>nul");
	return 0;
}