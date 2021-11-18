//Passing arguments to function with the help of reference args in definition, so they can be passed with their actual value and not a copy of it
#include <iostream>
#include <cstdlib>
using namespace std;

void swap(char &a, char &b) {
	cout << "First argument: " << a << "\nSecond argument: " << b << endl;
	for (int k = 0; k < 20 ; k++) {
		cout << "-";
	}
	cout << "\nExchanging values...\n\n";
	char temp = a; a = b; b = temp;
	cout << "\nFirst argument: " << a << "\nSecond argument: " << b << "\nExecution of swap() function is over\n\n";
}

int main() {
	char x = 'a', y = 'b';
	swap(x, y);
	cout << "Values of var x: " << x << "\nValue of var y: " << y << endl;
	system("pause>nul");
	return 0;
}