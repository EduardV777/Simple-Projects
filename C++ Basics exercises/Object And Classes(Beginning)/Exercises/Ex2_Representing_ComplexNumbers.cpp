#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class ComplexNumbers {
public:
	int realPart;
	int imaginaryPart;
	string op;
	ComplexNumbers(int realNum, int imaginaryNum) {
		realPart = realNum;
		imaginaryPart = imaginaryNum;
		cout << "\nComplex number has been created\n";
	}

	//defining operators for performing mathematical operations between objects of this class
	void operator+(ComplexNumbers x) {
		int newRealPart; int newImaginaryPart;
		newRealPart = this->realPart + x.realPart;
		newImaginaryPart = this->imaginaryPart + x.imaginaryPart;
		this->realPart = newRealPart; this->imaginaryPart = newImaginaryPart;
		cout << "\nObject's " << this << " complex number has been changed.(Adding operation performed)\n";
	}
	void operator-(ComplexNumbers x) {
		int newRealPart; int newImaginaryPart;
		newRealPart = this->realPart - x.realPart;
		newImaginaryPart = this->imaginaryPart - x.imaginaryPart;
		this->realPart = newRealPart; this->imaginaryPart = newImaginaryPart;
		cout << "\nObject's " << this << " complex number has been changed.(Substraction operation performed)\n";
	}
	void operator*(ComplexNumbers x) {
		int newRealPart; int newImaginaryPart;
		newRealPart = this->realPart * x.realPart + this->realPart * x.imaginaryPart;
		newImaginaryPart = this->imaginaryPart * x.realPart + this->imaginaryPart * x.imaginaryPart;
	}
	void operator/(ComplexNumbers x) {
		int newRealPart; int newImaginaryPart; int denom; string stringRepresentation;
		int newRealPart1Num1; int newRealPart2Num1; int newImaginaryPart1Num1; int newImaginaryPart2Num1;
		int newRealPart1Num2; int newRealPart2Num2; int newImaginaryPart1Num2; int newImaginaryPart2Num2;
		newRealPart1Num1 = this->realPart * x.realPart; newRealPart2Num1=this->realPart*(x.imaginaryPart*-1); newImaginaryPart1Num1 = this->imaginaryPart * x.realPart; newImaginaryPart2Num1 = this->imaginaryPart * (x.imaginaryPart * -1);
		newRealPart1Num2 = x.realPart * x.realPart; newRealPart2Num2 = x.realPart * (x.imaginaryPart * -1); newImaginaryPart1Num2 = x.imaginaryPart * x.realPart; newImaginaryPart2Num2 = x.imaginaryPart* (x.imaginaryPart * -1);

		newImaginaryPart2Num1 = newImaginaryPart2Num1 * -1; newImaginaryPart2Num2=newImaginaryPart2Num2 * -1;
		newRealPart = newRealPart1Num1 + newImaginaryPart2Num1; newImaginaryPart = newImaginaryPart1Num1 + newRealPart2Num1;
		denom = newRealPart1Num2 + newRealPart2Num2 + newImaginaryPart1Num2 + newImaginaryPart2Num2;
		cout << "\nObject's " << this << " complex number has been changed.(Division operation performed)\n";
		if (newImaginaryPart > 0) {
			cout << newRealPart << "/" << denom << " + " << newImaginaryPart << "i/" << denom << "\n\n";
		}
		else {
			cout << newRealPart << "/" << denom << " - " << newImaginaryPart << "i/" << denom << "\n\n";
		}
		this->realPart = newRealPart / denom; this->imaginaryPart = newImaginaryPart / denom;
	}

	void showNumber() {
		if (imaginaryPart >= 0) {
			cout << this->realPart << "+" << this->imaginaryPart << "i\n\n";
		}
		else {
			cout << this->realPart << this->imaginaryPart << "i\n\n";
		}
	}
};


int main() {
	ComplexNumbers obj1(7, 2);
	ComplexNumbers obj2(3, -5);
	obj1.showNumber(); obj2.showNumber();
	obj1 + obj2;
	obj1.showNumber();
	obj2 - obj1;
	obj2.showNumber();
	obj1 / obj2;
	obj1.showNumber();
	system("pause>nul");
	return 0;
}