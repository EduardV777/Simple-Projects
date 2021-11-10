//
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main() {
	int n, k=1, x;
	cout << "Calculating the natural logarithm of different arguments('x'):" << endl << endl << "How much numbers do you want to test? - "; cin >> n;
	for (; k <= n; k++) {
		cout << endl << "Enter value for 'x': "; cin >> x;
		cout << endl << "LNe(" << x << ") = " << log(x) << endl; 
	}
	cout << endl << "Action finished!" << endl;
	system("pause>nul");
	return 0;
}