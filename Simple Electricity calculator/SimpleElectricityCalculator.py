#NOT FINISHED

#day 6:00 - 22:00 night 22:00 - 6:00
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
def performCalculation(appliancesList, days):
    #kwH
    dayTariff=0.14666; nightTariff=0.06245; totalConsumption=0
    for k in range(0,len(appliancesList)-1,+2):
        print(appliancesList[k])
        while True:
            dayTime=input(f"В каква част от денонощието използвате уреда {appliancesList[k]}(Пример: Day, DayNight, Night) - ")
            if dayTime=="Day":
                while True:
                    hours=int(input("Колко часа от деня използвате уреда?"))
                    if hours>16:
                        print(f"[Грешка]: Надвишавате часовете за избраната част от денонощието - {dayTime}")
                    elif hours<1:
                        print(f"[Грешка]: Не може часовете да са под 0.")
                        continue
                    else:
                        hoursDay=hours
                        totalConsumption += ((appliancesList[k + 1] * hoursDay) * 0.14666)*days
                        break
            elif dayTime=="DayNight":
                while True:
                    hours=int(input("Колко часа от деня използвате уреда?"))
                    if hours>16:
                        print(f"[Грешка]: Надвишавате часовете за избраната част от денонощието - {dayTime}")
                    elif hours<1:
                        print(f"[Грешка]: Не може часовете да са под 0.")
                        continue
                    else:
                        hoursDay=hours
                        totalConsumption += ((appliancesList[k + 1] * hoursDay) * 0.14666)*days
                        while True:
                            hours = int(input("Колко часа от нощта използвате уреда?"))
                            if hours > 8:
                                print(f"[Грешка]: Надвишавате часовете за избраната част от денонощието - {dayTime}")
                            elif hours < 1:
                                print(f"[Грешка]: Не може часовете да са под 0.")
                                continue
                            else:
                                nightHours=hours
                                totalConsumption += ((appliancesList[k + 1] * nightHours) * 0.06245)*days
                                break
                        break
            elif dayTime=="Night":
                while True:
                    hours=int(input("Колко часа от нощта използвате уреда?"))
                    if hours>8:
                        print(f"[Грешка]: Надвишавате часовете за избраната част от денонощието - {dayTime}")
                    elif hours<1:
                        print(f"[Грешка]: Не може часовете да са под 0.")
                        continue
                    else:
                        nightHours=hours
                        totalConsumption += ((appliancesList[k + 1] * nightHours) * 0.06245)*days
                        break
            else:
                print("[Грешка]: Не въведохте правилно този параметър!\n\n")
                continue
            break
    print(f"Вашата консумация за период от {days} дни ще бъде - {totalConsumption:.2f} лева.")
def BeginCalculation():
    totalConsumption=0
    while True:
        if lang=="BG":
            print("Изберете вашия доставчик(CEZ / EVN / EnergoPro) - "); energySupplier=input()
            if energySupplier=="CEZ" or energySupplier=="cez":
                print("Много добре, вие избрахте доставчик CEZ!\nЗа какъв период искате да изчислите вашата консумация(дни)?")
                days=int(input())
                appliances=[]; consumptionW=[]
                print("[Внимание: За да преминете към следващия етап, въведете команда /next]\n")
                while True:
                    appliance=input("Въведете електроуред: ")
                    if len(appliance)<4:
                        print("[Грешка]: Минималната дължина на името на уреда е 4!\n\n")
                        continue
                    elif appliance=="/next":
                        #convert consumption to kwH
                        totalConsumption=totalConsumption/1000
                        performCalculation(appliances, days)
                        break
                    else:
                        consumptionOfAppliance=int(input(f"Въведете консумацията на {appliance}(W): "))
                        if consumptionOfAppliance<1:
                            print(f"[Грешка]: Невалидна консумация за уред {appliance} - {consumptionOfAppliance} W")
                            continue
                        else:
                            totalConsumption+=consumptionOfAppliance
                            #W->kWh
                            totalConsumption/=1000
                            appliances.append(appliance); appliances.append(totalConsumption)
            elif energySupplier=="EVN" or energySupplier=="evn":
                pass
            elif energySupplier=="EnergoPro" or energySupplier=="energopro" or energySupplier=="Energopro":
                pass
            else:
                print("[Грешка]: Невалиден доставчик! Опитайте пак.\n\n")
                continue

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
