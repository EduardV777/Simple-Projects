#include <iostream>
#include <cstdlib>
using namespace std;

int FindSymbol(char** array, char symbol) {
	int found = 0;
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			if (symbol == array[k][j]) {
				found += 1;
			}
		}
	}
	return found;
}

int main() {
	char** arr = new char* [5];
	char symb;
	cout << "Which symbol do you want to look for? - "; cin >> symb; cout << endl;
	srand(3);
	for (int k = 0; k < 5; k++) {
		arr[k] = new char[5];
		for (int j = 0; j < 5; j++) {
			arr[k][j] = char(1 + rand() % 127);
		}
	}
	//output
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << arr[k][j] << " || ";
		}
		cout << endl;
	}
	cout << "\nThe symbol " << symb << " was found: " << FindSymbol(arr, symb) << " times.\n";
	system("pause>nul");
	return 0;
}