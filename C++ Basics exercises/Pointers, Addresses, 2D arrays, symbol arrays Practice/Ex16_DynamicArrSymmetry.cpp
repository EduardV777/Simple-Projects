#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	srand(5);
	int size = 1 + rand() % 20;
	int* dynArr = new int[size];
	for (int k = 0; k < size; k++) {
		dynArr[k] = 0;
	}
	for (int k = 0,i = size - 1; k <= i; k++,i--) {
		dynArr[k] = k; dynArr[i] = k;
	}
	for (int k = 0; k < size; k++) {
		cout << dynArr[k] << " ";
	}
	system("pause>nul");
	return 0;
}