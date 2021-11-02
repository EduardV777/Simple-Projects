#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	int n = 3;
	while (n<=3) {
		cout << "Conversion from Kilometers into Miles: " << endl << endl;
		double dKm = 0;
		while (true) {
			cout << "Please enter the amount of kilometers: "; cin >> dKm;
			if (dKm <= 0) {
				cout << endl << "Error: That's invalid amount of kilometers! Please try again." << endl << endl;
				continue;
			}
			else {
				break;
			}
		}
		cout << "Converting..." << endl;
		const double KminMile = 1.609344;
		double dMile = dKm / KminMile;
		cout << "Kilometers --> Miles: " << dMile << endl << endl;
		n++;
	}
	system("pause");
	return 0;
}