#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[5][5], Arr2[5][5];
	srand(2);
	//Arr1
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			Arr[k][j] = 1 + rand() % 17;
		}
	}
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << Arr[k][j] << " | ";
		}
		cout << endl;
	}
	//Arr2
	int k = 0; int j = 0;
	while (true) {
		int row, col;
		cout << "Choose which row do you want to pull into 'Arr2'(Max 4): "; cin >> row;
		cout << endl << "Choose which column do you want to pull into 'Arr2'(Max 4): "; cin >> col;
		cout << endl;
		for (int i=0; i < 5;i++) {
			Arr2[k][i] = Arr[row][i];
		}
		k++;
		for (int i=0; i < 5; i++) {
			Arr2[i][j] = Arr[i][col];
		}
		j++;
		if (k == 5 and j == 5) {
			break;
		}
	}
	cout << endl << "Result: \n";
	for (k = 0; k < 5; k++) {
		for (j = 0; j < 5; j++) {
			cout << Arr2[k][j]<<" | ";
		}
		cout << endl;
	}
	system("pause>nul");
	return 0;
}