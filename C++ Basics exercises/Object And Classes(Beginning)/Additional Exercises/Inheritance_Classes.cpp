#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class MyMoney {
public:
	string name;
	double money;
	double rate;
	int time;


	MyMoney() {
		name = "";
		money = 0;
		rate = 0;
		time = 0;
	}
	MyMoney(string cN, double cM, double cR, int cT) {
		name = cN;
		money = cM;
		rate = cR;
		time = cT;
	}

	double getMoney() {
		double s = money;
		for (int k = 1; k <= time; k++) {
			s *= (1 + rate / 100);
		}
		return s;
	}
	void showAll() {
		cout << "Name: " << name << "\nMoney: " << money << " USD\nRate: " << rate << " %\nTime: " << time << " years\nFinal sum: " << getMoney() << " USD\n";
	}
	void setData(string clientName, double clientMoney, double clientRate, int clientTime) {
		name = clientName;
		money = clientMoney;
		rate = clientRate;
		time = clientTime;
		for (int k = 1; k <= 45; k++) {
			cout << "-";
		}
		cout << endl << "\nData of object " << this << " has been updated.\n";
		for (int k = 1; k <= 45; k++) {
			cout << "-";
		}
		cout << endl;
	}

};

class BigMoney :public MyMoney {
public:
	int periods;
	BigMoney() : MyMoney() {
		periods = 1 + rand() % 5;
	}
	BigMoney(string clientName, double clientMoney, double clientRate, int clientTime, int p) : MyMoney(clientName, clientMoney, clientRate, clientTime) {
		periods = p;
	}

	double getMoney() {
		double s = money;
		for (int k = 1; k <= time * periods; k++) {
			s *= (1 + rate / 100/periods);
		}
		return s;
	}
	void showAll() {
		MyMoney::showAll();
		cout << "Accruals per year: " << periods << "\n";
	}
	void setData(string clientName, double clientMoney, double clientRate, int clientTime, int p) {
		MyMoney::setData(clientName, clientMoney, clientRate, clientTime);
		periods = p;
	}
};

int main() {
	srand(2);
	MyMoney objA("Ivan Ivanov",1200,3,9);
	objA.showAll();
	cout << endl;
	BigMoney objB("Ivan Ivanov",1200,3,9,3);
	objB.showAll();
	objB.setData("Ivan Petkov", 3500, 4, 8, 5);
	objB.showAll();
	system("pause>nul");
	return 0;
}
