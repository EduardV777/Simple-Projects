#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[5][5], num=1;
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++,num++) {
			Arr[k][j] = num;
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