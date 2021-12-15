#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class MyMoney{
private:
    string name;
    double money;
    double rate;
    int time;

    double getMoney(){
        double s=money;
        for(int k=1;k<=time;k++){
            s*=(1+rate/100);
        }
        return s;
    }
public:
    void showAll() {
        cout<<"Name: "<<name<<"\nMoney: "<<money<<"\nRate: "<<rate<<"%\nTime: "<<time<<" years\nFinal sum: "<<getMoney()<<endl;
    }
    void setData(string clientName, double clientMoney, double clientRate, int clientTime){
        name=clientName;
        money=clientMoney;
        rate=clientRate;
        time=clientTime;
    }
    //variant 2 - set only name
    void setData(string clientName){
        name=clientName;
    }
    //variant 3 - set initial client sum and client rate
    void setData(double clientMoney,double clientRate){
        money=clientMoney;
        rate=clientRate;
    }
    //variant 4 - set client time
    void setData(int clientTime){
        time=clientTime;
    }

};

int main() {
    MyMoney bank1;
    bank1.setData("Eduard Velkov", 1000, 5, 8);
    bank1.setData("Eduard Robertinov");
    bank1.setData(2500,12);
    bank1.setData(10);
    bank1.showAll();
    system("pause>nul");
    return 0;
}
