#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int Sum(int n, int power, int i=1, int sum=0) {
	if (i > n) {
		return sum;
	}
	else {
		sum += pow(i, power);
		i++;
		return Sum(n, power, i, sum);
	}
	
}
int main() {
	int n, k;
	cout << "How much number would you like to calculate? - "; cin >> n; cout << "\nEnter k(Power of numbers): "; cin >> k;
	cout << "Result = " << Sum(n, k) << endl;
	system("pause>nul");
	return 0;
}