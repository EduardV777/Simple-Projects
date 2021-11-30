#include <iostream>
#include <cstdlib>
using namespace std;
//Without recursion
int ExtractNumberFromFS(int n) {
	int* seq = new int[n]; seq[0] = 1; seq[1] = 1;
	for (int k = 2; k < n; k++) {
		seq[k] = seq[k - 1] + seq[k - 2];
	}
	int wantedNumber = seq[n-1];
	return wantedNumber;
}

//With recursion
int ExtractNumberFromFS2(int n, int* seq, int k = 2) {
	if (k >= n) {
		return seq[n-1];
	}
	else {
		seq[k] = seq[k - 1] + seq[k - 2];
		k++;
		return ExtractNumberFromFS2(n, seq, k);
	}
}

int main() {
	int n;
	cout << "Which number you'd like to extract from the fibonacci sequence? - "; cin >> n;
	int* seq = new int[n]; seq[0] = 1; seq[1] = 1;
	cout << "\nThe number you have chosen is: " << ExtractNumberFromFS2(n,seq) << endl;
	system("pause>nul");
	return 0;
}