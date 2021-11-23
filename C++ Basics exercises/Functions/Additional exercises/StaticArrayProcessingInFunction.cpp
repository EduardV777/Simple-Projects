#include <iostream>
#include <cstdlib>
using namespace std;

void fibs(int* array, int size) {
	for (int k = 0; k < size; k++) {
		if (k == 0 || k == 1) {
			array[k] = 1;
		}
		else {
			array[k] = array[k - 1] + array[k - 2];
		}
	}
}

void myRands(int* array, int size) {
	for(int k = 0; k < size; k++) {
		array[k] = 1 + rand() % 17;
	}
}

int main() {
	srand(2);
	const int s = 15;
	int f[15];
	fibs(f, s);
	cout << "Fibs array:\n";
	for(int k = 0; k < s; k++) {
		cout << f[k] << " | ";
	}
	cout << endl << "Random numbers array:\n";
	myRands(f, s);
	for (int k = 0; k < s; k++) {
		cout << f[k] << " | ";
	}
	cout << endl;
	system("pause>nul");
	return 0;
}