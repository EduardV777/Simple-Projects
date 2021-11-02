#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	cout << "Conversion of M/s into Km/h: " << endl << endl;
	double ms = 0, kmh = 0;
	while (true) {
		cout << "Enter amount for m/s: "; cin >> ms;
		if (ms <= 0) {
			cout << endl << "Error: Conversion is impossible with amount of 'm/s' below 1." << endl << endl;
			continue;
		}
		else {
			break;
		}
	}
	cout << endl << "Conveting..." << endl;
	const int MetersinKm = 1000, SecondsinHour=3600;
	cout << "Km/h: " << (ms / MetersinKm) * SecondsinHour<<endl<<endl;
	system("pause");
	return 0;
}