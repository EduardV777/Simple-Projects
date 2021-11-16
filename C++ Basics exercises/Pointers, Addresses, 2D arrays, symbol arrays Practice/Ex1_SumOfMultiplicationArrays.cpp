#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Array1[10], Array2[10], randNum, randNum2, sum=0;
	srand(2);
	for (int k = 0; k < 10; k++) {
		randNum = 1 + rand() % 25; randNum2 = 1 + rand() % 25;
		Array1[k] = randNum; Array2[k] = randNum2;
	}
	/*
	for (int& x : Array1) {
		cout << x << " || ";
	}
	cout << endl;
	for (int& x : Array2) {
		cout << x << " || ";
	}
	cout << endl;
	for (int k = 0; k < 10; k++) {
		sum += Array1[k] * Array2[k];
		cout << sum << endl;
	}
	*/
	cout << endl;
	cout << sum;
	system("pause>nul");
	return 0;
}