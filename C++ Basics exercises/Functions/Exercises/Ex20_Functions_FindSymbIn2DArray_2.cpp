#include <iostream>
#include <cstdlib>
using namespace std;

int FindSymb(const char** array,char symbol) {
	int found = 0;
	for (int k = 0; k < 5; k++) {
		for (int j = 0; j < 100; j++) {
			if (array[k][j] == '\0') {
				break;
			}
			else if (symbol == array[k][j]) {
				found += 1;
			}
		}
	}
	return found;
}

int main() {
	const char** arr = new const char* [5];
	char symb;
	for (int k = 0; k < 5; k++) {
		arr[k] = new char[100];
	}
	arr[0] = "This is a text stored in 2D array on different rows.";
	arr[1] = "C++ is very interesting to learn as it provides many ways to complete different tasks";
	arr[2] = "For this example we will try to look for a certain symbol chosen by the user in this text.";
	arr[3] = "If the symbol is found n times, that will be printed at the end of this program.";
	arr[4] = "Lets see if it's successful.";
	//output text
	for (int k = 0; k < 5; k++) {
		cout << arr[k];
		cout << endl;
	}
	cout << "\nWhich symbol do you want to look for? - "; cin >> symb; cout << "\nThe symbol " << symb << " was found: " << FindSymb(arr,symb) << " times.\n";
	system("pause>nul");
	return 0;
}