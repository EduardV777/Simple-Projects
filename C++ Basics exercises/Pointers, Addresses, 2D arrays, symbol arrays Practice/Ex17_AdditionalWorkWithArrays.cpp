#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	srand(2);
	int size = 10;
	int *Arr1=new int [size], *Arr2=new int [size], *Arr3=new int [size];
	//putting random values in first two
	for (int k = 0; k < size; k++) {
		Arr1[k] = 2 + rand() % 16;
		Arr2[k] = 1 + rand() % 8;
	}
	//filling third arr by comparing two values between first two arrays in every index and picking out the max one
	for (int k = 0; k < size; k++) {
		int maxVal=0;
		if (Arr1[k] > Arr2[k]) {
			maxVal = Arr1[k];
		}
		else {
			maxVal = Arr2[k];
		}
		Arr3[k] = maxVal;
	}
	//outputting arrays 1/2
	for (int k = 0; k < size; k++) {
		cout << Arr1[k] << " | ";
	}
	cout << endl;
	for (int k = 0; k < size; k++) {
		cout << Arr2[k] << " | ";
	}
	cout << endl << endl;
	//outputting array 3
	for (int k = 0; k < size; k++) {
		cout << Arr3[k] << " | ";
	}
	system("pause>nul");
	return 0;
}