import time
def initConfig(language="BG"):
    global lang; global head
    lang=language
    if lang=="BG":
        head="[Демо банкоматна система]\n\n"
    elif lang=="EN":
        head="Demo ATM system\n\n"
def CheckForSuspension():
    Time = time.time()
    return Time
class BankAccounts:
    allBankNumbers=["212019181716"]; pins=["0000"]; accountState=["active"]; suspensionTime=[0]; bankBalance=[5000]
def bankAccountControl():
    pass
def main():
    def constructMessages():
        global req1; global req2; global err1; global err2; global blockedMsg; global suspendedMsg
        if lang=="BG":
            req1="Моля, въведете номера на вашата банкова сметка: "; req2="\nВъведете ПИН код: "
            err1="\n\n[ГРЕШКА]: Въведеният банков номер не е валиден.\n\n"; err2="\n\n[ГРЕШКА]: Въведеният пин за тази сметка е неправилен!\n\n"
            blockedMsg="\n\n|Банковата система е блокирана временно!|"; suspendedMsg="\n\n|Банковата сметка е временно блокирана.|\n\n"
        elif lang=="EN":
            req1="Please, enter the number of your bank acount: "; req2="\nEnter PIN code: "
            err1 = "\n\n[ERROR]: The bank account number is invalid.\n\n"; err2 = "\n\n[ERROR]: The pin you entered is not valid for this bank account!\n\n"
            blockedMsg = "\n\n|The bank account is temporarily suspended!|"
    initConfig()
    constructMessages()
    print(head)
    while True:
        bankNumber=input(req1)
        try:
            if BankAccounts.allBankNumbers.index(bankNumber)>=0:
                slot=BankAccounts.allBankNumbers.index(bankNumber)
                if BankAccounts.accountState[slot] == "suspended":
                    if CheckForSuspension()<BankAccounts.suspensionTime[slot]:
                        print(suspendedMsg)
                        continue
                    else:
                        print("Сметката ви е отблокирана")
                        break
                else:
                    break
        except ValueError:
            print(err1)
            continue
    wrongPin=0; loginSuspended=False
    while True:
        if wrongPin!=3:
            pin=input(req2)
            if pin==BankAccounts.pins[slot]:
                bankAccountControl()
                break
            else:
                print(err2)
                wrongPin+=1
                continue
        else:
            wrongPin=0; loginSuspended=True
            BankAccounts.accountState[slot]="suspended"
            suspendedTime=time.time()
            suspendedTime+=1800
            BankAccounts.suspensionTime[slot]=suspendedTime
            print(blockedMsg)
            break
    if loginSuspended==True:
        loginSuspended=False
        main()
main()