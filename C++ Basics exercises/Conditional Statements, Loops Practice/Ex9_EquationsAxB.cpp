#include <iostream>
#include <cstdio>
using namespace std;
int main() {
	double A, B, res;
	cout << "Solving Ax=B type of equations" << endl << endl;
	cout << "Enter value for parameter 'A': "; cin >> A; cout << endl;
	cout << "And enter value for parameter 'B': "; cin >> B; cout << endl;
	if (A != 0) {
		res = B / A;
		cout << endl << "x = " << res << endl;
	}
	else if (B != 0) {
		cout << endl << "No solution to the equation!(A=0 and B is not 0)" << endl;
	}
	else {
		cout << endl << "Every number is solution to the equation!" << endl;
	}
	cout << endl << "Action complete!" << endl;
	system("pause>nul");
	return 0;
}