#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int num, n, k=1;
	cout << "I can show you numbers which when your chosen number is divided by them, there is no remainder:\n\n";
	cout << "Please tell me your chosen number: "; cin >> num; cout << "\n\nPlease tell me how much numbers do you want to be generated: "; cin >> n; cout << "\n\n";
	for (; k <= n;) {
		if (k > num) {
			cout << "\nNotice: Max number reached!\n\n";
			break;
		}else if (num % k == 0) {
			cout << k << " || ";
			k++;
		}
		else {
			k++, n++;
			continue;
		}
	}

}