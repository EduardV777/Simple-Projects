#include <iostream>
#include <cstdlib>
using namespace std;

class Savings {
public:
	double startingSum; double p, p2; int y, totalInstallments = 0;
	Savings() {
		startingSum = 5000; p = 0.74; p2 = 1.25; y = 10;
	}
	Savings(double money) {
		startingSum = money; p = 1.35; p2=1.84; y = 5;
	}
	Savings(double money, double percentage, double percentage2) {
		startingSum = money; p = percentage; p2 = percentage2; y = 5;
	}
	Savings(double money, double percentage, double percentage2, int years) {
		startingSum = money; p = percentage; p2=percentage2 ; y = years;
	}

	double CalculateSavings() {
		double s=startingSum;
		//two different installments added to the savings account
		for (int k = 1; k <= y; k++) {
			s *= (1 + p / 100);
			s *= (1 + p2 / 100);
			totalInstallments += 2;
		}
		return s;
	}

	void ShowSavingsInfo() {
		cout << "Starting sum: " << startingSum << "\nAccount savings rate 1: " << p << "%\nAccount savings rate 2: " << p2 << "%\nPeriod: " << y << " years\nFinal sum = "<<CalculateSavings()<<"\nTotal installments for selected period: "<<totalInstallments<<"\n\n";
	}
};

int main() {
	Savings acc1;
	acc1.ShowSavingsInfo();
	Savings acc2(100000, 3, 1.25, 20);
	acc2.ShowSavingsInfo();
	system("pause>nul");
	return 0;
}