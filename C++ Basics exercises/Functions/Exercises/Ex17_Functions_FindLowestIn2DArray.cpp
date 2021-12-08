#include <iostream>
#include <cstdlib>
using namespace std;

int* FindLowest(int** array) {
	int lowestNum = 25;
	int* LowestRef=array[0];
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			if (lowestNum > array[k][j]) {
				lowestNum = array[k][j];
				LowestRef = array[k] + j;
			}
		}
	}
	return LowestRef;
}

int main() {
	int **arr=new int* [5];
	srand(3);
	for (int k = 0; k < 5; k++) {
		arr[k] = new int[5];
		for (int j = 0; j < 5; j++) {
			arr[k][j] = 1 + rand() % 25;
		}
	}
	//check
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << arr[k][j] << ", ";
		}
		cout << endl;
	}
	cout << "\nLowest number found: " << *FindLowest(arr);
	system("pause>nul");
	return 0;
}