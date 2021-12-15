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
};

int main() {
    MyMoney bank1,bank2;
    bank1.setData("Eduard Velkov", 1000, 8, 5);
    bank2.setData("Martin Taylor", 5000, 9, 7);
    bank1.showAll();
    cout<<endl;
    bank2.showAll();
    system("pause>nul");
    return 0;
}
