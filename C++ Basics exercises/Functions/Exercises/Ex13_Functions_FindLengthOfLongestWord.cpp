#include <iostream>
#include <cstdlib>
using namespace std;

int FindLongestWord(char* textArr) {
	int len = 0, maxLen=0;
	for (int k = 0; k < 100; k++) {
		if (textArr[k] != ' ' && textArr[k]!='\0') {
			len += 1;
		}
		else if (textArr[k] == '\0') {
			if (maxLen < len) {
				maxLen = len;
			}
			break;
		}
		else {
			if (maxLen < len) {
				maxLen = len;
			}
			len = 0;
		}
	}
	return maxLen;
}

int main() {
	char Text[100] = "Let's find the longest word in this sentence";
	cout << "'" << Text << "'";
	cout << "\n\nLongest word in the sentence is " << FindLongestWord(Text) << " characters long.";
	system("pause>nul");
	return 0;
}