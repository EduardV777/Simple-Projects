#include <iostream>
#include <cstdlib>
using namespace std;

int* getMax(int* array, int s) {
	int i = 0;
	for (int k = 0; k < s-1; k++) {
		if (array[i] < array[k + 1]) {
			i = k+1;
		}
	}
	return array + i;
}

void show(int* array,int s) {
	cout << endl;
	for (int k = 0; k < s; k++) {
		cout << array[k] << " | ";
	}
	cout << endl << endl;
}

int main() {
	const int s = 10;
	int Arr[10] = {1, 5, 8, 2, 4, 9, 11, 9, 12, 3};
	cout << "Array contents:";
	show(Arr, s);
	int* maxPnt = getMax(Arr,s);
	*maxPnt = -100;
	cout << "Array contents:";
	show(Arr, s);
	int maxNum = *getMax(Arr, s);
	maxNum = -300;
	cout << "Array contents:";
	show(Arr, s);
	cout << "Value of the highest element in this array: " << *getMax(Arr, s) << endl;
	cout << "Index of the highest element in this array: " << getMax(Arr, s)-Arr;
	system("pause>nul");
	return 0;
}