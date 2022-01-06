#include <iostream>
#include <cstdlib>
using namespace std;

class NormalCar {
public:
	string brand, color, type; int tankCap, year; double consumption;

	NormalCar() {
		brand = "Toyota"; color = "Red"; year = 2013; type = "Hatchback"; tankCap = 55; consumption = 7.5;
	}
	NormalCar(string brand, string color, string type, int tankCap,int year, int consumption) {
		this->brand = brand; this->color = color; this->year = year; this->type = type; this->tankCap = tankCap; this->consumption = consumption;
	}

	double CalculateKmPerTank() {
		double km = (tankCap / consumption) * 100;
		return km;
	}

	void showCarDetails() {
		cout << "Brand - " << brand << "\nYear - " << year << "\nType - " << type << "\nFuel Capacity: " << tankCap << " L\nConsumption per 100km: " << consumption << " L\nWith a full tank you can drive: "<<CalculateKmPerTank()<<"km\n\n";
	}
};

class HeavyVehicle :public NormalCar {
public:
	double transportLimit; double priceGasolinePerL;
	
	HeavyVehicle() {
		this->brand = "Mercedes"; this->color = "Silver Metallic"; this->year = 2019; this->type = "Trailer Truck"; this->tankCap = 400; this->consumption = 13.5;
		transportLimit = 55; priceGasolinePerL = 2.20;
	}
	HeavyVehicle(string brand, string color, string type, int tankCap, int year, int consumption, double transportLimit, double priceGasolinePerL) {
		this->brand = brand; this->color = color; this->year = year; this->type = type; this->tankCap = tankCap; this->consumption = consumption; this->transportLimit = transportLimit; this->priceGasolinePerL = priceGasolinePerL;
	}
	//calculate the cost of transport of one tone per km
	double CalculateTransportCost() {
		double cost = ((consumption / 100) * priceGasolinePerL) / transportLimit;
		return cost;
	}
	void showCarDetails() {
		cout << "Brand - " << brand << "\nYear - " << year << "\nType - " << type << "\nTransport Limit: "<< transportLimit << " tones\nFuel Capacity: " << tankCap << " L\nConsumption per 100km: " << consumption << " L\nCost of transport per tone/km: "<<CalculateTransportCost()<<"\n\n";
	}
};

int main() {
	NormalCar car1("Ferrari","Red","Sports Car",50,2009,7.5);
	car1.showCarDetails();
	HeavyVehicle transportVan1("Renault","Yellow","Van",45,2019,9.3,3,2.34);
	transportVan1.showCarDetails();
	system("pause>nul");
	return 0;
}