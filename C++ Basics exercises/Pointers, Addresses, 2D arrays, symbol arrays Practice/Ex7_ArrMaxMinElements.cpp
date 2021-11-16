#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Arr[6], highestNum, lowestNum, highInd=0, lowInd=0;
	srand(2);
	for (int k = 0; k < 6; k++) {
		Arr[k] = 1 + rand() % 7;
	}
	for (int& x: Arr) {
		cout << x << " | ";
	}
	cout << endl;
	for (int i = 0; i < 2; i++) {
		if (i == 0){
			highestNum = Arr[0];
			for (int k = 0; k < 6; k++) {
				if (Arr[k] > highestNum) {
					highestNum = Arr[k];
					highInd = k;
				}
			}
		}
		else if (i == 1) {
			lowestNum = Arr[0];
			for (int j = 0; j < 6; j++) {
				if (Arr[j]<lowestNum){
					lowestNum = Arr[j];
					lowInd = j;
				}
			}
		}
	}
	cout << "Highest element is: " << highestNum << " [Index:" << highInd << "]" << endl << "Lowest element is: " << lowestNum << " [Index:" << lowInd << "]" << endl;
	system("pause>nul");
	return 0;
}