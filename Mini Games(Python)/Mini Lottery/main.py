import mysql.connector; import time; import random

def PlayGame(gameMode, playerBalance):
    quit=False
    if gameMode=="1":
        amountNumbers=6; highLimit=49; jackpotAmount=100000
    elif gameMode=="2":
        amountNumbers=6; highLimit=45; jackpotAmount=75000
    elif gameMode=="3":
        amountNumbers=5; highLimit=35; jackpotAmount=25000
    selection=[]
    k=0; sameNumbersDetected=False
    while k<amountNumbers:
        while True:
            num=input(f"Choose number {k+1}: ")
            num=int(num)
            if k!=0:
                for j in range(0,len(selection)):
                    if num==selection[j]:
                        sameNumbersDetected=True
                        print("\nYou already have that number in your selection!\n")
                        break
            if sameNumbersDetected==True:
                sameNumbersDetected=False
                continue
            else:
                if 1 <= num <= highLimit:
                    selection.append(num)
                    k += 1
                else:
                    print(f"\nNumbers in this game are between 1 and {highLimit}\n")
                    continue
                break
    while True:
        print(f"\nYour selection:\n")
        selectionOutput=""
        for i in range(0,len(selection)):
            if i == len(selection) - 1:
                selectionOutput+=str(selection[i])
            else:
                selectionOutput += str(selection[i])+","

        print(selectionOutput)
        print("\nDo you want to proceed, change a number in your selection or return?\n")
        while True:
            userChoice=input("- ")
            if userChoice=="Proceed" or userChoice=="proceed":
                print("\nProceeding . . .\n\nHow much BetCoins would you like to bet?\n")
                while True:
                    bet=float(input("Bet: \n\n"))
                    if bet>playerBalance:
                        print(f"\nYour bet exceeds your maximum balance ({playerBalance})\n")
                        continue
                    else:
                        playerBalance-=bet
                        break
                generatedNumbers=[]
                k=0; rep=False; guessedNumbers=0;
                while k<amountNumbers:
                    genNum=round(1+random.random()*(highLimit+1))
                    if len(generatedNumbers)>0:
                        for j in range(0,len(generatedNumbers)):
                            if genNum==generatedNumbers[j]:
                                rep=True
                                break
                        if rep==True:
                            rep=False
                            continue
                    generatedNumbers.append(genNum)
                    k+=1
                print(generatedNumbers)
                for k in range(0,len(selection)):
                    for j in range(0,len(generatedNumbers)):
                        if selection[k]==generatedNumbers[j]:
                            guessedNumbers+=1
                if guessedNumbers==amountNumbers:
                    won=True; quit=True
                    print(f"\n\n\n\n\n\n\nYOU WON THE JACKPOT!!!\n***Winnings: {jackpotAmount} BetCoins***")
                    winnings=jackpotAmount
                    playerBalance+=winnings
                    print(f"You guessed {guessedNumbers} numbers.\nYour initial bet: {bet}\nYour winnings: {winnings}\n")
                    break
                else:
                    quit = True
                    if guessedNumbers==3:
                        winnings=bet+0.50
                        playerBalance += winnings
                    elif guessedNumbers==4:
                        winnings=bet+(bet*0.20)
                        playerBalance+=winnings
                    elif guessedNumbers==5:
                        winnings=bet+(bet*0.50)
                        playerBalance+=winnings
                    else:
                        winnings=0
                    print(f"You guessed {guessedNumbers} numbers.\nYour initial bet: {bet}\nYour winnings: {winnings}\n")
                    break

            elif userChoice=="Change" or userChoice=="change":
                while True:
                    whichNum=input("Which number do you want to change?\n- ")
                    whichNum=int(whichNum)
                    for k in range(0,len(selection)):
                        if whichNum==selection[k]:
                            while True:
                                num=input(f"Choose new number {k+1}: ")
                                num=int(num)
                                if 1<=num<=highLimit:
                                    for j in range(0,len(selection)):
                                        if num==selection[j]:
                                            print("\nYou have that number already in your selection.\n")
                                            sameNumbersDetected=True
                                            break
                                else:
                                    print(f"\nNumber must be between 1 and {highLimit}\n")
                                    continue
                                if sameNumbersDetected==True:
                                    sameNumbersDetected=False
                                    continue
                                else:
                                    selection[k]=num
                                    break
                            break
                    break
                break
            elif userChoice=="Return" or userChoice=="return":
                quit=True; break
            else:
                continue
        if quit==True:
            return playerBalance
        return playerBalance

def ControlPanel(name, accId, DbConnectionInfo):
    queryExecution.execute(f"Select accountBalance from accountstats where accountId='{accId}'")
    queryRes=queryExecution.fetchone()
    balance=queryRes[0]
    queryExecution.execute(f"Select playedGames, wonGames, lostGames from accountstats where accountId='{accId}'")
    queryRes = queryExecution.fetchone()
    par1=queryRes[0]; par2=queryRes[1]; par3=queryRes[2]
    class currentAccountStats:
        accName=name; accBalance=float(balance)
        playedGamesTotal=par1; wonGamesTotal=par2; lostGamesTotal=par3
        currentlyPlayedGames=0; currentlyWonGames=0; currentlyLostGames=0
    print(f"\n\n\n\n\n\n|||Lottery game|||\n\nWelcome, {currentAccountStats.accName}\nCurrent balance: {currentAccountStats.accBalance} BetCoins\n\n")
    while True:
        print("1 - Bet   2 - Check account stats\n3 - Account operations   4 - Support\n5 - Log off")
        option=input("\n- ")
        if option=="1":
            if currentAccountStats.accBalance>0:
                print("What game do you want to bet on?\n1. 6/49\n2. 6/45\n3. 5/35\n")
                while True:
                    gameMode=input("- ")
                    if gameMode=="1":
                        print("\nYou have selected 6/49.\n")
                        res=PlayGame(gameMode,currentAccountStats.accBalance)
                        currentAccountStats.accBalance=res
                        if res==100000:
                            currentAccountStats.currentlyWonGames+=1
                        else:
                            currentAccountStats.currentlyLostGames+=1
                        currentAccountStats.currentlyPlayedGames+=1
                        break
                    elif gameMode=="2":
                        print("\nYou have selected 6/45\n")
                        res=PlayGame(gameMode,currentAccountStats.accBalance)
                        currentAccountStats.accBalance = res
                        if res == 100000:
                            currentAccountStats.currentlyWonGames += 1
                        else:
                            currentAccountStats.currentlyLostGames += 1
                        currentAccountStats.currentlyPlayedGames += 1
                        break
                    elif gameMode=="3":
                        print("\nYou have selected 5/35\n")
                        res=PlayGame(gameMode,currentAccountStats.accBalance)
                        currentAccountStats.accBalance = res
                        if res == 100000:
                            currentAccountStats.currentlyWonGames += 1
                        else:
                            currentAccountStats.currentlyLostGames += 1
                        currentAccountStats.currentlyPlayedGames += 1
                        break
            else:
                print("\nInsufficient BetCoin balance!\n")
                continue
        elif option=="2":
            print(f"Stats for account ID[{accId}]:\n\nTotal Played Games - {currentAccountStats.playedGamesTotal}\nTotal Won Games - {currentAccountStats.wonGamesTotal}\nTotal Lost Games - {currentAccountStats.lostGamesTotal}\nCurrent Balance: {currentAccountStats.accBalance} BetCoins\n\n")
            continue
        elif option=="3":
            while True:
                controlOption=input("\nEnter '1' if you wish to withdraw money from your current BetCoin balance\nEnter '2' if you wish to deposit funds into your BetCoin balance\nEnter '3' if you want to change your name/password\n\n[4]Return\n- ")
                if controlOption=="1":
                    print(f"Your current BetCoin balance is: {currentAccountStats.accBalance}\nEnter the amount of money you'd like to withdraw:\n")
                    withdrawAmount=float(input("- "))
                    if withdrawAmount>currentAccountStats.accBalance:
                        print("\nInsufficient funds!\n")
                        break
                    elif withdrawAmount==0:
                        print("\nYou can't withdraw 0 BetCoins\n")
                    else:
                        currentAccountStats.accBalance-=withdrawAmount
                        print("Operation completed!")
                        break
                elif controlOption=="2":
                    print("Enter the amount of money you'd like to deposit into your account:\n")
                    depositAmount=float(input("- "))
                    if depositAmount>10000:
                        print("\nSorry, deposits are limited to 10 000 USD\n")
                        break
                    elif depositAmount==0:
                        print("\nYou can't deposit 0 USD\n")
                    else:
                        currentAccountStats.accBalance+=depositAmount
                        print("\nOperation completed!\n")
                        break
                elif controlOption=="3":
                    print("Enter 'changePass' to change your password\nEnter 'changeName' to change your account name.\n\n[4]Return")
                    changeOption=input("- ")
                    if changeOption=='changePass':
                        while True:
                            currentPass=input("Enter your current password: ")
                            queryExecution.execute(f"Select accountPassword from accounts where accountId={accId}")
                            queryRes=queryExecution.fetchone()
                            realCurrentPass=queryRes[0]
                            if currentPass!=realCurrentPass:
                                print("\nIncorrect current password!\n")
                                continue
                            else:
                                while True:
                                    newPass=input("Enter your new password: ")
                                    if len(newPass)<5:
                                        print("\nPassword is too short! It must be at least 5 symbols long.\n")
                                        continue
                                    elif len(newPass)>20:
                                        print("\nPassword is too long! It must be below 20 symbols length.\n")
                                        continue
                                    else:
                                        queryExecution.execute(f"Update accounts set accountPassword={newPass} where accountId={accId} limit 1")
                                        DbConnectionInfo.commit()
                                        print("\nYou have changed your password successfully!\n")
                                        break
                                break
                    elif changeOption=="changeName":
                        while True:
                            currentPass=input("Enter your current password: ")
                            queryExecution.execute(f"Select accountPassword from accounts where accountId={accId}")
                            queryRes=queryExecution.fetchone()
                            if currentPass!=queryRes[0]:
                                print("\nIncorrect password!\n")
                            else:
                                while True:
                                    newName=input("New Account Name: ")
                                    if len(newName)<4:
                                        print("\nYour account name must be at least 4 symbols.\n")
                                        continue
                                    elif len(newName)>10:
                                        print("\nYour account name should not exceed 10 symbols length.\n")
                                        continue
                                    else:
                                        currentAccountStats.accName=newName
                                        queryExecution.execute(f"Update accounts set accountName='{newName}' where accountId={accId} limit 1")
                                        DbConnectionInfo.commit()
                                        print("\nYour account name has been successfully changed!\n")
                                        break
                                break
                    elif changeOption=="4":
                        continue
                elif controlOption=="4":
                    break
            continue
        elif option=="4":
            while True:
                choice=input("Try:\n[1]F.A.Q\n[2]Report a bug\n\n[4]Return\n- ")
                if choice=="1":
                    print("\n||Frequently Asked Questions||\n1. The game system can't startup and I get 'Failure connecting to the database' error. Why is that happening?\n-- Sometimes we are performing technical checks on our database and game system. We will usually post a notice about them before we take the server offline, but there could be cases when emergency shutdown is required to fix any problems that have arisen during the work of our server infrastructure.\nIn case you have a problem and we didn't post any notices, contact us through the report system.\n\n \n\n[4] Return\n")
                    while True:
                        userInput=input("-- ")
                        if userInput=="4" or not userInput=="4":
                            break
                elif choice=="2":
                    print("What kind of issue are your experiencing? Write down one of the following\n([1] - Login Issue, [2] - Registration issue, [3] - Account control issue, [4] - Slow/Failing transactions, [5] - Lottery bug\n")
                    while True:
                        issueCategory=""
                        issueCode=input("- ")
                        if issueCode=="1":
                            issueCategory="Login"
                            break
                        elif issueCode=="2":
                            issueCategory="Registration"
                            break
                        elif issueCode=="3":
                            issueCategory="Account Control"
                            break
                        elif issueCode=="4":
                            issueCategory="Transaction problem"
                            break
                        elif issueCode=="5":
                            issueCategory="Game bug"
                            break
                        else:
                            print("\nUnrecognised option!\n")
                            continue
                    print("Write detailed description of the problem you are experiencing(2000 max. symbols):\n")
                    while True:
                        problemDesc=input("- ")
                        if len(problemDesc)>2000:
                            print(problemDesc)
                            print("\n2000 characters exceeded! Cannot send report. You can copy and shorten you report above.\n\n")
                            continue
                        else:
                            queryExecution.execute("SELECT reportId from bugreports")
                            existingIds=queryExecution.fetchall()
                            reportId=round(random.random()*(1000*1000))
                            for k in range(0,len(existingIds)):
                                if reportId==existingIds[k]:
                                    reportId=reportId//1+random.random()*15
                            currentTime=time.gmtime()
                            reportTime=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                            queryExecution.execute(f"INSERT into bugreports VALUES({accId}, {reportId}, \"{problemDesc}\", '{reportTime}', '{issueCategory}')")
                            DbConnectionInfo.commit()
                            print("\nReport sent!\nWe will review the information you sent us and contact you within 48 hours.\nFeel free to contact us if you experience any other problems.\n\n")
                            break
                elif choice=="4":
                    break
        elif option=="5":
            print("\nLogging you off . . .\n")
            queryExecution.execute(f"Update accountstats set accountBalance={currentAccountStats.accBalance}, playedGames=playedGames+{currentAccountStats.currentlyPlayedGames}, wonGames=wonGames+{currentAccountStats.currentlyWonGames}, lostGames=lostGames+{currentAccountStats.currentlyLostGames} where accountId={accId}")
            DbConnectionInfo.commit()
            del accId; del name
            main()
            break
        else:
            continue

def LogIntoAccount(dbConnectionInfo):
    global successfullLogin
    successfullLogin=False
    while True:
        global userName; global queryExecution
        userName=input("Username: "); password=input("Password: ")
        print("\nLogging in . . .\n")
        queryExecution=dbConnectionInfo.cursor()
        queryExecution.execute(f"Select * from accounts where accountName='{userName}'")
        queryRes=queryExecution.fetchone()
        if queryRes=="None":
            print("\nUsername/Password is incorrect\n")
            continue
        else:
            queryExecution.execute(f"Select accountPassword from accounts where accountName='{userName}'")
            queryRes=queryExecution.fetchone()
            try:
                passw=queryRes.index(password)
                #check if account is suspended in case of successful logging in
                queryExecution.execute(f"Select accountStatus from accounts where accountName='{userName}'")
                queryRes = queryExecution.fetchone()
                if queryRes[0]=="suspended":
                    print(f"\n\nThis account with name {userName} is suspended.\n If you think this is a mistake, contact the administrator\n\n")
                    main()
                else:
                    print("\nSuccessful login!\n")
                    successfullLogin=True
                    break
            except:
                print("\nLogin data incorrect!\n")
                continue

def CreateAccount(dbConnectionInfo):
    print("\n||Account creation||\n\n**Every new account now gets free 20 BetCoins to help your luck at getting amazing rewards!**\n")
    while True:
        accName=input("Account Name: ")
        if len(accName)<4:
            print("\nYour account name must be at least 4 symbols\n")
            continue
        elif len(accName)>10:
            print("\nYour account name must not be over 10 symbols\n")
            continue
        else:
            break
    while True:
        accPass=input("Password: ")
        if len(accPass)<5:
            print("\nYour password must be atleast 5 symbols\n")
            continue
        elif len(accPass)>20:
            print("\nThat password is too long!\n")
            continue
        else:
            break
    #input new account data into DB
    currentDateTime=time.gmtime()
    queryExecution=dbConnectionInfo.cursor()
    queryExecution.execute(f"INSERT INTO accounts(accountName,accountPassword,creationDate) VALUES ('{accName}', '{accPass}', '{currentDateTime.tm_mday}.{currentDateTime.tm_mon}.{currentDateTime.tm_year} {currentDateTime.tm_hour}:{currentDateTime.tm_min}' )")
    queryExecution.execute("INSERT INTO accountStats(playedGames,wonGames,lostGames) VALUES(0,0,0)")
    dbConnectionInfo.commit()
    print("\nAccount successfully created!\n")

def main():
    #connect to DB
    hostAddress="localhost"; adminAccessName="accountControl"; adminAccessPass="control"; db="accountdata"
    try:
        database=mysql.connector.connect(host=hostAddress, user=adminAccessName, password=adminAccessPass, database=db)
    except:
        print("[ERROR]: Failure connecting to database! Shutting down. . .\n         Report the problem at the developer's website\n")
        return 0
    #timeTest=time.gmtime()
    #print(timeTest)
    while True:
        try:
            option=int(input("1 - Create a local account | 2 - Log in account\n -- "))
            if option==1:
                CreateAccount(database)
                continue
            elif option==2:
                LogIntoAccount(database)
            else:
                print("\nWrong option\n")
                continue
            break
        except ValueError:
            print("\nWrong option\n")
            continue
    if successfullLogin==True:
        queryExecution.execute(f"Select accountId from accounts where accountName='{userName}'")
        global accountId
        queryRes=queryExecution.fetchone()
        accountId=queryRes[0]
        ControlPanel(userName, accountId, database)
main()
