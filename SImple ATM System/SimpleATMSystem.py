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
        global head2; global optionChoice; global errChoice; global req1; global req2; global err1; global err2; global blockedMsg; global suspendedMsg
        global req3; global req4; global errReg; global errPin; global errExists; global regSuccess
        if lang=="BG":
            head2="\n\n\n----Регистрация на нов банков номер----\n"
            optionChoice="Изберете опция:\n1 (Регистрирайте нов банков номер)\n2 (Проверете съществуваща сметката)"
            regSuccess="Сметката Ви е регистрирана успешно в системата!"
            req1="Моля, въведете номера на вашата банкова сметка: "; req2="\nВъведете ПИН код: "; req3="Въведете номера на вашата нова сметка: "; req4="Въведете ПИН код за вход в системата: "
            errExists="\n\nТози банков номер вече съществува!\n\n"; errPin="\n\nПИН кодът е неправилен. ПИН кодовете са с дължина от 4 символа."; errReg="\n\nНомерът бе въведен неправилно.\nДължината на банков номер е 12 символа.\n\n"; errChoice="\n\n[ГРЕШКА]: Неправилен избор!\n\n"; err1="\n\n[ГРЕШКА]: Въведеният банков номер не е валиден.\n\n"; err2="\n\n[ГРЕШКА]: Въведеният пин за тази сметка е неправилен!\n\n"
            blockedMsg="\n\n|Банковата сметка е блокирана временно за 30 минути!|"; suspendedMsg="\n\n|Банковата сметка е временно блокирана.|\n\n"
        elif lang=="EN":
            optionChoice = "Make a choice:\n1 (Register new bank account number)\n2 (Check an already existing bank account)"
            req1="Please, enter the number of your bank acount: "; req2="\nEnter PIN code: "
            errChoice="\n\n[ERROR]: Incorrect choice!\n\n"; err1 = "\n\n[ERROR]: The bank account number is invalid.\n\n"; err2 = "\n\n[ERROR]: The pin you entered is not valid for this bank account!\n\n"
            blockedMsg = "\n\n|The bank account is temporarily suspended for 30 minutes!|"
    initConfig()
    constructMessages()
    print(head)
    while True:
        choice=input(optionChoice)
        if choice!="1" and choice!="2":
            print(errChoice)
            continue
        else:
            break
    if choice=="1":
        print(head2)
        while True:
            newBankNumber=input(req3)
            if len(newBankNumber)<12:
                print(errReg)
            elif len(newBankNumber)>12:
                print(errReg)
            else:
                #check if it already exists
                try:
                    if BankAccounts.allBankNumbers.index(newBankNumber)>-1:
                        print(errExists)
                except ValueError:
                    break
        while True:
            newPin=input(req4)
            if len(newPin)<4:
                print(errPin)
            elif len(newPin)>4:
                print(errPin)
            else:
                BankAccounts.allBankNumbers.append(newBankNumber); BankAccounts.pins.append(newPin); BankAccounts.accountState.append("active"); BankAccounts.suspensionTime.append(0); BankAccounts.bankBalance.append(0)
                print(regSuccess)
                break
        main()
    if choice=="2":
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
