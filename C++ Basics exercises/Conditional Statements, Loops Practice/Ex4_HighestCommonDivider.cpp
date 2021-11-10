#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int a, b, k, j, A[250], B[250], size1=0, size2=0, hcf=0, tmp=0;
	cout << "I will find the highest common factor of two numbers of your choice: \n\n";
	cout << "Number A: "; cin >> a; cout << "\nNumber B: "; cin >> b; cout << endl << endl;
	//array A -- number A
	for (k = 1, j=0;k<=a;) {
		if (a % k == 0) {
			A[j] = k;
			cout << A[j] << " || ";
			k++, j++, size1+=1;
		}
		else {
			k++;
		}
	}
	cout << endl;
	//array B -- number B
	for (k = 1, j = 0; k <= b;) {
		if (b % k == 0) {
			B[j] = k;
			cout << B[j] << " || ";
			k++, j++, size2+=1;
		}
		else {
			k++;
		}
	}
	cout << endl;
	for (k = 0; k < size1; k++) {
		tmp = A[k];
		for (j = 0; j < size2; j++) {
			if (tmp == B[j]) {
				hcf = tmp;
			}
		}
	}
	cout << endl << "Highest common factor = " << hcf << endl;
	system("pause");
	return 0;
}