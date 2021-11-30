#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int Process(int x) {
	return x;
}

int Process(int x, int x2) {
	return (x * x) + (x2 * x2);
}

int Process(int x, int x2, int x3) {
	return pow(x, 3) + pow(x2, 3) + pow(x2, 3);
}

int main() {
	int argCount;
	cout << "How much numbers do you want to process(max. 3): "; cin >> argCount; cout << endl;
	if (argCount == 1) {
		int x;
		cout << "\nEnter value for x: "; cin >> x; cout << "\nResult = "<<Process(x)<<endl;
	}
	else if (argCount == 2) {
		int x, x2;
		cout << "\nEnter value for x: "; cin >> x; cout << "\nEnter value for x2: "; cin >> x2; cout << "\nResult = " << Process(x, x2) << endl;
	}
	else if (argCount == 3) {
		int x, x2, x3;
		cout << "\nEnter value for x: "; cin >> x; cout << "\nEnter value for x2: "; cin >> x2; cout << "\nEnter value for x3: "; cin >> x3; cout << "\nResult = " << Process(x, x2, x3) << endl;
	}
	system("pause>nul");
	return 0;
}