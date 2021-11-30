#include <iostream>
#include <cstdlib>
using namespace std;

//Without recursion
int CalculateDoubleFactorial(int n) {
	int s = 1;
	for (int k = 1; k <= n; k+=2) {
		s *= k;
	}
	return s;
}

//With recursion
int CalculateDoubleFactorial2(int n, int k = 1, int sum = 1) {
	if (k > n) {
		return sum;
	}
	else {
		sum *= k;
		k += 2;
		return CalculateDoubleFactorial(n);
	}
}

int main() {
	int n;
	cout << "Enter the number for which you want to calculate it's double factorial: "; cin >> n;
	cout << "\nFactorial of N = " << CalculateDoubleFactorial(n) << endl;
	system("pause>nul");
	return 0;
}