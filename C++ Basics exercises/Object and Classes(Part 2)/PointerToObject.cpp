#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

class Points {
public:
	string objName;
	int pts;
	void showPoints() {
		cout << "Object name: "<< objName << "   |   " << "Points: " << pts << endl;
	}
};

int main() {
	Points obj1, obj2;
	Points *p = &obj1;
	p->objName = "obj1"; p->pts = 3500;
	p->showPoints();
	p = &obj2;
	p->objName = "obj2"; p->pts = 6000;
	p->showPoints();
	cout << "\nChecking the values of these object by directly calling their method.\n";
	obj1.showPoints(); obj2.showPoints();
	return 0;
}
