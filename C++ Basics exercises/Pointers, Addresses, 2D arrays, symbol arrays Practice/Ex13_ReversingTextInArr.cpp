#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
	char Text[100] = "This sentence is about to be reversed";
	/* Variant 1
	string Txt;
	//string Txt = "This sentence is about to be reversed";
	Txt = Text;
	//reversing Txt
	reverse(Txt.begin(),Txt.end());
	cout << Txt;
	*/

	/*Variant 2
	string Arr[100];
	for (int k = 37, j=0; k > -1; k--,j++) {
		Arr[j] = Text[k];
	}
	for (int j = 0; j < 100; j++) {
		cout << Arr[j];
	}
	*/
	system("pause>nul");
	return 0;
}