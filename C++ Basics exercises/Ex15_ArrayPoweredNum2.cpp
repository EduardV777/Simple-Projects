#include <iostream>
#include <cstdlib>
using namespace std;

int powerTwo(int incrementing_power) {
	int pow2 = 2, k=1;
	while (k <= incrementing_power) {
		pow2 *= 2;
		k++;
	}
	return pow2;
}

int main() {
	cout << "Creator of array with the powers of the number 2: " << endl << endl;
	int k = 0, pow = 1, choice=0; const int size = 10; int Array[size];
	while (k < size) {
		Array[k] = powerTwo(pow);
		pow += 1, k++;
	}
	k = 0;
	while (true) { cout << "Do you want to output an array with 10 different powers of the number 2?" << endl << "[1]-Yes" << endl << "[2]-No" << endl; cin >> choice; if (choice == 0 || choice < 1 || choice>2) { cout << endl << "Error: Choice is incorrect!" << endl << endl; continue; } else { break; } }
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