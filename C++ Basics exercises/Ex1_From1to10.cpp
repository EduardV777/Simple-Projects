#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "Natural numbers from 1 to 10: " << endl << endl;
	int n = 1;
	while (n <= 10) {
		cout << n << " || ";
		n += 1;
	}
	cout << endl;
	system("pause");
	return 0;
}