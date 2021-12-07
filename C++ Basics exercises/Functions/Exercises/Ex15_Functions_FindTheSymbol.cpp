#include <iostream>
#include <cstdlib>
using namespace std;

int FindSymbol(char* textArr, char symbol) {
	int foundSymbol = 0;
	for (int k = 0; k < 120; k++) {
		if (textArr[k] == symbol) {
			foundSymbol += 1;
		}
	}
	return foundSymbol;
}

int main() {
	char Text[120] = "The program is going to try finding a certain symbol in me. It will return the number of times the symbol was found.";
	char symbol = 'a';
	cout << "'" << Text << "'" << endl;
	cout << "\nLooking for symbol '" << symbol << "'\nFound it: " << FindSymbol(Text, symbol) << " times.";
	system("pause>nul");
	return 0;
}