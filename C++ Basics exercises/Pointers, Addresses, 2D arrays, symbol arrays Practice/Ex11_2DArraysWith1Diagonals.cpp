#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[5][5];
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			Arr[k][j] = 10;
		}
	}
	//setting elements of the first diagonal to 1
	int j = 0;
	for (int k = 0; k < 5; k++) {
		for (; j < 5;) {
			Arr[k][j] = 1;
			j++;
			break;
		}
	}
	//setting elements of the second diagonal to 1
	j = 4;
	for (int k = 0; k < 5; k++) {
		for (; j > -1;) {
			Arr[k][j] = 1;
			j--;
			break;
		}
	}
	//setting all other elements to zero
	for (int k = 0; k < 5; k++) {
		for (j = 0; j < 5; j++) {
			if (Arr[k][j] != 1) {
				Arr[k][j] = 0;
			}
			else {
				continue;
			}
		}
	}

	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << Arr[k][j] << " | ";
		}
		cout << endl;
	}
	system("pause>nul");
	return 0;
}