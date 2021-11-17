import mysql.connector; import time; import hashlib; import random
global db_connection; global queryExecutor; global loginStatus
loginStatus=False
db_connection=mysql.connector.connect(host="localhost", user="admin", password="admin", database="cardealership"); queryExecutor=db_connection.cursor()

def listCurrentCarOffers():
    def SpecificOfferChoice(sellerName,offerId,accId):
        def ProcessOrder(user,accountId,offerId):
            print("\nProcessing order...\n")
            currentTime=time.localtime()
            queryExecutor.execute(f"SELECT * FROM offerpostings WHERE offerId={offerId} AND accountId={accId}")
            offerChoice=queryExecutor.fetchone()
            queryExecutor.execute(f"INSERT INTO userorders VALUES({accountId},{offerId},'{offerChoice[0][2]}','{offerChoice[0][3]}','{offerChoice[0][4]}','{offerChoice[0][5]}','{offerChoice[0][6]}','{offerChoice[0][7]}','{offerChoice[0][8]}','{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}','PENDING',{offerChoice[0][0]},'Waiting for seller response')")
            queryExecutor.execute(f"UPDATE myoffers SET status='Ordered' WHERE accountId={accId} AND offerId={offerId}")
            db_connection.commit()
            print("Order placed successfully!")

        if loginStatus==False:
            print("You can't view any additional information about this user and their offer, unless you log in your account.")
            print("Proceed?")
            proceed=input("- ")
        else:
            while True:
                choice=input("\n[1] - Reveal seller's contact info\n[2] - View seller's rating\n[3] - Order Now\n[4] - Return ")
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
                            elif userContactChoice=="2":
                                break

                elif choice=="2":
                    pass
                elif choice=="3":
                    print("Are you sure you wish to order that car?[Y]/[N]\n")
                    yesOrNo=input("- ")
                    if yesOrNo=="Y":
                        ProcessOrder(username[0],id[0],offerId)
                    else:
                        pass
                elif choice=="4":
                    return 0

    currentTime=time.localtime()
    print(f"\n\n---------LIST OF CURRENT CAR OFFERS POSTED HERE({currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min})---------")
    queryExecutor.execute("SELECT accounts.username, offerpostings.offerId, offerpostings.title, offerpostings.description, offerpostings.TYPE, offerpostings.fuelType, offerpostings.driveType, offerpostings.yearProd, offerpostings.datePosted FROM accounts, offerpostings WHERE accounts.id=offerpostings.accountId limit 15")
    offers=queryExecutor.fetchall()
    offer="№: / By: / Offer id: / Title: / Description: / Type: / Fuel Type: / Drive Type: / Production Year: / Posted:\n\n"
    for k in range(0,len(offers)):
        offer+=str(k+1)+" | "
        for j in range(0,len(offers[k])):
            offer+=str(offers[k][j])+" | "
        if k!=len(offers)-1:
            offer+="\n_____________________________________________________________________________________________\n\n№: / By: / Offer id: / Title: / Description: / Type: / Fuel Type: / Drive Type: / Production Year: / Posted:\n\n"
    offer+="\n"
    print(offer)
    offersList=[]; j=0
    for k in range(0,15):
        if j==len(offers):
            break
        offersList.append(offers[k])
        j+=1
    if len(offers)>0:
        print("[1-15]Select a specific offer for more details\n'Return' to return to main menu")
        while True:
            usrChoice=input(": ")
            if usrChoice=="return" or usrChoice=="Return" or usrChoice=="RETURN":
                return 0
            elif usrChoice=="1":
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice)-1][0]}'")
                accId=queryExecutor.fetchone(); offerId=offers[int(usrChoice)-1][1]
                SpecificOfferChoice(offersList[int(usrChoice)-1][0],offerId,accId[0])
                listCurrentCarOffers()
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
    else:
        print("No offers currently found. 'Return' to continue to the menu.")
        usrChoice=input()
        main()
def RegisterAccount():
    while True:
        username=input("Select a username for your account['Return' to go back to the menu]: ")
        queryExecutor.execute("SELECT * FROM reservednames")
        notAllowedNames=queryExecutor.fetchall(); blockedName=False
        #is name matching one of the reserved/blocked names
        for k in range(0,len(notAllowedNames)):
            if notAllowedNames[k][0].lower() in username.lower():
                print("\nThis name is taken or reserved. Please choose a different name.\n")
                blockedName=True
                continue
        if blockedName==True:
            continue
        #is name matching another user's name
        queryExecutor.execute("SELECT username FROM accounts")
        takenNames=queryExecutor.fetchall()
        for k in range(0,len(takenNames)):
            if username.lower()==takenNames[k][0].lower():
                print("\nThis name is taken or reserved. Please choose a different name.\n")
                blockedName=True
                break
        if blockedName==True:
            continue
        if len(username)<3:
            print("\nYour name should be longer than 2 symbols\n")
            continue
        elif username=="return" or username=="Return":
            return 0
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
        usernameOrEmail=input("Username or e-mail: ")
        if usernameOrEmail=="return" or usernameOrEmail=="Return":
            return success
        password=input("Password: ")
        if password=="return" or password=="Return":
            return success
        passwordCrypted=hashlib.sha256(password.encode()).hexdigest()
        try:
            if "@" in usernameOrEmail:
                queryExecutor.execute(f"SELECT PASSWORD FROM accounts WHERE email='{usernameOrEmail}' LIMIT 1")
                passwordCryptedDb=queryExecutor.fetchone()
                queryExecutor.execute(f"SELECT username FROM accounts WHERE email='{usernameOrEmail}' LIMIT 1")
                username=queryExecutor.fetchone()
                queryExecutor.execute(f"SELECT id FROM accounts WHERE email='{usernameOrEmail}' LIMIT 1")
                id=queryExecutor.fetchone()
            else:
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{usernameOrEmail}' LIMIT 1")
                id=queryExecutor.fetchone()
                queryExecutor.execute(f"SELECT username FROM accounts WHERE username='{usernameOrEmail}' LIMIT 1")
                username = queryExecutor.fetchone()
                queryExecutor.execute(f"SELECT PASSWORD FROM accounts WHERE username='{usernameOrEmail}' LIMIT 1")
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
    return success

def postCarOffer():
    queryExecutor.execute("SELECT * FROM reservednames")
    blockedWords = queryExecutor.fetchall()
    print("Write a title for your offer:\n")
    while True:
        title=input("- ")
        for k in range(0,len(blockedWords)):
            if blockedWords[k][0].lower() in title.lower() or blockedWords[k][0].upper() in title.upper():
                print("\nThat title cannot be posted. Change your title and make sure it does not contain profanities, personal names or other sensitive data.\n")
                continue
        if len(title)<5:
            print("\nYou can add a bit more information in your title.\n")
            continue
        else:
            break
    print("Write detailed description for your offer:\n")
    while True:
        desc=input("- ")
        for k in range(0,len(blockedWords)):
            if blockedWords[k][0].lower() in desc.lower() or blockedWords[k][0].upper() in desc.upper():
                print("\nYour description contains profanities. Please change your description.\n")
                continue
        if len(desc)<15:
            print("\nYour description is too short.\n")
            continue
        else:
            break
    print("What type of car is this?\n")
    while True:
        type=input("- ")
        if len(type)==0 or len(type)<=5:
            if type!="suv" and type!="SUV":
                #attempt to find out the type from the offer description
                if "coupe" in desc.lower():
                    type="Coupe"
                elif "sedan" in desc.lower():
                    type="Sedan"
                elif "sports" in desc.lower():
                    type="Sports car"
                elif "hatchback" in desc.lower():
                    type="Hatchback"
                elif "station wagon" in desc.lower():
                    type="Station wagon"
                print(f"The system couldn't recognise the type you entered, so we attempted to determine it automatically\nThe type was determined as: '{type}'")
                print("If that is correct select '1' to proceed or try to set it again by selecting '2'.\n")
                option=input()
                if option=="1":
                    break
                else:
                    continue
            else:
                type="SUV"
                break
        else:
            break
    print("What type of fuel is this car using?(Gas,Gasoline,Diesel,Electric...)?\n")
    while True:
        fType=input("- ")
        if len(fType)<1 or len(fType)>10:
            print("\nInvalid fuel type. Try again.\n")
            continue
        else:
            break
    print("What type of drivetrain does the car have?(FWD,RWD,4x4...)?\n")
    while True:
        drivetrain=input("- ")
        if len(drivetrain)<3:
            print("\nInvalid drivetrain type.\n")
            continue
        else:
            break
    print("What year was this car produced in?\n")
    while True:
        year=input("- ")
        if len(year)!=4:
            print("\nInvalid year.\n")
            continue
        else:
            year=int(year)
            if year<1900:
                print("\nInvalid year. It must be between 1900-2021.\n")
                continue
            else:
                year=str(year)
                break
    currentTime=time.localtime()
    postingTime=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
    del currentTime
    print("Do you want to add any additional notes to this offer?(Enter blank field if you wish to skip that)\n")
    comments=input("- ")
    for k in range(0,len(blockedWords)):
        if blockedWords[k][0].lower() in comments.lower() or blockedWords[k][0].upper() in comments.upper():
            print("\nYour additional comment to this offer has been removed as it contains profanities.\n")
            comments=""
    #generate a random unique offer id
    queryExecutor.execute("SELECT offerId FROM offerpostings")
    existingIds=queryExecutor.fetchall()
    while True:
        tryAgain=False
        offerId=round(1+random.random()*1000000)
        for k in range(0,len(existingIds)):
            if existingIds[k][0]==offerId:
                tryAgain=True
                break
        if tryAgain==True:
            continue
        else:
            break
    queryExecutor.execute(f"INSERT INTO offerpostings(accountId,offerId,title,description,TYPE,fuelType,driveType,yearProd,datePosted,comments) VALUES({id[0]},{offerId},'{title}','{desc}','{type}','{fType}','{drivetrain}','{year}','{postingTime}','{comments}');")
    queryExecutor.execute(f"INSERT INTO myoffers VALUES({id[0]},{offerId},'{postingTime}','Listed')")
    db_connection.commit()
    print(f"\nYour offer was successfully posted!\nOffer ID: {offerId}\n")
    main()

def MyOffers(id):
    print("Offers posted by you\n\n")
    queryExecutor.execute(f"SELECT offerpostings.title,myoffers.offerId,myoffers.posted,myoffers.status FROM myoffers, offerpostings WHERE myoffers.accountId={id} AND offerpostings.accountId={id}")
    myoffers=queryExecutor.fetchall()
    print(f"You have posted {len(myoffers)} offers")
    output="Title:     |  Offer ID:     |   Posted:     |   Status:\n"
    for k in range(0,len(myoffers)):
        for j in range(0,len(myoffers[k])):
            output+=str(myoffers[k][j])+"       "
        if k!=len(myoffers)-1:
            output+="\nTitle:     |  Offer ID:     |   Posted:     |   Status:\n"
    print(output)
    print("\nProceed?")
    proceed=input("- ")
    return 0

def main():
    global loginStatus
    if loginStatus==True:
        queryExecutor.execute(f"SELECT notification FROM usernotifications WHERE accountId={id[0]}")
        notifications=queryExecutor.fetchall()
        if len(notifications)>0:
            alertStatus=f"You have {len(notifications)} new notifications!"
        else:
            alertStatus = "You have no notifications."
        currentTime=time.localtime()
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
        print(f"{greeting}, {AccountData.accName}\n\n{alertStatus}\n\n1 - Check the current car offers | 2 - Check your offers\n3 - Post a car offer | 4 - Send special request\n5 - Contact us\n6 - Account details/settings | 7 - Log off")
    else:
        print("Hello, Guest\n\n1 - Check the current car offers | 2 - Check your offers\n3 - Post a car offer | 4 - Send special request\n5 - Contact us\n6 - Log in your account | 7 - Register Account")

    while True:
        option=input("- ")
        if option=="1":
            listCurrentCarOffers()
            main()
        elif option=="2":
            if loginStatus==False:
                print("\nYou have to log in your account first.\n")
            else:
                MyOffers(id[0])
                main()
        elif option=="3":
            if loginStatus==False:
                print("\nYou need to log in your account first.\n")
            else:
                postCarOffer()
                main()
        elif option=="4":
            if loginStatus==False:
                print("\nPlease log in your accounts or create one first.\n")
                continue
        elif option=="5":
            name=""
            if loginStatus==False:
                while True:
                    sender=input("Introduce yourself: ")
                    if len(sender)<1:
                        continue
                    else:
                        name=sender
                        break
            else:
                name=AccountData.accName
            print("Title: \n")
            title=input("- ")
            if loginStatus==False:
                print("Message(Please add information about how to contact you at the end):\n")
            else:
                print("Message:\n")
            msg=input("- ")
            print("Confirm you are not a robot:\n")
            k=0
            while k<3:
                a = round(1 + random.random() * 15); b = round(1 + random.random() * 15); res = a + b
                print(f"{a}+{b}=?")
                userSol=input()
                if int(userSol)!=res:
                    print("\nFailed verification\n")
                    k+=1
                else:
                    break
            if k==3:
                print("Verification failed 3 times! Try again later.")
                main()
            else:
                queryExecutor.execute(f"INSERT INTO postbox(sentFrom,title,message,category) VALUES('{name}','{title}','{msg}','FEEDBACK/SUPPORT REQUEST');")
                db_connection.commit()
                print("Message sent! Thank you for contacting us.\n\n")
                proceed=input("Proceed?\n")
                main()
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
