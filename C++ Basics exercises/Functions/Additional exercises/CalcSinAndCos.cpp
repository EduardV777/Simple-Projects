#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;
//Declaring functions
double myCos(double);
double mySin(double);
void show(double);

	int main() {
		const double pi = 3.141592;
		show(pi / 6);
		show(pi / 4);
		show(pi / 3);
		show(pi / 2);
	system("pause>nul");
	return 0;
}

double myCos(double x) {
	int n = 100;
	double s = 0, q = 1;
	for (int k = 0; k <= n; k++) {
		s += q;
		q *= (-1) * x * x / (2 * k + 1) / (2 * k + 2);
	}
	return s;
}

double mySin(double x) {
	int n = 100;
	double s = 0, q = x;
	for (int k = 0; k <= n; k++) {
		s += q;
		q *= (-1) * x * x / (2 * k + 2) / (2 * k + 3);
	}
	return s;
}

void show(double x) {
	cout << "Value of argument: " << x << endl;
	cout << "Cos: " << myCos(x) << " vs. " << cos(x) << endl;
	cout << "Sin: " << mySin(x) << " vs. " << sin(x) << endl;
	cout << endl;

}