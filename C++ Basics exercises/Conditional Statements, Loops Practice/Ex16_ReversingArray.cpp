#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	int Numbers[10], length=0, j=0;
	srand(2);
	cout << "{Array generating...}";
	for (int& x : Numbers) {
		x = 1 + rand() % 11;
	}
	cout << "[Before reversing]Elements generated:" << endl;
	for (int& x : Numbers) {
		cout << x << " | ";
		length += 1;
	}
	//cout << endl << length << endl;
	cout << endl << endl << "{Reversing elements...}"<<endl<<endl;
	for (int i = length - 1; i > j; i--, j++) {
		//cout << endl << j << endl;
		int temp = Numbers[j];
		Numbers[j] = Numbers[i];
		Numbers[i] = temp;
	}
	cout << endl << endl << "{After reversing...}" << endl << endl;
	for (int& x : Numbers) {
		cout << x << " | ";
	}
	cout << endl << endl << "Action finished!";
	system("pause>nul");
	return 0;
}