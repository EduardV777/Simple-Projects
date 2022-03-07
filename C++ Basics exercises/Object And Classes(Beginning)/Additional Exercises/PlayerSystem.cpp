#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <string>
using namespace std;

class playerStats {
public:
	string playerName;
	int id, kills, deaths;
	double KD;

	playerStats() {
		//default
	}
	playerStats(int id, string playerName, int kills, int deaths) {
		this->id = id;
		this->playerName = playerName;
		this->kills = kills;
		this->deaths = deaths;
		if (kills != 0 || deaths != 0) {
			this->KD = (double)kills / deaths;
		}
		else {
			this->KD = 0;
		}
		cout << "New account with player name " << playerName << " created!\nID "<< id << endl;
		for (int k = 0; k <= 35; k++) {
			cout << "-";
		}
		cout << endl;
	}
	~playerStats() {
		cout << "Account of player " << playerName << " has been deleted!\nID(" << id << ")" << endl;
		for (int k = 0; k <= 35; k++) {
			cout << "-";
		}
		cout << endl;
	}
	void ChangeName() {
		string newName;
		cout << "Please enter your new name: ";
		getline(cin, newName);
		cout << endl;
		if (newName.length() < 14) {
			cout << "Player's name " << playerName << " was changed to " << newName << endl;
			for (int k = 0; k <= 35; k++) {
				cout << "-";
			}
			cout << endl;
			playerName = newName;
		}
		else {
			cout << "Error: This name is too long." << endl;
			for (int k = 0; k <= 35; k++) {
				cout << "-";
			}
			cout << endl;
		}
	}
	void viewStats() {
		cout << fixed << setprecision(2) << "ID: "<< id << "\nName: " << playerName << "\nKills: " << kills << "\nDeaths: " << deaths << "\nK/D: " << KD << endl;
		for (int k = 0; k <= 35; k++) {
			cout << "-";
		}
		cout << endl;
	}
	double UpdateKD(int currKills, int currDeaths) {
		cout << "Player's " << playerName << " K/D is updated." << endl;
		for (int k = 0; k <= 35; k++) {
			cout << "-";
		}
		cout << endl;
		return KD;
	}
	void IncreaseKills() {
		kills += 1;
		cout << "Player " << playerName << " now has " << kills << " kills.";
		UpdateKD(kills, deaths);
	}
	void IncreaseDeaths() {
		deaths += 1;
		cout << "Player " << playerName << " now has " << deaths << " deaths.";
		UpdateKD(kills, deaths);
	}
};

playerStats* CreateNewAccount(int IDct) {
	cout << "Nickname: ";
	string name;
	getline(cin, name);
	playerStats *newAcc = new playerStats(IDct,name, 0, 0);
	return newAcc;
}


int main() {
	playerStats* acc;
	int ct = 0;
	playerStats** accounts = new playerStats*[100];
	for (int k = 0; k <= 100; k++) {
		accounts[k] = 0;
	}
	/*playerStats account1(0, "Eduard", 15, 34);
	account1.viewStats();
	playerStats account2(1,"Roberto", 25, 13);
	account2.ChangeName();
	account2.viewStats();*/
	//cout << endl;
	//cout << endl;
	while (true) {
		for (; ct < 100; ct++) {
			if (accounts[ct] == 0) {
				break;
			}
		}
		string command;
		cout << "Command: ";
		getline(cin>>ws, command);
		cout << endl;
		if (command == "create new account") {
			acc = CreateNewAccount(ct);
			accounts[ct] = acc;
		}
		else if (command == "show stats") {
			bool found = false;
			int seekingID;
			cout << "Enter the id of the account: ";
			cin >> seekingID;
			if ((seekingID < 100 && seekingID>=0) && accounts[seekingID]!=0) {
				accounts[seekingID]->viewStats();
			}
			else {
				cout << "No such ID exists." << endl;
			}
		} else if(command == "quit") {
			break;
		}
		else if (command == "delete account") {
			cout << "Please enter the id of the account: ";
			int seekingID;
			cin >> seekingID;
			if ((seekingID > 100 or seekingID<0) || accounts[seekingID] == 0) {
				cout << "No such ID exists." << endl;
			}
			else {
				delete accounts[seekingID];
				accounts[seekingID] = 0;
			}
		}
		else if (command == "show all accounts") {
			for (int i = 0; i <= 60; i++) {
				cout << "_";
			}
			cout << endl;
			for (int k = 0; k < 100; k++) {
				if (accounts[k] == 0) {
					break;
				}
				else {
					accounts[k]->viewStats();
					for (int i = 0; i <= 10; i++) {
						cout << "-";
					}
					cout << endl;
				}
			}
			for (int i = 0; i <= 60; i++) {
				cout << "_";
			}
			cout << endl << endl;
		}
	}
	return 0;
}
