#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Numbers[10], sum=0;
	srand(2);
	for (int k = 0; k < 10; k++) {
		Numbers[k] = 1 + rand() % 20;
	}
	/*
	for (int& x : Numbers) {
		cout << x << " | ";
	}
	*/
	for (int k = 0; k < 10; k++) {
		sum += Numbers[k] * Numbers[k];
	}
	cout << "Sum of elements to the power of 2: " << sum << endl;
	system("pause>nul");
	return 0;
}