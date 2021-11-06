import mysql.connector; import time
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
            pass
        elif option=="2":
            print(f"Stats for account ID[{accId}]:\nTotal Played Games - {currentAccountStats.playedGamesTotal}\nTotal Won Games - {currentAccountStats.wonGamesTotal}\nTotal Lost Games - {currentAccountStats.lostGamesTotal}\n\n")
            continue
        elif option=="3":
            while True:
                controlOption=input("\nEnter '1' if you wish to withdraw money from your current BetCoin balance\nEnter '2' if you wish to deposit funds into your BetCoin balance\nEnter '3' if you want to change your name/password\n\n[4]Return")
                if controlOption=="1":
                    print(f"Your current BetCoin balance is: {currentAccountStats.accBalance}\nEnter the amount of money you'd like to withdraw:\n")
                    withdrawAmount=float(input("- "))
                    if withdrawAmount>currentAccountStats.accBalance:
                        print("\nInsufficient funds!\n")
                        break
                    else:
                        currentAccountStats.accBalance-=withdrawAmount
                        print("Operation completed!")
                        break
                elif controlOption=="2":
                    print("Enter the amount of money you'd like to deposit into your account:\n")
                    depositAmount=float(input("- "))
                    if depositAmount>10000:
                        print("\nSorry, deposits are limited to 10 000\n")
                        break
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
            pass
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
    #print(queryRes)
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
        global accountId; accountId=""
        queryRes=queryExecution.fetchone()
        k=0
        #take actual id from query result
        while k<len(queryRes):
            if k!="(" or k!=",":
                for j in range(k,len(queryRes)):
                    if queryRes[j]!=",":
                        accountId+=str(queryRes[j])
                        k+=1
                    else:
                        k+=1
                        break
                break
            else:
                k+=1
        ControlPanel(userName, accountId, database)
main()
