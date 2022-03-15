#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class MyWords {
public:
	string word;
	bool state;

	MyWords() {
		word = "";
		state = true;
	}

	void read() {
		cout << word << " ";
		if (state) {
			(this + 1)->read();
		}
	}
};

int main() {
	const int n = 5;
	string wordsToAdd[n] = { "one","two","three","four","five" };
	MyWords wordsObjs[n];
	for (int k = 0; k < 5; k++) {
		wordsObjs[k].word = wordsToAdd[k];
		if (k == n-1) {
			wordsObjs[k].state = false;
		}
	}
	wordsObjs[0].read();
	cout << endl;
	wordsObjs[3].read();
	cout << endl;
	return 0;
}
