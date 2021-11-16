//TO BE FINISHED
#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[5][5], num = 1, steps=1, length=1;
	for (int k = 0; k < steps; k++) {
		if (steps > 5) {
			break;
		}
		for (int j = 0; j < steps; j++, num++) {
			Arr[k][j] = num;
		}
	}
	
	for (int k = 0; k < 5; k++,length++) {
		if (length > 5) {
			break;
		}
		for (int j = 0; j < length; j++) {
			cout << Arr[k][j];
		}
	}
	system("pause>nul");
	return 0;
}