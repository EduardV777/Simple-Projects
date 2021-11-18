#include <iostream>
#include <cstdlib>
using namespace std;

double getMoney(double m, double r, int y=1, int n=1) {
	double s = m;
	double q = r / n;
	double z = n * y;
	for (int k = 1; k <= z; k++) {
		s *= (1+q / 100);
	}
	return s;
}

int main() {
	double money = 1000;
	double rate = 5;
	cout << "Initial sum: " << money << endl << "Yearly rate: " << rate << endl << endl;
	cout << "One year deposit: " << getMoney(money, rate) << endl;
	cout << "Seven years deposit: " << getMoney(money, rate, 7) << endl;
	cout << "Seven years deposit with three accruals per year: " << getMoney(money, rate, 7, 3) << endl;
	system("pause>nul");
	return 0;
}