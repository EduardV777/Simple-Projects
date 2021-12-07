#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;
//variant 1
int CalculatePolynomial(int* arr, int x) {
	int res = 0;
	for (int k = 0; k < 10; k++) {
		res += arr[k] * pow(x, k);
	}
	return res;
}
//variant 2
int CalculatePolynomial(int* arr) {
	for (int k = 0; k < 10; k++) {
		cout << arr[k] << ", ";
	}
	return 0;
}

int main() {
	int* values = new int[10];
	int x;
	cout << "Please enter value for x: "; cin >> x; cout << "\nAutomatically generating elements...\n";
	srand(2);
	for (int k = 0; k < 10; k++) {
		values[k] = 1 + rand() % 25;
	}
	//Variant 1
	/*
	cout << "(";
	for (int k = 0; k < 10; k++) {
		cout << values[k] << ", ";
	}
	cout << ")" << endl;

	cout << "Result = " << CalculatePolynomial(values, x) << endl;
	*/
	//Variant 2
	cout << CalculatePolynomial(values);
	system("pause>nul");
	return 0;
}