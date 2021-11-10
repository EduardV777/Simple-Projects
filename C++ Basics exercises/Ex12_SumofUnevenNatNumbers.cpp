#include <iostream>
#include <cstdlib>
using namespace std;

int calculateSum(int a, int b) {
	return a + b;
}

int main() {
	int a = 0, b = 0;
	cout << "Sum calculator of uneven natural numbers: " << endl << endl;
	
	while (true) { cout << "Value A: "; cin >> a; if (a % 2 == 0 || a <= 0) { cout << endl << "Error: Number is not uneven! Try again." << endl << endl; continue; } else { break; } } while (true) { cout << endl << "Value B: "; cin >> b; if (b % 2 == 0 || b <= 0) { cout << endl << "Error: The number is not uneven! Try again." << endl << endl; continue; } else { break; } }
	cout << endl << "Result = " << calculateSum(a, b) << endl;
	system("pause");
	return 0;
}