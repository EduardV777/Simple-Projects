#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

const int n = 10;

class Taylor {
public:
	double c[n];
	Taylor(double cf = 0) {
		for (int k = 0; k < n; k++) {
			c[k] = cf;
		}
	}
	Taylor(double *cfList) {
		for (int k = 0; k < n; k++) {
			c[k] = cfList[k];
		}
	}

	double Calc(double x) {
		double s = 0, q = 1;
		for (int k = 0; k < n; k++) {
			s += c[k] * q;
			q *= x;
		}
		return s;
	}
};


int main() {
	double tanCf[n] = { 0,1,0,1. / 3,0,2. / 15,0,17. / 315,0,62. / 2835 };
	Taylor expObj, f(1), tanObj(tanCf);
	expObj.c[0] = 1;
	for (int k = 1; k < n; k++) {
		expObj.c[k] = expObj.c[k-1]/k;
	}
	double x = 1.00;
	cout << expObj.Calc(x) << " -- " << exp(x) << endl;
	cout << tanObj.Calc(x) << " -- " << tan(x) << endl;
	cout << f.Calc(x/2) << " -- " << 1 / (1 - x / 2);
	return 0;
}
