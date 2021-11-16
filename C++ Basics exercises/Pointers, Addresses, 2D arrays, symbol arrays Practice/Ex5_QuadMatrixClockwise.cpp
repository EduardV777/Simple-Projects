#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Matrix[4][4];
	srand(3);
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			Matrix[k][j] = 1 + rand() % 10;
		}
	}
	//outputting arr values
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			cout << Matrix[k][j] << " || ";
		}
		cout << endl;
	}
	cout << endl;
	for (int k = 0, column=0; k < 4; k++, column++) {
		for (int j = 0, row = j; j < 4; j++, row++) {
			Matrix[k][j] = Matrix[row][column];
		}
	}
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			cout << Matrix[k][j] << " || ";
		}
		cout << endl;
	}
	system("pause>nul");
	return 0;
}