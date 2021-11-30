#include <iostream>
#include <cstdlib>
using namespace std;
//No recursion
int CalculateFactorial(int number) {
	int s = 1;
	for (int k = 1; k <= number; k++) {
		s *= k;
	}
	return s;
}

//With recursion
int CalculateFactorial2(int number, int k = 1, int sum=1) {
	if (k > number) {
		return sum;
	}
	else {
		sum *= k;
		k++;
		return CalculateFactorial2(number, k, sum);
	}
}

int main() {
	int n;
	cout << "Enter the number for which you want to calculate it's factorial: "; cin >> n;
	cout << endl << "Factorial of n = " << CalculateFactorial2(n) << endl;
	system("pause>nul");
	return 0;
}