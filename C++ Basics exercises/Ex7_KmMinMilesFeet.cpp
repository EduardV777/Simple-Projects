#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "Conversion of Kilometers/Meters into Miles/Feet: " << endl << endl;
	double dKm=0, dM=0, dMi=0, dF=0;
	while (true) {
		cout << "Please enter amount of kilometers - "; cin >> dKm;
		if (dKm <= 0) {
			cout << endl << "Error: Invalid amount of kilometers! Try again." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	while (true) {
		cout << "Please enter amount of meters - "; cin >> dM;
		if (dM <= 0) {
			cout << endl << "Error: Invalid amount of meters! Try again." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	cout << endl << "Converting..." << endl;
	double dUser = dKm + (dM/1000);
	const double KminMile = 1.609344; const int FeetinMi = 5280;
	cout << "Miles: " << dUser / KminMile << endl << "Feet: " << (double)(dUser / KminMile) * FeetinMi<<endl<<endl;
	system("pause");
	return 0;
}