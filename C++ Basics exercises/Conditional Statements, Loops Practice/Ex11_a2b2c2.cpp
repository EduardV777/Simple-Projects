#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;
int main() {
	cout << "Looking for all solutions for 'a2+b2=c2' in the range of 1-100 for all variables." << endl << endl;
	//a2+b2=c2
	int a, b, c;
	for (int k = 1; k <= 100; k++) {
		a = k;
		for (int j = 1; j <= 100; j++) {
			b = j;
			for (int i = 1; i <= 100; i++) {
				c = i;
					if (a*a + b*b == c*c) {
						//cout << i << endl;
						cout << a << "(2) +" << b << "(2) = " << c << "(2)"<<endl;
						break;
				    }
			}
		}
	}
	cout << endl << endl << "Action finished!" << endl;
	system("pause>nul");
	return 0;
}