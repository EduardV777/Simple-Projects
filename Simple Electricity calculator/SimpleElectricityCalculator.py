def initConfigure(language="BG"):
    global guide; global head; global lang; lang = language
    if lang=="BG":
        head="Прост калкулатор за ток"
        guide="Добре дошли в наръчника за правилно използване на тази програма! Моля имайте впредвид, че тази програма е създадена с демонстративна цел и не бива да се използва за реални битови сметки.\n" \
              "За да преминете през всички стъпки успешно следва да прочете наръчника докрай.\n1 - Най-напред ще видите стартовото меню, което Ви кани да изберете опция, според действието, което желаете да извършите.\n" \
              "При избиране на опция '1' вие ще пристъпите към нова калкулация. Ще бъдете подканени да въведете вашият доставчик на електроенергия, а след това ще имате възможност да въведете и уредите Ви и тяхната консумация.\n" \
              "Дължимата стойност на вашата консумация ще бъде изчислена за избрания период време от вас, след което ще имате възможност отново да изберете опция от заглавното меню.\n\n"
    else:
        head="Simple electricity calculator"
        guide="Welcome to the guide for proper use of this software! Please keep in mind, that the software has been created for demonstration purposes and in no way should be used for real calculations or commercial use.\n"\
              "To go through all steps successfully, you have to read the guide carefully.\n 1 - First of all you will see the starting menu where you can enter the option you choose according to the action you want to perform.\n"\
              "If you choose option '1', you will start a new calculation. You will be asked to enter the name of your energy supplier, after that you will be able to enter the appliances and their consumption.\n"\
              "The total cost of your consumption will be calculated for the chosen period of time. After you do that you will be able to enter a new option from the starting menu.\n\n"
def performCalculation(appliancesList, days, energySupplierCode, consumption):
    #kwH
    if energySupplierCode==1:
        dayTariff=0.14666; nightTariff=0.06245
    elif energySupplierCode==2:
        if consumption*days<=2499:
            dayTariff = 0.38636; nightTariff = 0.05464
        elif 2500<=consumption*days<=8300:
            dayTariff = 0.36944; nightTariff = 0.26208
    elif energySupplierCode==3:
        dayTariff = 0.14778; nightTariff = 0.05787
    totalConsumption=0; daytime=""
    def constructMessages(val1=0,val2=""):
        global msg3; global err1
        totalConsumption=val1; dayTime=val2
        if lang=="BG":
            msg3 = f"\nВашата консумация за период от {days} дни ще бъде - {totalConsumption:.2f} лева.\n\n"
            err1 = f"\n[Грешка]: Надвишавате часовете за избраната част от денонощието - {dayTime}\n"
        elif lang=="EN":
            msg3 = f"\nYour consumption for this period of {days} days will be - {totalConsumption:.2f} leva.\n\n"
            err1 = f"\n[Error]: You are exceeding the hours for this part of the day - {dayTime}\n"
    for k in range(0,len(appliancesList)-1,+2):
        if lang=="BG":
            msg1=f"В каква част от денонощието използвате уреда '{appliancesList[k]}' (Пример: Day, DayNight, Night) - "; msg2="Колко часа от деня използвате уреда?"
            err2=f"[Грешка]: Не може часовете да са под 0."; err3="[Грешка]: Не въведохте правилно този параметър!\n\n"
        elif lang=="EN":
            msg1 = f"In what time of the day are you using the appliance '{appliancesList[k]}' (Example: Day, DayNight, Night) - "; msg2 = "How much hours of the day are you using the appliance?"
            err2 = f"[Error]: Hours cannot be below 0."; err3 = "[Error]: You didn't enter that parameter correctly!\n\n"
        while True:
            dayTime=input(msg1)
            if dayTime=="Day":
                while True:
                    hours=int(input(msg2))
                    if hours>16:
                        constructMessages(0,dayTime)
                        print(err1)
                    elif hours<1:
                        print(err2)
                        continue
                    else:
                        hoursDay=hours
                        totalConsumption += ((appliancesList[k + 1] * hoursDay) * dayTariff)*days
                        break
            elif dayTime=="DayNight":
                while True:
                    hours=int(input(msg2))
                    if hours>16:
                        constructMessages(0, dayTime)
                        print(err1)
                    elif hours<1:
                        print(err2)
                        continue
                    else:
                        hoursDay=hours
                        totalConsumption += ((appliancesList[k + 1] * hoursDay) * dayTariff)*days
                        while True:
                            hours = int(input(msg2))
                            if hours > 8:
                                constructMessages(0, dayTime)
                                print(err1)
                            elif hours < 1:
                                print(err2)
                                continue
                            else:
                                nightHours=hours
                                totalConsumption += ((appliancesList[k + 1] * nightHours) * nightTariff)*days
                                break
                        break
            elif dayTime=="Night":
                while True:
                    hours=int(input(msg2))
                    if hours>8:
                        constructMessages(0, dayTime)
                        print(err1)
                    elif hours<1:
                        print(err2)
                        continue
                    else:
                        nightHours=hours
                        totalConsumption += ((appliancesList[k + 1] * nightHours) * nightTariff)*days
                        break
            else:
                print(err3)
                continue
            break
    constructMessages(totalConsumption, dayTime)
    print(msg3)
    main()
def BeginCalculation():
    totalConsumption=0
    def constructMessages (val1="",val2="",val3=0):
        global msg; global errInvalidConsumption; global ask2
        energySupplier=val1; appliance=val2; consumptionOfAppliance=val3
        if lang=="BG":
            msg = f"Много добре, вие избрахте доставчик {energySupplier}!\nЗа какъв период искате да изчислите вашата консумация(дни)?"
            errInvalidConsumption = f"\n[Грешка]: Невалидна консумация за уред '{appliance}' - {consumptionOfAppliance} W\n"
            ask2 = f"Въведете консумацията на {appliance}(W): "
        elif lang=="EN":
            msg = f"Very well, you chose supplier {energySupplier}!\nFor what period of time do you want to perform the calculation(days)?"
            errInvalidConsumption = f"\n[Error]: Invalid consumption for appliance '{appliance}' - {consumptionOfAppliance} W\n"
            ask2 = f"Enter consumption of {appliance}(W): "
    if lang=="BG":
        q1="Изберете вашия доставчик(CEZ / EVN / EnergoPro) - "
        errInvalidSupplier="[Грешка]: Невалиден доставчик! Опитайте пак.\n\n"; errLength="\n[Грешка]: Минималната дължина на името на уреда е 4!\n\n"
        notice1="\n[Внимание: За да преминете към следващия етап, въведете команда /next]\n"
        ask1="Въведете електроуред: "
    elif lang=="EN":
        q1 = "Choose your energy supplier(CEZ / EVN / EnergoPro) - "
        errInvalidSupplier = "[Error]: Invalid supplier! Try again.\n\n"; errLength = "\n[Error]: Minimum length of appliance's name is 4!\n\n"
        notice1 = "\n[Notice: To go to the next stage, enter the command /next]\n"
        ask1 = "Enter appliance name: "
    while True:
        energySupplier = input(q1)
        if energySupplier == "CEZ" or energySupplier == "cez":
            energySupplierCode = 1
            break
        elif energySupplier == "EVN" or energySupplier == "evn":
            energySupplierCode = 2
            break
        elif energySupplier == "EnergoPro" or energySupplier == "energopro" or energySupplier == "Energopro":
            energySupplier = "EnergoPro"
            energySupplierCode = 3
            break
        else:
            print(errInvalidSupplier)
            continue
    constructMessages(energySupplier)
    print(msg)
    days = int(input())
    appliances = []
    print(notice1)
    while True:
        appliance = input(ask1)
        if len(appliance) < 4:
            print(errLength)
            continue
        elif appliance == "/next":
            # convert consumption to kwH
            totalConsumption = totalConsumption / 1000
            performCalculation(appliances, days, energySupplierCode, totalConsumption)
            break
        else:
            constructMessages(energySupplier,appliance)
            consumptionOfAppliance = int(input(ask2))
            if consumptionOfAppliance < 1:
                print(errInvalidConsumption)
                continue
            else:
                totalConsumption += consumptionOfAppliance
                # W->kWh
                totalConsumption /= 1000
                appliances.append(appliance)
                appliances.append(totalConsumption)
def main():
    initConfigure()
    QuitRequested=False
    while True:
        if lang=="BG":
            message=f"--------------- {head} ---------------\n\n1 - Стартирай нова калкулация        2 - Прочети инструкциите за използване\n3 - Излез\n\n[Notice: To switch to the english version of this software write /lang_EN]\n"
        elif lang=="EN":
            message=f"--------------- {head} ---------------\n\n1 - Start new calculation        2 - Read a guide for proper use\n3 - Quit\n\n[Внимание: За да преминете към българската версия на тази програма наберете командата /lang_BG]\n"
        print(message)
        option=input()
        if option=="1":
            BeginCalculation()
            break
        elif option=="2":
            print(guide)
            continue
        elif option=="3":
            QuitRequested=True
            break
        elif option=="/lang_EN":
            initConfigure("EN")
        elif option=="/lang_BG":
            initConfigure("BG")
        else:
            if lang=="BG":
                print("[Грешка]: Бе избрана грешна опция! Моля опитайте отново.\n\n")
            if lang=="EN":
                print("[Error]: Incorrect option! Please try again.\n\n")
            continue
    if QuitRequested==True:
        return 0
main()
