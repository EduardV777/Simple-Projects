#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "User generated array with 5 elements: " << endl << endl;
	int k = 0, choice = 0, ui=0; const int size = 5; int Array[size];
	while (k < size) {
		cout << "Value for element index " << k << ": "; cin >> ui;
		Array[k] = ui;
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