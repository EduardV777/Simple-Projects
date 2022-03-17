#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

const int n = 10;

class Taylor {
private:
	double c[n];
public:
	double &operator[](int k) {
		return c[k];
	}
	Taylor(double cf = 0) {
		for (int k = 0; k < n; k++) {
			(*this)[k] = cf;
		}
	}
	Taylor(double *cfList) {
		for (int k = 0; k < n; k++) {
			(*this)[k] = cfList[k];
		}
	}
	double operator()(double x) {
		double s = 0, q = 1;
		for (int k = 0; k < n; k++) {
			s += (*this)[k]*q;
			q *= x;
		}
		return s;
	}
};

int main() {
	double cfList[n] = { 0,1,0,1. / 3,0,2. / 15,0,17. / 315,0,62. / 2835 };
	Taylor expObj, f(1), tanObj(cfList);
	expObj[0] = 1;
	for (int k = 1; k < n; k++) {
		expObj[k] = expObj[k - 1] / k;
	}
	double x = 1.0;
	cout << expObj(x) << " -- " << exp(x) << endl;
	cout << tanObj(x) << " -- " << tan(x) << endl;
	cout << f(x/2) << " -- " << 1 / (1 - x / 2) << endl;
	return 0;
}
