//using pointers
#include <iostream>
#include <cstdlib>
using namespace std;

void swap(char* a, char* b) {
	cout << "First argument: " << *a << "\nSecond argument: " << *b << endl;
	for (int k = 0; k < 20; k++) {
		cout << "-";
	}
	cout << "\nExchanging values...\n";
	char temp = *a; *a = *b; *b = temp;
	cout << "First argument: " << *a << "\nSecond argument: " << *b << "\nExecution of swap() function is over.\n\n";
}

int main() {
	char x = 'a', y = 'b';
	swap(&x, &y);
	cout << "Value of var x: " << x << "\nValue of var y: " << y << endl;
	system("pause>nul");
	return 0;
}