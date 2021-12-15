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

    double getMoney(){
        double s=money;
        for(int k=1;k<=time;k++){
            s*=(1+rate/100);
        }
        return s;
    }

    void showAll() {
        cout<<"Name: "<<name<<"\nMoney: "<<money<<"\nRate: "<<rate<<"%\nTime: "<<time<<" years\nFinal sum: "<<getMoney()<<endl;
    }
};


int main() {
    MyMoney savings;
    savings.name="Eduard Velkov";
    savings.money=1000;
    savings.rate=8;
    savings.time=5;
    savings.showAll();
    system("pause>nul");
    return 0;
}
