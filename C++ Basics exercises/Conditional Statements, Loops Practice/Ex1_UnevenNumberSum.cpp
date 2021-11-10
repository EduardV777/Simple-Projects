#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int n, k, s=0, orig_count;
	cout << "Calculating the sum total of 'n' uneven numbers using for(): \n\n";
	cout << "Please set 'n'(Amount of uneven numbers): "; cin >> n; cout << endl << endl;
	orig_count = n;
	for (k = 1; k <= n;) {
		if (k % 2 != 0) {
			cout << k << " || ";
			s += k;
			k++;
		} else {
			k++, n++;
			continue;
		}
	}
	cout << endl << "Sum of " << orig_count << " uneven numbers = " << s << endl << endl;
	system("pause");
	return 0;
}