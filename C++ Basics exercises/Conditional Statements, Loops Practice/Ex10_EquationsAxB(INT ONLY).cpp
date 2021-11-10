#include <iostream>
#include <cstdio>
using namespace std;
int main() {
	double A, B, res; int allowedIntegers[1000];
	bool isItInt = false;
	cout << "Solving Ax=B type of equations:(Integers only)" << endl << endl;
	for (int k = 0; k < 1000; k++) {
		allowedIntegers[k] = k;
		//cout<<allowedIntegers[k];
	}
	try {
		while (true) {
			cout << "Enter value for A: "; cin >> A; cout << endl;
			for (int k = 0; k < 1000; k++) {
				if (A == allowedIntegers[k]) {
					isItInt = true;
					break;
				}
			}
			if (isItInt == true) {
				break;
			}
			else {
				cout << endl << endl << "Error: Only integers are allowed!" << endl << endl;
				continue;
			}
		}
		//revert status
		isItInt == false;
		while (true) {
			cout << "Enter value for B: "; cin >> B; cout << endl;
			for (int k = 0; k < 1000; k++) {
				if (B == allowedIntegers[k]) {
					isItInt = true;
					break;
				}
			}
			if (isItInt == true) {
				break;
			}
			else {
				cout << endl << endl << "Error: Only integers are allowed!" << endl << endl;
				continue;
			}
		}
		//revert status again
		isItInt = false;
		if (A != 0) {
			res = B / A;
			//cout << res;
			while (true) {
				for (int k = 0; k < 1000; k++) {
					if (res == allowedIntegers[k]) {
						isItInt = true;
						break;
					}
				}
				if (isItInt == true) {
					throw res;
					break;
				}
				else {
					string msg = "No solution to the equation!(Result not integer!)";
					throw msg;
					break;
				}
			}
		}
		else if (B != 0) {
			string msg = "No solution to the equation!";
			throw msg;
		}
		else {
			cout << endl << "Every number is solution to this equation!";
		}
	}
		catch (double a) {
			cout << "x = " << a << endl;
	}
		catch (string a) {
			cout << endl << a;
	}
		cout << endl << endl << "Action complete!" << endl;
		system("pause>nul");
		return 0;
}