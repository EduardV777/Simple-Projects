#include <iostream>
#include <cstdio>
using namespace std;
int main() {
	int n = 100, k=1;
	double q = 1, x = 1, s=1;
	cout << "This program will calculate the expression x^n/(n+1)!" << endl << endl;
	for (; k <= n; k++) {
		s += q;
		q *= x / (k+1);
	}
	cout << endl << "Result = " << s << endl << endl;
	system("pause>nul");
	return 0;
}