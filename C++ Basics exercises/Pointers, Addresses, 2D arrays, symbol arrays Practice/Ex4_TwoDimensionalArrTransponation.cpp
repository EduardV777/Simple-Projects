#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Matrix[10][10];
	srand(2);
	for (int k = 0; k < 10; k++) {
		for (int j = 0; j < 10; j++) {
			Matrix[k][j] = 1 + rand() % 10;
		}
	}
	//outputting the values of array 'Matrix'
	for (int k = 0; k < 10; k++) {
		for (int j = 0; j < 10; j++) {
			cout << Matrix[k][j] << " || ";
		}
		cout << endl;
	}
	cout << endl;
	int temp = 0, diagonalPos=0, j=0;
	//exchanging values
	for (int k = 0; k < 10; k++) {
		for (j=diagonalPos; j < 10; j++) {
			if (j != diagonalPos) {
				temp = Matrix[k][j];
				Matrix[k][j] = Matrix[j][k];
				Matrix[j][k] = temp;
			}
			else {
				continue;
			}
		}
		diagonalPos++;

	}

	for (int k = 0; k < 10; k++) {
		for (j = 0; j < 10; j++) {
			cout << Matrix[k][j] << " || ";
		}
		cout << endl;
	}
	system("pause>nul");
	return 0;
}