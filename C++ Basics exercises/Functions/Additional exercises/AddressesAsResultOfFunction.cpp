#include <iostream>
#include <cstdlib>
using namespace std;

int &getMax(int* array,int size) {
	int i = 0;
	for (int k = 0; k < size - 1; k++) {
		if (array[i]<array[k+1]) {
			i = k + 1;
		}
	}
	return array[i];
}


void show(int* array,int size) {
	for (int k = 0; k < size; k++) {
		cout << array[k] << " | ";
	}
	cout << endl;
}

int main() {
	const int s = 10;
	int Arr[10] = { 1, 5, 8, 2, 4, 9, 11, 9, 12, 3 };
	cout << "Array contents:\n";
	show(Arr, s);
	int maxNum = getMax(Arr, s);
	maxNum = -100;
	cout << "Array contents:\n";
	show(Arr, s);
	int& maxRef = getMax(Arr,s);
	maxRef = -300;
	cout << "Array contents:\n";
	show(Arr, s);
	cout << "\nValue of the highest element of the array: " << getMax(Arr, s) << endl;
	system("pause>nul");
	return 0;
}