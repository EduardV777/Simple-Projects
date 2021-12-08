#include <iostream>
#include <cstdlib>
using namespace std;

int FindAverage(int** arr,int elements) {
	int sum = 0;
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			sum += arr[k][j];
		}
	}
	return sum / elements;
}

int main() {
	int elements = 0;
	int** arr = new int* [5];
	srand(3);
	for (int k = 0; k < 5; k++) {
		arr[k] = new int[5];
		for (int j = 0; j < 5; j++) {
			arr[k][j] = 1 + rand() % 25;
			elements += 1;
		}
	}
	//output
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << arr[k][j] << ", ";
		}
		cout << endl;
	}
	cout << "\nAverage of all elements in this array: " << FindAverage(arr,elements) << endl;
	system("pause>nul");
	return 0;
}