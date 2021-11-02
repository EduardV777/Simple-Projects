#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	double kmh = 0, ms=0;
	cout << "Conversion of km/h into m/s: " << endl << endl;
	while (true) {
		cout << "Enter the amount for km/h: "; cin >> kmh;
		if (kmh <= 0) {
			cout << endl << "Error: Conversion with 0 or below amount of km/h is impossible." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	cout << endl << "Converting..." << endl;
	const int MetersinKm = 1000, SecondsinHour = 60 * 60;
	ms = (kmh*MetersinKm) / SecondsinHour;
	cout << "M/s: " << ms << endl << endl;
	system("pause");
	return 0;
}