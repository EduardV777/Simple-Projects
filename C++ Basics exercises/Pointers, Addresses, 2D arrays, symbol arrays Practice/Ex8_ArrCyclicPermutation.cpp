#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int size;
	cout << "Array Size: "; cin >> size; cout << endl;
	int* p = new int[size];
	//user input values in Arr
	for (int k=0; k < size; k++) {
		cout << "Array element " << k+1 << " value: "; cin >> p[k]; cout << endl;
	}
	/*output values of Arr test
	cout << endl << "Array values:\n";
	for (int k = 0; k < size; k++) {
		cout << p[k] << " | ";
	}
	*/
	int skip;
	cout << endl << "Value 'K': "; cin >> skip; cout << endl;
	int* p2 = new int[size];
	int nextElement = skip - 1, k=0, k2=0;
	//output original array
	cout << endl << "Array before cyclic permutation:\n";
	for (int j = 0; j < size; j++) {
		cout << p[j] << " | ";
	}
	cout << endl;
	//permutation process starts 10 5 65 104 1 0 2
	while (k < size) {
		if (k2 < size) {
			int i = 0;
			if (nextElement >= size) {
				nextElement -= size;
			}
			if (k == nextElement) {
				//put the element value in the second array that is gonna store the result after the permutation
				p2[k2] = p[k];
				p[k] = -400;
				k2 += 1; int times=0;
				//calculate the nextElement in the permutation
				while (i < skip) {
					if (times == size - 1 && k2==size) {
						break;
					}
					if (nextElement >= size-1) {
						nextElement = 0;
					} else {
						nextElement += 1;
					}
					if (p[nextElement] == -400) {
						times++;
						continue;
					}
					else {
						times = 0;
						i++;
					}
				}
			}
			else {
				k++;
				if (k == size) {
					k = 0;
				}
			}
		//test output
			//for (int j = 0; j < size; j++) {
				//cout << p2[j] << " | ";
			//}
		//TEST
		}
		else {
			break;
		}
	}
	//output the new sequence stored in the second dynamic array
	cout << endl << "Array after cyclic permutation:\n";
	for (k = 0; k < size; k++) {
		cout << p2[k] << " | ";
	}
	cout << endl;
	std::system("pause>nul");
	return 0;
}