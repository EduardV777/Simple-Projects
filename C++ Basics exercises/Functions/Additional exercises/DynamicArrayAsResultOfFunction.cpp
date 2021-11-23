//Not recommended working that way
#include <iostream>
#include <cstdlib>
using namespace std;

int* fibs(int size) {
	int* nums = new int[size];
	for (int k = 0; k < size; k++) {
		if (k == 0 || k == 1) {
			nums[k] = 1;
		}
		else {
			nums[k] = nums[k - 1] + nums[k - 2];
		}
	}
	return nums;
}

int* myRands(int size) {
	int* randNums = new int[size];
	for (int k = 0; k < size; k++) {
		randNums[k] = 1 + rand() % 11;
	}
	return randNums;
}

int main() {
	srand(2);
	int s = 10;
	int* f = fibs(s);
	cout << "Fibs dynamic array:\n";
	for (int k = 0; k < s; k++) {
		cout << f[k] << " | ";
	}
	cout << endl;
	delete[] f;
	f = myRands(s);
	cout << "\nRandom numbers dynamic array:\n";
	for (int k = 0; k < s; k++) {
		cout << f[k] << " | ";
	}
	cout << endl;
	delete[] f;
	system("pause>nul");
	return 0;
}