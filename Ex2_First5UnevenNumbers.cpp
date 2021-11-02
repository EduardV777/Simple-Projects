#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "First five uneven numbers displayed below: " << endl << endl;
	int n = 1, k = 1;
	while (n <= 5) {
		cout << k << " || ";
		n += 1; k += 2;
	}
	cout << endl;
	system("pause");
	return 0;
}