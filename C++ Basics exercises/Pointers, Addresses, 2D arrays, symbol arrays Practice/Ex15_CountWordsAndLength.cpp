#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	char Txt[100] = "I am learning programming";
	int words = 0, length = 0;
	for (int k = 0; k < 100; k++) {
		if (Txt[k] == '\0') {
			break;
		}
		cout << Txt[k];
	}
	cout << endl << endl;
	int k = 0;
	for (char& x : Txt) {
		if (x == '\0') {
			k += 1;
			cout << "Length of word " << k << ": " << length << endl;
			words = k;
			cout << "Amount of words in that string: " << words << endl;
			break;
		}
		if (x == ' ') {
			k += 1;
			cout << "Length of word " << k << ": " << length << endl;
			length = 0;
			continue;
		}
		length += 1;
	}
	system("pause>nul");
	return 0;
}