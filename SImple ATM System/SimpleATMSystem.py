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
def constructMessages(val1="", val2=0):
        global head2; global optionChoice; global errChoice; global req1; global req2; global err1; global err2; global blockedMsg; global suspendedMsg
        global req3; global req4; global errReg; global errPin; global errExists; global regSuccess; global contrMsg; global contrWrongOpt; global balanceOutput
        global depositMsg; global depositErr1; global depositErr2; global depositProcess; global depositSuccessful; global depositWithdraw; global depositImpossible
        global withdrawSuccess; global changePin; global changePinErr; global changePinErr2; global changePinErr3; global changePinBlocked; global changePinNew; global changePinSuccess
        if lang=="BG":
            head2="\n\n\n----Регистрация на нов банков номер----\n"
            optionChoice="Изберете опция:\n1 (Регистрирайте нов банков номер)\n2 (Проверете съществуваща сметката)\n"
            regSuccess="Сметката Ви е регистрирана успешно в системата!"
            req1="Моля, въведете номера на вашата банкова сметка: "; req2="\nВъведете ПИН код: "; req3="Въведете номера на вашата нова сметка: "; req4="Въведете ПИН код за вход в системата: "
            errExists="\n\nТози банков номер вече съществува!\n\n"; errPin="\n\nПИН кодът е неправилен. ПИН кодовете са с дължина от 4 символа."; errReg="\n\nНомерът бе въведен неправилно.\nДължината на банков номер е 12 символа.\n\n"; errChoice="\n\n[ГРЕШКА]: Неправилен избор!\n\n"; err1="\n\n[ГРЕШКА]: Въведеният банков номер не е валиден.\n\n"; err2="\n\n[ГРЕШКА]: Въведеният пин за тази сметка е неправилен!\n\n"
            blockedMsg="\n\n|Банковата сметка е блокирана временно за 30 минути!|\n\n"; suspendedMsg="\n\n|Банковата сметка е временно блокирана.|\n\n"
            contrMsg="\n\n\n\nИзберете опция:\n\n[1] Проверете баланса на сметката си\n[2] Депозирайте средства\n[3] Изтеглете средства\n[4] Сменете вашият ПИН код\n[5] Изход от системата"; contrWrongOpt="\nГрешна опция!\n"; balanceOutput=f"\n\nБанкова сметка номер [{val1}]\n\n - Налични средства ({val2} лева)\n\n[1] Продължи"; depositMsg=f"Текущи средства в сметката ({val2})\n\nВъведете сумата която искате да вкарате във вашата сметка - "
            depositErr1="\n\nНевалидна сума!\n\n"; depositErr2="\n\nМоля изпълнете операцията в банков клон!"; depositProcess="Обработка на транзакцията..."; depositSuccessful="\n\nУспешна транзакция!\n\n"; depositWithdraw="\n\nВъведете сумата която желаете да изтеглите - "; depositImpossible="\n\nНедостатъчна наличност!\n\n"; withdrawSuccess="\n\nУспешна транзакция!\n\n"; changePin="Въведете вашият текущ ПИН - "
            changePinErr="\n\nНевалиден ПИН! (3 максимални опита)\n\n"; changePinErr2="\n\nПИН кодът трябва да се състои от 4 символа.\n\n"; changePinBlocked="\n\nВашата сметка е блокирана за 30 минути!\n\n"; changePinNew="\n\nВъведете вашият нов ПИН код(4 цифри) - "; changePinErr3="\n\nПИН кодът не може да бъде същият, като текущият Ви ПИН код!\n\n"; changePinSuccess="\n\nУспешно променихте своя ПИН!\n\n"
        elif lang=="EN":
            optionChoice = "Make a choice:\n1 (Register new bank account number)\n2 (Check an already existing bank account)"
            req1="Please, enter the number of your bank acount: "; req2="\nEnter PIN code: "; req2="\nEnter PIN code: "; req3="Enter the number of your new bank account: "; req4="Enter PIN code to log into the system: "
            errExists="\n\nThis bank number already exists!\n\n"; errPin="\n\nPIN code is incorrect. PIN codes have length of 4 symbols."; errReg="\n\nGiven number is incorrect.\nThe length of a bank number is 12 symbols.\n\n"; errChoice="\n\n[ERROR]: Incorrect choice!\n\n"; err1 = "\n\n[ERROR]: The bank account number is invalid.\n\n"; err2 = "\n\n[ERROR]: The pin you entered is not valid for this bank account!\n\n"
            blockedMsg = "\n\n|The bank account is temporarily suspended for 30 minutes!|"; suspendedMsg="\n\n|Your bank account is temporarily suspended.|\n\n"
            contrMsg = "\n\n\n\nChoose an option:\n\n[1] Check account's balance\n[2] Deposit funds to your account\n[3] Withdraw funds from your account\n[4] Change your PIN code\n[5] Log out from the system"; contrWrongOpt = "\nWrong option!\n"; balanceOutput = f"\n\nBank account number [{val1}]\n\n - Available funds ({val2} leva)\n\n[1] Resume"; depositMsg = f"Current funds in this bank account ({val2})\n\nEnter the amount of funds you want to deposit in to your account - "
            depositErr1 = "\n\nInvalid sum!\n\n"; depositErr2 = "\n\nPlease, do this action at a bank office!"; depositProcess = "Processing transaction..."; depositSuccessful = "\n\nSuccessful transaction!\n\n";depositWithdraw = "\n\nEnter the amount of funds you want to withdraw - "; depositImpossible = "\n\nNot enough funds!\n\n"; withdrawSuccess = "\n\nSuccessful transaction!\n\n"; changePin = "Enter your current PIN code - "
initConfig()
def main():
    constructMessages()
    print(head)
    while True:
        choice=input(optionChoice)
        if choice!="1" and choice!="2" and choice!="/lang_EN":
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
                    global slot
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
                    constructMessages(BankAccounts.allBankNumbers[slot], BankAccounts.bankBalance[slot])
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
    elif choice=="/lang_EN":
        initConfig("EN")
        main()
def bankAccountControl():
    SafeGuard = False
    while True:
        if SafeGuard==True:
            del SafeGuard
            main()
            break
        print(contrMsg)
        option=input()
        if option=="1":
            print(balanceOutput)
            resume=""
            while resume!="1":
                resume=input()
                if resume!="1":
                    continue
                else:
                    break
            continue
        elif option=="2":
            while True:
                cash=input(depositMsg)
                if int(cash)<1:
                    print(depositErr1)
                    continue
                elif int(cash)>10000:
                    print(depositErr2)
                    continue
                else:
                    current_time=time.time()
                    print(depositProcess)
                    finishProcess_time=current_time+5
                    BankAccounts.bankBalance[slot]+=int(cash)
                    while True:
                        if time.time()>=finishProcess_time:
                            print(depositSuccessful)
                            constructMessages(BankAccounts.allBankNumbers[slot], BankAccounts.bankBalance[slot])
                            break
                        else:
                            continue
                break
        elif option=="3":
            cash=input(depositWithdraw)
            if int(cash)>10000:
                print(depositErr2)
            elif int(cash)>BankAccounts.bankBalance[slot]:
                print(depositImpossible)
            else:
                BankAccounts.bankBalance[slot]-=int(cash)
                constructMessages(BankAccounts.allBankNumbers[slot], BankAccounts.bankBalance[slot])
                print(withdrawSuccess)
        elif option=="4":
            wrongPin=0
            while True:
                if wrongPin!=3:
                    currentPin=input(changePin)
                    if currentPin!=BankAccounts.pins[slot]:
                        wrongPin+=1
                        print(changePinErr)
                        continue
                    else:
                        while True:
                            newPin=input(changePinNew)
                            if newPin>4 or newPin<4:
                                print(changePinErr2)
                                continue
                            elif newPin==currentPin:
                                print(changePinErr3)
                                continue
                            else:
                                BankAccounts.pins[slot]=newPin
                                print(changePinSuccess)
                                break
                else:
                    print(changePinBlocked)
                    suspensionTime=time.time()
                    suspensionTime+=1800
                    BankAccounts.suspensionTime[slot]=suspensionTime
                    BankAccounts.accountState[slot]="suspended"
                    SafeGuard=True
                    break
                break
        elif option=="5":
            main()
            break
        else:
            print(contrWrongOpt)
            continue
main()
