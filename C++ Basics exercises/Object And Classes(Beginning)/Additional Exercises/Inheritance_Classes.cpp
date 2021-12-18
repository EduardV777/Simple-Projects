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

	double getMoney() {
		double s = money;
		for (int k = 1; k <= time; k++) {
			s *= (1 + rate / 100);
		}
		return s;
	}
	void showAll() {
		cout << "Name: " << name << "\nMoney: " << money << " USD\nRate: " << rate << " %\nTime: " << time << " years\nFinal sum: " << getMoney() << " USD\n";
		for (int k = 1; k <= 35; k++) {
			cout << "-";
		}
		cout << endl;
	}
	void setData(string clientName,double clientMoney,double clientRate,int clientTime) {
		name = clientName;
		money = clientMoney;
		rate = clientRate;
		time = clientTime;
	}

	double operator-(MyMoney obj) {
		return getMoney() - obj.getMoney();
	}
	double operator--() {
		if (money >= 1000) {
			money -= 1000;
		}
		else {
			money = 0;
		}
		return money;
	}
	int operator--(int) {
		if (time > 0) {
			time-=1;
		}
		return time;
	}
	MyMoney operator+(MyMoney obj) {
		MyMoney tmp;
		tmp.name = "Eduard Velkov";
		tmp.money = money + obj.money;
		tmp.rate = rate + obj.rate;
		tmp.time = time + obj.time / 2;
		return tmp;
	}
	double operator++() {
		money += 1000;
		return money;
	}
	int operator++(int) {
		time += 1;
		return time;
	}
};

int main() {
	MyMoney obj1, obj2;
	obj1.setData("Ivan Koichev", 1500, 5, 7);
	obj2.setData("Seth Baker", 1700, 2, 8);
	obj1.showAll(); obj2.showAll();
	cout << endl << endl;
	--obj1; obj2--; obj1.showAll(); obj2.showAll();
	cout << "\nSubstracting Seth's final sum from Ivan's final sum by applying the predefined '-' operator: " << obj2 - obj1 << " USD" << endl << endl;
	++obj1; obj2++; obj1.showAll(); obj2.showAll();
	MyMoney* obj3 = new MyMoney;
	*obj3 = obj1 + obj2;
	obj3->showAll();
	system("pause>nul");
	return 0;
}