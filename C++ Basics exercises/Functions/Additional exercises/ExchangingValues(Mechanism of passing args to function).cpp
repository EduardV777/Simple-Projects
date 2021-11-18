#include <iostream>
#include <cstdlib>
using namespace std;

void swap(char a, char b) {
	cout << "First argument: " << a << "\nSecond argument: " << b << endl;
	for (int k = 0; k < 20; k++) {
		cout << "-";
	}
	cout << endl << "Exchanging values...\n";
	char temp = a; a = b; b = temp;
	cout << "First argument: " << a << "\nSecond argument: " << b <<"\nExecution of function swap() is over.\n\n";
}

int main() {
	char x = 'a', y = 'b';
	swap(x, y);
	cout << "Values of variables x and y:\n" << "x = " << x << "\ny = " << y << endl;
	system("pause>nul");
	return 0;
}