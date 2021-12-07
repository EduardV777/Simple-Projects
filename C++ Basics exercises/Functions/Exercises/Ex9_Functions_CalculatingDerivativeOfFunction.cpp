#include <iostream>
#include <cstdlib>
using namespace std;
//variant 1
double CalculateDx(double F(double,double), double arg, double h) {
	h = arg;
	return (F(arg,h)-F(arg,0))/h;
}

//variant 2
double CalculateDx(double F(double, double), double* arr, double* arrResults, double h=0) {
	for (int k = 0; k < 8; k++) {
		h = arr[k];
		arrResults[k] = (F(arr[k], h) - F(arr[k], 0)) / h;
	}
	return *arrResults;
}

double F(double arg, double h = 0) {
	if (h > 0) {
		return 2 * (arg + h) + 35 / 5;
	}
	return 2 * arg + 35 / 5;
}

int main() {
	//variant 1
	/*
	double argument;
	cout << "F(x) = 2x+35/5" << "\nEnter the point at which you want to calculate the derivative of F: "; cin >> argument;
	double(*Fx)(double, double);
	Fx = F;
	cout << "F'(" << argument << ") = " << CalculateDx(Fx, argument, argument);
	*/

	//variant 2
	double* arguments = new double[8]; double* results = new double[8];
	double(*Fx)(double, double);
	Fx = F;
	srand(2);
	for (int k = 0; k < 8; k++) {
		arguments[k] = 1 + rand() % 25;
	}
	cout << "F(x) = 2x+35/5\nDifferent points generated...\n";
	CalculateDx(Fx, arguments, results);
	for (int k = 0; k < 8; k++) {
		cout << "F'(" << arguments[k] << ") = " << results[k]<<"\n";
	}
	system("pause>nul");
	return 0;
}