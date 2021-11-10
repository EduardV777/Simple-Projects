#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int n, k=1, s=0;
	cout << "Calculate the sum total of 'n' even numbers with do-while: \n\n";
	cout << "'n' Amount of even numbers: "; cin >> n; cout << endl << endl;
	do {
		if (k % 2 != 0) {
			s += k;
			k++;
		}
		else {
			k++;
			continue;
		}
	} while (k <= n - 1);
		cout << endl << "Sum = " << s << endl << endl;
		system("pause");
		return 0;
}