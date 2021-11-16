#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Matrix[4][4], sum=0;
	srand(2);
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			Matrix[k][j] = 1 + rand() % 11;
		}
	}
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			cout << Matrix[k][j] << " | ";
		}
		cout << endl;
	}
	cout << endl;
	int diagonalPos = 0;
	for (int k = 0; k < 4; k++) {
		for (int j = 0; j < 4; j++) {
			if (j == diagonalPos) {
				sum += Matrix[k][j];
				break;
			}
			else {
				continue;
			}
		}
		diagonalPos++;
	}
	cout << "Sum of main diagonal elements = " << sum << endl;
	system("pause>nul");
	return 0;
}