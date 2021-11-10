#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Numbers[10], length=0;
	//srand(31564);
	srand(2);
	cout << "{Array loading...}" << endl << endl;
	for (int k = 0; k < 10; k++) {
		Numbers[k] = 1 + rand() % 10;
	}
	cout << "[Before sorting]Elements generated: "<<endl;
	for (int& x : Numbers) {
		cout << x << " | ";
		length += 1;
	}
	cout << endl << endl << "{Sorting array in descending order...}"<<endl<<endl;
	for (int i = length-1; i > 0; i--) {
		for (int j = length-1; j > 9 - i; j--) {
			if (Numbers[j] > Numbers[j - 1]) {
				int temp = Numbers[j - 1];
				Numbers[j - 1] = Numbers[j];
				Numbers[j] = temp;
			}
		}
	}
	cout << "[After sorting]Elements after sorting:" << endl;
	for (int& x : Numbers) {
		cout << x << " | ";
	}
	cout << endl << endl << "Action finished!";
	system("pause>nul");
	return 0;
}