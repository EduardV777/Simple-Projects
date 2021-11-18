#include <iostream>
#include <cstdlib>
using namespace std;

double getMoney(double m, double r) {
	return m*(1 + r / 100);
}
double getMoney(double m,double r, int y){
	double s = m;
	for (int k = 1; k <= y; k++) {
		s *= (1 + r / 100);
	}
	return s;
}
double getMoney(double m, double r, int y, int n) {
	return getMoney(m, r / n, n * y);
}

int main() {
	double money = 1000;
	double rate = 5;
	int years = 7;
	int n = 3;
	cout << "Initial sum: " << money << endl << "Yearly rate: " << rate << "%" << endl;
	cout << endl << "Yearly deposit: " << getMoney(money, rate) << endl << "Five year deposit: " << getMoney(money, rate, years) << endl << "Five years deposit with 'n' periods of time adding rate: " << getMoney(money, rate, years, n) << endl;
	system("pause>nul");
	return 0;
}