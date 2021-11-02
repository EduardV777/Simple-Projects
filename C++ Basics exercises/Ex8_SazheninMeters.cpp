#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	double sazh = 0;
	cout << "Conversion of sazhens into meters: "<<endl<<endl;
	while (true) {
		cout << "Please enter amount of 'sazhens' to be converted - "; cin >> sazh;
		if (sazh <= 0) {
			cout << endl << "Error: Amount in 'sazhens' is invalid! Try again with different value." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	cout << endl << "Converting..." << endl;
	const double MetersinSazhen = 2.1336;
	cout << "Meters: " << sazh * MetersinSazhen<<endl<<endl;
	system("pause");
	return 0;
}