#include <iostream>
#include <cstdlib>
using namespace std;

int Sum(int a, int b) {
	int result = a + b;
	return result;
}

int main() {
	int a = 0, b = 0;
	cout << "This program will calculate the sum of natural numbers: " << endl << endl;
	while (true) { cout << "Value A: "; cin >> a; if (a < 0) { cout << endl << "Error: Value cannot be below 0" << endl << endl; continue; } else { break; } } while (true) { cout << endl << "Value B: "; cin >> b; if (b < 0) { cout << endl << "Error: Value cannot be below 0" << endl << endl; continue; } else { break; } }
	cout<<"Result = "<<Sum(a, b)<<endl;
	system("pause");
	return 0;
}