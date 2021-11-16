#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	srand(3);
	int size = 7, size2=size+size;
	int* Arr1 = new int[size], *Arr2 = new int[size], *Arr3 = new int[size2];

	for (int k = 0; k < size; k++) {
		Arr1[k] = 3 + rand() % 16; Arr2[k] = 1 + rand() % 10;
	}
	for (int k = 0; k < size; k++) {
		cout << Arr1[k]<<" | ";
	}
	cout << endl;
	for (int k = 0; k < size; k++) {
		cout << Arr2[k] << " | ";
	}
	cout << endl << endl;
	int k = 0;
	for (; k < size; k++) {
		Arr3[k] = Arr1[k];
	}
	int j = 0;
	for (; k < size2; k++, j++) {
		Arr3[k] = Arr2[j];
	}
	k = 0;
	for (; k < size2; k++) {
		cout << Arr3[k] << " | ";
	}
	cout << endl;
	system("pause>nul");
	return 0;
}