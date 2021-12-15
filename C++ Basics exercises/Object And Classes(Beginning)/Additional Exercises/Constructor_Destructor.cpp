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
    MyMoney(){
        name="Mr. Bean";
        money=200;
        rate=2;
        time=9;
        cout<<"Created client "<<name<<" with deposit of "<<money<<" USD.\n";
    }
    MyMoney(string clientName, double clientMoney, double clientRate, int clientTime){
        name=clientName;
        money=clientMoney;
        rate=clientRate;
        time=clientTime;
        cout<<"Created client "<<name<<" with deposit of "<<money<<" USD.\n";
    }
    ~MyMoney() {
        cout<<"Deleted client "<<name<<endl;
        for(int k=0;k<=35;k++){
            cout<<"*";
        }
        cout<<endl;
    }
    void showAll(){
        cout<<"Name: "<<name<<"\nMoney: "<<money<<"USD\nRate: "<<rate<<"%\nDeposit period: "<<time<<" years\nFinal sum: "<<getMoney()<<" USD"<<endl;
        for(int k=0;k<=35;k++){
            cout<<"-";
        }
        cout<<endl;
    }
    void setData(string clientName, double clientMoney, double clientRate, int clientTime){
        name=clientName;
        money=clientMoney;
        rate=clientRate;
        time=clientTime;
    }
};

MyMoney postman(){
    MyMoney objA("Postman Peyo",40000,3,7);
    return objA;
}

int main() {
    postman();
    MyMoney objB;
    objB.showAll();
    MyMoney *objC=new MyMoney("Petko Petkov",2000,1,8);
    objC->showAll();
    delete objC;
    system("pause>nul");
    return 0;
}
