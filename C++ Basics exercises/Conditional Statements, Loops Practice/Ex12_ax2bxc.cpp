#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
using namespace std;
int main() {
	int a, b, c;
	double x1, x2;
	cout << "Solving the quadratic equation Ax2+bx+c=0" << endl << endl;
	srand(2); double chance = 0;
	for (int k = 0; k <= 2; k++) {
		double num = rand(); int numInt = num;
		chance = numInt - num;
		if (0.30 < chance < 0.50) {
			a = (int)(1 + rand() % 45), b = (int)1 + rand() % 23, c = (int)1 + rand() % 48 / 2;
		}else if (0.50<chance < 0.70) {
			a = (int)(1 + rand() % 12), b = (int)1 + rand() % 56, c = (int)1 + rand() % 24 / 2;
		}
		else if (chance > 0.70) {
			a = (int)(1 + rand() % 15), b = (int)1 + rand() % 35, c = (int)1 + rand() % 74 / 2;
		}
	}
	double D = (pow(b, 2) - 4 * a * c);
	cout << "Step 1: " << a << "x2 + " << b << "x + " << c << " = 0" << endl << endl;
	cout << "Step 2: x = -b +- _/b2-4*a*c\n            _______________\n                   2a"<<endl<<endl;
	if (D >= 0){
		b = (b * -1);
		cout << "            " << b << " +- " << D<<endl<< "        ________________"<<endl<<"                 "<<2*a<<endl<<endl;
		x1 = (b + D)/(2 * a); x2=(b - D) / (2 * a);
		cout << "Two real roots found to this equation!" <<std::fixed<< endl <<"x1 = "<<std::setprecision(2)<<x1<<endl<<"x2 = "<<x2<<endl<<endl;
	}
	else {
		cout << "No solution(Discriminant is negative!)"<<endl<<endl;
	}
	cout << "Action Finished!" << endl;
	system("pause>nul");
	return 0;
}