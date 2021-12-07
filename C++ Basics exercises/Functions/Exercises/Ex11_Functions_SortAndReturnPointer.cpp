#include <iostream>
#include <cstdlib>
using namespace std;

int* ProcessArray(int* array, int size) {
	for (int i = size-1; i > -1; i--) {
		for (int j = 0; j < i; j++) {
			if (array[j] > array[j + 1]) {
				int temp = array[j + 1]; array[j + 1] = array[j]; array[j] = temp;
			}
		}
	}
	int* lastElement=array+(size-1);
	return lastElement;
}

int main() {
	int size = 10;
	int* arr = new int[size];
	srand(2);
	for (int k = 0; k < size; k++) {
		arr[k] = 1 + rand() % 25;
		cout << arr[k] << ", ";
	}
	cout << endl << endl;
	int *lastElement = ProcessArray(arr, size);
	//output after sorting
	for (int k = 0; k < size; k++) {
		cout << arr[k] << ", ";
	}
	cout << endl << "Returned pointer to last element: " << *lastElement;
	system("pause>nul");
	return 0;
}