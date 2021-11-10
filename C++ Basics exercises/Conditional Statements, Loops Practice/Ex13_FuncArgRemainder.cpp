#include <iostream>
#include <cstdlib>
using namespace std;
int ReturnNums(int number) {
	int sum = 0;
	for (int k = 1; k <= 100; k++) {
		if (k%number == 0) {
			sum += k;
		}

	}
	cout << sum;
	return 0;
}
int main() {
	int num;
	cout << "We will use a function and return all the numbers that it's argument can divide by without any remainder(Limit:100)"<<endl<<endl;
	while (true) {
		cout << "Enter a number: "; cin >> num; cout << endl << endl;
		if (num <= 0){
			cout << "Error: Number must be positive and over 0! Try again." << endl;
			continue;
		}
		else {
			break;
		}
	}
	ReturnNums(num);
	system("pause>nul");
	return 0;
}