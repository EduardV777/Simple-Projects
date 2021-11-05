import mysql.connector; import time
def LogIntoAccount(dbConnectionInfo):
    while True:
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
                print("\nSuccessful login!\n")
                break
            except:
                print("\nLogin data incorrect!\n")
                continue
    print(queryRes)
def CreateAccount(dbConnectionInfo):
    print("\n||Account creation||\n")
    while True:
        accName=input("Account Name: ")
        if len(accName)<4:
            print("\nYour account name must be atleast 4 symbols\n")
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
    dbConnectionInfo.commit()
    print("\nAccount successfully created!\n")
def main():
    #connect to DB
    hostAddress="localhost"; adminAccessName="root"; adminAccessPass="root"; db="accountdata"
    try:
        database=mysql.connector.connect(host=hostAddress, user=adminAccessName, password=adminAccessPass, database=db)
    except:
        print("[ERROR]: Failure connecting to database! Shutting down. . .\n         Report the problem at the developer's website\n")
        return 0
    timeTest=time.gmtime()
    print(timeTest)
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
        except ValueError:
            print("\nWrong option\n")
            continue
main()
