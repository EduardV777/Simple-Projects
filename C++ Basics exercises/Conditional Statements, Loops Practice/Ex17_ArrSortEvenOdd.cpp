#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Numbers[10], odd=0, even=0, length=0, k=0;
	srand(6);
	cout << "{Generating array...}"<<endl<<endl;
	for (int& x : Numbers) {
		x = 1 + rand() % 10;
	}
	cout << "[Before sorting]Elements generated:" << endl;
	for (int& x : Numbers) {
		cout << x << " | ";
		length += 1;
	}
	cout << endl;
	cout << endl << endl << "{Sorting even and odd numbers in the sequence...}" << endl;
	//Bringing odd numbers before even numbers
	for (int i = 0, k=length-1; i < k; i++,k--) {
		if (Numbers[i]%2==0) {
			while (true) {
				if (Numbers[k] % 2 != 0) {
					int temp = Numbers[k];
					Numbers[k] = Numbers[i];
					Numbers[i] = temp;
					break;
				}
				else {
					k -= 1;
				}
			}
		}
		else {
			k += 1;
		}
	}
	//Counting odd and even numbers
	for (int& x : Numbers) {
		//cout << x << " | ";
		if (x % 2 == 0) {
			even += 1;
		}
		else {
			odd += 1;
		}
	}
	int lastIndex;
	//sorting odd numbers[asc.]
	for (int i = 1; i < odd; i++) {
		for (int j = 0; j < odd - i; j++) {
			if (Numbers[j] > Numbers[j + 1]) {
				int temp = Numbers[j + 1];
				Numbers[j + 1] = Numbers[j];
				Numbers[j] = temp;
			}
		}
		lastIndex = i+1;
	}
	//Sorting even numbers[asc.]
	for (int i = 1; i < even ; i++) {
		for (int j = lastIndex; j < (even+odd) - i; j++) {
			if (Numbers[j] > Numbers[j + 1]) {
				int temp=Numbers[j + 1];
				Numbers[j + 1] = Numbers[j];
				Numbers[j] = temp;
			}
		}
	}
	cout << endl << endl << "[After sorting]Elements sorted:"<<endl<<endl;
	for (int& x : Numbers) {
		cout << x << " | ";
	}
	cout << endl;
	system("pause>nul");
	return 0;
}