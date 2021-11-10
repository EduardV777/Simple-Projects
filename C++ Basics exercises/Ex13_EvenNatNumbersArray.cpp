#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int k = 0, j = 0, choice=0; const int size = 100; int Array[size];
	while (k < size) {
		Array[k] = j;
		j += 2; k++;
	}
	k = 0;
	while (true) { cout << "Do you want to output an array with 2000 even numbers?" << endl << "[1]-Yes" << endl << "[2]-No" << endl; cin >> choice; if (choice == 0 || choice < 1 || choice>2) { cout << endl << "Error: Choice is incorrect!" << endl << endl; continue; } else { break; } }
	if (choice == 1) {
		cout << endl << "Array Even Numbers: " << endl;
		while (k < size) {
			cout << Array[k] << " || ";
			k++;
		}
		cout << endl;
	} else if (choice == 2) {
		cout << endl << "Leaving program..." << endl;
		system("pause"); return 0;
	}
	system("pause");
	return 0;
}