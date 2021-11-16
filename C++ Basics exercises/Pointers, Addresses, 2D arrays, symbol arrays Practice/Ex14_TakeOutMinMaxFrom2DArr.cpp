#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[5][5], * Arr2 = new int[100];
	srand(2);
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			Arr[k][j] = 1 + rand() % 10;
		}
	}
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << Arr[k][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	//Looking for the max number and putting it into the onedimensional dynamic array
	for (int k = 0; k < 5; k++) {
		int maxNum = 0;
		for (int j = 0; j < 5; j++) {
			if (maxNum < Arr[k][j]) {
				maxNum = Arr[k][j];
			}
		}
		Arr2[k] = maxNum;
	}
	for (int k = 0; k < 100; k++) {
		if (Arr2[k] == -842150451) {
			break;
		}
		cout << Arr2[k] << " | ";
	}
	cout << endl;
	system("pause>nul");
	return 0;
}