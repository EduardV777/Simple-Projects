#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class ParalellepipedDesc {
public:
	double len;
	double width;
	double height;

	ParalellepipedDesc() {
		len = 1 + rand() % 25;
		width = 1 + rand() % 25;
		height = 1 + rand() % 25;
		cout << "\n[Generated random data for object]\n\n\n";
	}
	ParalellepipedDesc(double l, double w, double h) {
		len = l;
		width = w;
		height = h;
		cout << "\n[Geometric figure created!]\n\n\n";
	}

	double CalculateVolume() {
		if (len == width and len == height and width == height) {
			return len * len * len;
		}
		else {
			return len * width * height;
		}
	}
	void showObjectData() {
		string figType;
		if (len == width and len == height and width == height) {
			figType = "Cube";
		}
		else {
			figType = "Cuboid";
		}
		cout << "Figure Type: Paralellepiped["<< figType <<"]\nWidth = " << width << "\nLength = " << len << "\nHeight = " << height << "\n";
	}
};


class ParalellepipedMass : public ParalellepipedDesc {
public:
	double mass, V;
	ParalellepipedMass() {
		mass = 5000 + rand() % 5000;
		V = ParalellepipedDesc::CalculateVolume();
	}
	double getDensity() {
		return mass / V;
	}
	void ShowMatDensity() {
		cout << "\nDensity of the material that the figure is made of = " << getDensity() << " g/cm3\n";
	}
	void showObjectData() {
		ParalellepipedDesc::showObjectData();
		cout << "Volume = " << V << " g/cm3\n";
	}
	double operator/(double num) {
		V/=num;
		cout << "\n[Figure's volume has been decreased "<< num <<" times.]\n\n";
		return V;
	}
	ParalellepipedMass operator+(ParalellepipedMass obj2) {
		ParalellepipedMass newFig;
		newFig.len = len+obj2.len + width+obj2.width + height+obj2.height / 6;
		newFig.width = len + obj2.len + width + obj2.width + height + obj2.height / 6;
		newFig.height = len + obj2.len + width + obj2.width + height + obj2.height / 6;
		newFig.V = V+obj2.V;
		newFig.mass = mass+obj2.mass;
		cout << "\n[Created new figure with this arithmetic operation]\n";
		return newFig;
	}
};

int main() {
	ParalellepipedMass obj1,obj2;
	obj1.showObjectData();
	cout << endl;
	obj2.showObjectData();
	obj1.ShowMatDensity();
	//obj1 / 2;
	//obj1.showObjectData();
	ParalellepipedMass obj3 = obj1 + obj2;
	obj3.showObjectData();
	system("pause>nul");
	return 0;
}