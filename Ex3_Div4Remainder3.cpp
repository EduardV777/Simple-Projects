#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "Numbers that have remainder of 3 when divided by 4: " << endl << endl;
	int n=0;
	while (true) {
		cout << "How much numbers do you want to be displayed? - "; cin >> n;
		if (n <= 0) {
			cout << endl << "Error: This amount of numbers is invalid! Try again."<< endl;
			continue;
		}
		else {
			break;
		}
	}
	int k=1;
	while (n>0) {
		if (k % 4 == 3) {
			n--;
			cout << k << " || ";
		}
		k++;
	}
	cout << endl;
	system("pause");
	return 0;
}