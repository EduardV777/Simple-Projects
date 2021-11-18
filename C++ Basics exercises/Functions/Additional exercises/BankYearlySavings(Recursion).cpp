//Fixed Rate, one-time accrual per year
#include <iostream>
#include <cstdlib>
using namespace std;

double getMoney(double m, double r, int y) {
	if (y == 0) {
		return m;
	}
	else {
		return (1 + r / 100) * getMoney(m, r, y-1);
	}
}

int main() {
	double money = 1000; double rate = 5;
	cout << "Initial sum: " << money << "\nYearly rate: " << rate << endl;
	cout << "One year deposit: " << getMoney(money, rate,1) << endl << "Seven years deposit: " << getMoney(money, rate, 7) << endl << "Ten years deposit: " << getMoney(money, rate, 10) << endl;
	system("pause>nul");
	return 0;
}