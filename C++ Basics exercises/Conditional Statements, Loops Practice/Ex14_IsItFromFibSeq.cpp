#include <iostream>
#include <cstdlib>
using namespace std;
/* Variant 1
int main() {
	int num;
	while (true) {
		cout << "{Limit:10}" << endl << "Enter a number: "; cin >> num; cout << endl << endl;
		if (num <= 0) {
			cout << "Number must be positive and over 0! Try again." << endl << endl;
			continue;
		}
		else if (num > 10) {
			cout << "Too high! Number must be below 10. Try again." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	switch (num) {
	case 2:
	case 3:
	case 5:
	case 8:
		cout << "Yes! This number is part of the fibonacci sequence!" << endl << endl;
		break;
	default:
		cout << "Oh no! This number is not part of the fibonacci sequence." << endl << endl;
	}
	system("pause>nul");
	return 0;
}
*/
/* Variant 2
int main() {
	int num, n=0, k, fibo[10];
	fibo[0] = 1; fibo[1] = 1;
	bool found = false;
	while (true) {
		cout << "{Limit:55}" << endl << "Enter a number: "; cin >> num; cout << endl << endl;
		if (num <= 0) {
			cout << "Number must be positive and over 0! Try again." << endl << endl;
			continue;
		}else if (num>55){
			cout << "Too high! Number must be below 56. Try again." << endl << endl;
			continue;
		}else {
			break;
		}
	}
	//Counting 'n' elements in 'fibo' with 'for in'
	for (int &x : fibo) {
		n += 1;
	}
	//cout << n;
	//Creating fibo sequence in array
	for (k = 2; k < n; k++) {
		fibo[k] = fibo[k - 1] + fibo[k - 2];
		//cout << fibo[k] << " || ";
	}
	for (int& x : fibo) {
		if (num == x) {
			found = true;
			cout << "Yes! This number is part of the fibonacci sequence." << endl << endl;
			break;
		}
	}
	if (found == false) {
		cout << "Oh no! This number is not part of the fibonacci sequence." << endl << endl;
	}
	system("pause>nul");
	return 0;
}
*/