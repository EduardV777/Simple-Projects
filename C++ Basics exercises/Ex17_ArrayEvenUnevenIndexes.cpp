#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int k = 0, j = 0, choice = 0; const int size = 20; int Array[size];
	cout << "Creator of array with elements depending on the index: " << endl << endl;
	while (k < size) {
		if (k % 2 == 0) {
			Array[k] = k;
		}
		else if (k % 2 != 0) {
			Array[k] = k*k;
		}

		//cout << Array[k] << " || ";
		k++;
	}
	k = 0;
	while (true) { cout << "Do you want to output an array with the Fibonacci Sequence with length of 20?" << endl << "[1]-Yes" << endl << "[2]-No" << endl; cin >> choice; if (choice == 0 || choice < 1 || choice>2) { cout << endl << "Error: Choice is incorrect!" << endl << endl; continue; } else { break; } }
	if (choice == 1) {
		cout << endl << "Array Numbers: " << endl;
		while (k < size) {
			cout << Array[k] << " || ";
			k++;
		}
		cout << endl;
	}
	else if (choice == 2) {
		cout << endl << "Leaving program..." << endl;
		system("pause"); return 0;
	}
	system("pause");
	return 0;
}