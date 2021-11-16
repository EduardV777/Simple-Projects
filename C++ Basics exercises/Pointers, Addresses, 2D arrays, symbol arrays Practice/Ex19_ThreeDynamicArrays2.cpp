#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	srand(5);
	int size = 6; int size2 = size * 2;
	int* Arr1 = new int[size], * Arr2 = new int[size], * Arr3 = new int[size2];
	for (int k = 0; k < size; k++) {
		Arr1[k] = 1 + rand() % 12; Arr2[k] = 3 + rand() % 16;
	}
	for (int k = 0; k < size; k++) {
		cout << Arr1[k] << " | ";
	}
	cout << endl;
	for (int k = 0; k < size; k++) {
		cout << Arr2[k] << " | ";
	}
	cout << endl << endl;
	int i = 0, j=0;
	for (int k = 0; k < size; k++) {
		Arr3[i] = Arr1[k];
		i += 1;
		for (; j < size;) {
			Arr3[i] = Arr2[j];
			i++; j++;
			break;
		}
		if (i >= size2) {
			break;
		}
	}

	for (int k = 0; k < size2; k++) {
		cout << Arr3[k] << " | ";
	}
	cout << endl;
	system("pause>nul");
	return 0;
}