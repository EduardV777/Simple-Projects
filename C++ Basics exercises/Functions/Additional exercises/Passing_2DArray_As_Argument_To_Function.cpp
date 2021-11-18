#include <iostream>
#include <cstdlib>
using namespace std;

const int n = 3;

void output(int A[][n], int p) {
	for (int i = 0; i < p; i++) {
		for (int j = 0; j < n; j++) {
			cout << A[i][j] << " | ";
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	int Arr1[2][n] = { {2,3,1} ,{5,3,2} };
	int Arr2[][n] = { {5,6,3} ,{2,5,7} ,{9,3,1} ,{4,8,3} ,{6,7,1} };
	output(Arr1, 2); output(Arr2, 5);
	system("pause>nul");
	return 0;
}