#include <iostream>
#include <cstdlib>
using namespace std;

int* Multiply(int* Array, int size, bool performAction2 = false, int num = 0) {
	if (performAction2 == true) {
		for (int k = 0; k < size; k++) {
			Array[k] *= num;
		}
	}
	else {
		for (int k = 0; k < size; k++) {
			Array[k] *= 10;
		}
	}
	return 0;
}


int* ProcessArray(int* Array, int* function){
	function;
	return Array;
}
int* ProcessArray(int* Array, int num) {
	Multiply(Array, 10, true, num);
	return Array;
}

int main() {
	int* arr = new int[10];
	srand(2);
	for (int k = 0; k < 10; k++) {
		arr[k] = 1 + rand() % 20;
	}
	cout << "Current Array Elements:\n";
	for (int k = 0; k < 10; k++) {
		cout << arr[k] << " || ";
	}
	cout << "\nProcessing array...\n";
	int* processedArray = ProcessArray(arr, Multiply(arr,10));
	cout << "\nArray after processing:\n";
	for (int k = 0; k < 10; k++) {
		cout << processedArray[k] << " || ";
	}
	system("pause>nul");
	return 0;
}