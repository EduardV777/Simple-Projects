#include <iostream>
#include <cstdlib>
using namespace std;

void ReverseText(char* textArr,int textLength) {
	int rev = textLength;
	for (int k = textLength; k > -1; k--) {
		cout << textArr[k];
	}
	cout << endl;
}

/*
//Recursion test
void ReverseText(char* textArr, int textLength) {
	if (textLength == -1) {
		return;
	}
	int rev = textLength;
	cout << textArr[rev];
	textLength--;
	ReverseText(textArr, textLength);
}
*/

int main() {
	const int size = 100;
	char Text[size] = "This text will be shown in reversed order!";
	int length = 0;
	for (int k = 0; k < 100; k++) {
		if (Text[k] != '\0') {
			length += 1;
		}
		else {
			break;
		}
	}
	cout << Text << endl;
	ReverseText(Text,length);
	system("pause>nul");
	return 0;
}