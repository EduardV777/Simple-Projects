#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Numbers[5][5], sum = 0;
	srand(2);
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			Numbers[k][j] = 1 + rand() % 11;
		}
	}
	//Outputting the values of the Two-Dimensional Array 'Numbers'
	// /*
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 5; j++) {
			cout << Numbers[k][j] << " | ";
			sum += Numbers[k][j] * Numbers[k][j];
		}
		cout << endl;
	}
	// */
	cout << endl << "Sum: " << sum;
	system("pause>nul");
	return 0;
}