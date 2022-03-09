#include <iostream>
#include <cstdlib>
using namespace std;

class MyClass {
public:
	char label;
	MyClass *nextObject;

	void showLabel() {
		if (nextObject) {
			cout << nextObject->label << " ";
			nextObject->showLabel();
		}
	}

	~MyClass() {
		cout << "Object " << label << " was deleted.\n";
	}
};

int DeleteChainOfObjects(MyClass *obj1) {
	MyClass *next;
	if (obj1->nextObject) {
		next = obj1->nextObject;
	}
	else {
		delete obj1->nextObject; delete obj1;
		return 0;
	}
	delete obj1;
	DeleteChainOfObjects(next);
}


int main() {
	int n = 10;
	MyClass *obj1 = new MyClass, *p=obj1;
	obj1->label = 'A';
	cout << obj1->label << " ";
	for (int k = 1; k <= 10; k++) {
		if (k == 10) {
			p->nextObject = 0;
		}
		else {
			p->nextObject = new MyClass;
			p->nextObject->label = p->label + 1;
			p = p->nextObject;
		}
	}
	obj1->showLabel();
	cout << endl;
	DeleteChainOfObjects(obj1);
	return 0;
}
