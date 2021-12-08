#include <iostream>
#include <cstdlib>
using namespace std;

int* FindGreatest(int** tdArray) {
	int maxNum = 0, ind1 = 0, ind2 = 0;
	int* GreatestRef=tdArray[0];
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			if (maxNum < tdArray[k][j]) {
				maxNum = tdArray[k][j];
				GreatestRef = tdArray[k] + j;
			}
		}
	}
	return GreatestRef;
}

int main() {
	int** arr = new int* [5];
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
	cout << "\nBiggest number found: " << *FindGreatest(arr) << endl;
	system("pause>nul");
	return 0;
}