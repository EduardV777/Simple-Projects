import mysql.connector; import time; import hashlib; import random
global db_connection; global queryExecutor; global loginStatus
loginStatus=False
db_connection=mysql.connector.connect(host="localhost", user="admin", password="admin", database="cardealership"); queryExecutor=db_connection.cursor()

def listCurrentCarOffers():
    def SpecificOfferChoice(sellerName):
        while True:
            choice=input("\n[1] - Reveal seller's contact info\n[2] - View seller's rating\n[3] - Return\n - ")
            if choice=="1":
                a=round(1+random.random()*11); b=round(1+random.random()*11); res=a+b
                print(f"Confirm you are human: {a}+{b}=?")
                calc=input("- ")
                if int(calc)!=res:
                    print("\nUnsuccessful validation\n")
                    continue
                else:
                    queryExecutor.execute(f"SELECT email FROM accounts where username='{sellerName}'")
                    email=queryExecutor.fetchone()
                    print(f"Contact information for seller:\nE-mail: {email[0]}\n[1] - Contact | [2] - Return")
                    while True:
                        userContactChoice=input(" - ")
                        if userContactChoice=="1":
                            print("----Contact Form----\nTitle:")
                            title=input("- ")
                            print("Message:")
                            message=input("- ")

            elif choice=="2":
                pass
            elif choice=="3":
                return 0
    currentTime=time.localtime()
    print(f"\n\n---------LIST OF CURRENT CAR OFFERS POSTED HERE({currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min})---------")
    queryExecutor.execute("SELECT accounts.username, offerpostings.offerId, offerpostings.title, offerpostings.description, offerpostings.TYPE, offerpostings.fuelType, offerpostings.driveType, offerpostings.yearProd from accounts, offerpostings WHERE accounts.id=offerpostings.accountId limit 15")
    offers=queryExecutor.fetchall()
    offer="№: / By: / Offer id: / Title: / Description: / Type: / Fuel Type: / Drive Type: / Production Year: / Posted:\n\n"
    for k in range(0,len(offers)):
        offer+=str(k+1)+" | "
        for j in range(0,len(offers[k])):
            offer+=str(offers[k][j])+" | "
        if k!=len(offers)-1:
            offer+="\n---------------------------------------------------------------------------------------------------\n\n№: / By: / Offer id: / Title: / Description: / Type: / Fuel Type: / Drive Type: / Production Year: / Posted:\n\n"
    offer+="\n"
    print(offer)
    offersList=[]; j=0
    for k in range(0,15):
        if j==len(offers):
            break
        offersList.append(offers[k])
        j+=1
    print("[1-15]Select a specific offer for more details\n'Return' to return to main menu")
    while True:
        usrChoice=input(": ")
        if usrChoice=="1":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
            SpecificOfferChoice(offersList[int(usrChoice)-1][0])
            del offerOutput
        elif usrChoice=="2":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
            SpecificOfferChoice(offersList[int(usrChoice) - 1][0])
            del offerOutput
        elif usrChoice=="3":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
            SpecificOfferChoice(offersList[int(usrChoice) - 1][0])
            del offerOutput
        elif usrChoice=="4":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
            SpecificOfferChoice(offersList[int(usrChoice) - 1][0])
            del offerOutput
        elif usrChoice=="5":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="6":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="7":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="8":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="9":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="10":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="11":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="12":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="13":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="14":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
        elif usrChoice=="15":
            offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
            for k in range(0, len(offersList[int(usrChoice) - 1])):
                offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                j += 1
            print(offerOutput)
def RegisterAccount():
    while True:
        username=input("Select a username for your account: ")
        if len(username)<3:
            print("\nYour name should be longer than 2 symbols\n")
            continue
        else:
            break
    while True:
        failedStep = False
        password=input("Create a password for your account: ")
        if len(password)<5:
            print("\nPassword must be over 4 symbols\n")
            continue
        else:
            attempts=0
            while True:
                if attempts==3:
                    failedStep=True
                    print("\nYour passwords are not matching. Try creating your password again.\n")
                    break
                repeatPass=input("Confirm password: ")
                if repeatPass!=password:
                    print("\nPasswords are not matching\n")
                    attempts+=1
                    continue
                else:
                    passwordCrypted=hashlib.sha256(password.encode())
                    passwordCrypted=passwordCrypted.hexdigest()
                    del password
                    break
        if failedStep==True:
            del password
            continue
        else:
            break
    while True:
        email=input("Enter your e-mail: (Why?)")
        if email=="Why" or email=="WHY" or email=="why" or email=="Why?" or email=="WHY?" or email=="why?":
            print("\n*Your e-mail is required in case any changes are performed to your account to confirm that it is you doing them.\nAlso, your e-mail can be used to get contacted by other users regards your car offers posted here.\nYour e-mail also provides a way for admin to contact your in case the need arises.*\n")
            continue
        elif len(email)<3 or not "@" in email:
            print("\nE-mail is not correct.\n")
            continue
        else:
            break
    currentTime=time.gmtime()
    queryExecutor.execute(f"INSERT INTO accounts(username,PASSWORD,email, dateCreated) VAlUES('{username}','{passwordCrypted}','{email}','{currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year}');")
    db_connection.commit()
    print(f"\nYour account with username '{username}' has been created! You can now log in.\n")
    return 0

def LogInAcc():
    global username; global id
    username=""; id=0
    success=False
    while True:
        usernameOrEmail=input("Username or e-mail: "); password=input("Password: ")
        passwordCrypted=hashlib.sha256(password.encode()).hexdigest()
        try:
            if "@" in usernameOrEmail:
                queryExecutor.execute(f"SELECT PASSWORD from accounts where email='{usernameOrEmail}' LIMIT 1")
                passwordCryptedDb=queryExecutor.fetchone()
                queryExecutor.execute(f"SELECT username from account where email='{usernameOrEmail}' LIMIT 1")
                username=queryExecutor.fetchone()
                id=queryExecutor.execute(f"SELECT id from accounts where email='{usernameOrEmail}' LIMIT 1").fetchone()
            else:
                queryExecutor.execute(f"SELECT PASSWORD from accounts where username='{usernameOrEmail}' LIMIT 1")
                passwordCryptedDb=queryExecutor.fetchone()
            if passwordCrypted==passwordCryptedDb[0]:
                success=True
                break
            else:
                id=0
                print("\nIncorrect login credentials.\n")
        except:
            print("\nIncorrect login credentials.\n")
            continue
    if len(username)==0 or id==0:
        queryExecutor.execute(f"SELECT username from accounts where username='{usernameOrEmail}' LIMIT 1")
        username=queryExecutor.fetchone()
        queryExecutor.execute(f"SELECT id from accounts where username='{usernameOrEmail}' LIMIT 1")
        id=queryExecutor.fetchone()
    return success

def listCurrentOffers():
    pass

def postCarOffer():
    pass

def main():
    global loginStatus
    if loginStatus==True:
        currentTime=time.gmtime()
        if 5<=currentTime.tm_hour<=11:
            greeting="Good morning"
        elif 12<=currentTime.tm_hour<=15:
            greeting="Good day"
        elif 16<=currentTime.tm_hour<=18:
            greeting="Good afternoon"
        elif 19<=currentTime.tm_hour<=23:
            greeting="Good evening"
        else:
            greeting="Hello"
        class AccountData:
            accName=username[0]; accId=id[0]
    else:
        greeting="Hello"
    print("       Ed's Car Dealership\n")
    if loginStatus==True:
        print(f"{greeting}, {AccountData.accName}\n\n1 - Check the current car offers | 2 - Check your orders\n3 - Post a car offer | 4 - Send special request\n5 - Contact us\n6 - Account details/settings | 7 - Log off")
    else:
        print("Hello, Guest\n\n1 - Check the current car offers | 2 - Check your orders\n3 - Post a car offer | 4 - Send special request\n5 - Contact us\n6 - Log in your account | 7 - Register Account")

    while True:
        option=input("- ")
        if option=="1":
            listCurrentCarOffers()
        elif option=="2":
            pass
        elif option=="3":
            if loginStatus==False:
                print("\nYou need to log in your account first.\n")
            else:
                pass
                #postCarOffer()
        elif option=="4":
            pass
        elif option=="5":
            if loginStatus==False:
                continue
        elif option=="6":
            if loginStatus==False:
                print("\n\n\n\n\n\n")
                if LogInAcc()==True:
                    loginStatus=True
                main()
            else:
                pass
                #AccountDetailsSettings()
        elif option=="7":
            if loginStatus==True:
                del AccountData
                loginStatus=False
                main()
            else:
                print("\n\n\n\n\n\n")
                RegisterAccount()
                main()
        else:
            continue
main()