import mysql.connector; import time; import hashlib; import random
global db_connection; global queryExecutor; global loginStatus
loginStatus=False; connectionFailure=False
try:
    db_connection=mysql.connector.connect(host="localhost", user="admin", password="admin", database="cardealership"); queryExecutor=db_connection.cursor()
except:
    print("[ERROR]: Database connection failed!")
    connectionFailure=True

def listCurrentCarOffers():
    def SpecificOfferChoice(sellerName,offerId,accId):
        def ProcessOrder(user,accountId,offerId):
            print("\nProcessing order...\n")
            currentTime=time.localtime()
            queryExecutor.execute(f"SELECT * FROM offerpostings WHERE offerId={offerId} AND accountId={accId}")
            offerChoice=queryExecutor.fetchone()
            queryExecutor.execute(f"INSERT INTO userorders VALUES({accountId},{offerId},'{offerChoice[2]}','{offerChoice[3]}','{offerChoice[4]}','{offerChoice[5]}','{offerChoice[6]}','{offerChoice[7]}','{offerChoice[8]}','{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}','PENDING',{offerChoice[0]},'Waiting for seller response')")
            queryExecutor.execute(f"UPDATE myoffers SET status='Ordered' WHERE accountId={accId} AND offerId={offerId}")
            queryExecutor.execute(f"INSERT INTO usernotifications VALUES({accId},'[Ordered offer]User {username[0]} has ordered a car you offer - Offer ID[{offerId}]. You can contact them to discuss more about the order.','{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}')")
            db_connection.commit()
            print("Order placed successfully! Expect to be contacted by the seller soon.")

        if loginStatus==False:
            print("You can't view any additional information about this user and their offer, unless you log in your account.")
            print("Proceed?")
            proceed=input("- ")
        else:
            while True:
                choice=input("\n[1] - Reveal seller's contact info\n[2] - View seller's rating\n[3] - Order Now\n[4] - Return\n- ")
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
                    queryExecutor.execute(f"SELECT offerId FROM myoffers where accountId={id[0]}")
                    ids=queryExecutor.fetchall(); isThisMyOwnOffer=False
                    for k in range(0,len(ids)):
                        if ids[k][0]==offerId:
                            print("\nThis is your own offer!\n")
                            isThisMyOwnOffer=True
                            break
                    if isThisMyOwnOffer==True:
                        continue
                    else:
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
    queryExecutor.execute("SELECT accounts.username, offerpostings.offerId, offerpostings.title, offerpostings.description, offerpostings.TYPE, offerpostings.fuelType, offerpostings.driveType,offerpostings.yearProd, offerpostings.offerPrice, offerpostings.datePosted FROM accounts, offerpostings WHERE accounts.id=offerpostings.accountId limit 15")
    offers=queryExecutor.fetchall()
    offer="№: / By: / Offer id: / Title: / Description:     / Type: / Fuel Type: / Drive Type: / Production Year: / Price:  / Posted:\n\n"
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
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
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
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                listCurrentCarOffers()
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
        queryExecutor.execute("SELECT email FROM accounts")
        emails=queryExecutor.fetchall(); sameEmails=False
        #does the email match another user's email
        for k in range(0,len(emails)):
            if email==emails[k][0]:
                print("\nThe entered email is already in use! Please try another one.\n")
                sameEmails=True
                break
        if sameEmails==True:
            continue
        if email=="Why" or email=="WHY" or email=="why" or email=="Why?" or email=="WHY?" or email=="why?":
            print("\n*Your e-mail is required in case any changes are performed to your account to confirm that it is you doing them.\nAlso, your e-mail can be used to get contacted by other users regards your car offers posted here.\nYour e-mail also provides a way for admin to contact your in case the need arises.*\n")
            continue
        elif len(email)<3 or not "@" in email or not "." in email:
            print("\nE-mail is not correct.\n")
            continue
        else:
            break
    currentTime=time.gmtime()
    queryExecutor.execute(f"INSERT INTO accounts(username,PASSWORD,email, dateCreated) VAlUES('{username}','{passwordCrypted}','{email}','{currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year}');")
    db_connection.commit()
    print(f"\nYour account with username '{username}' has been created! You can now log in.\n")
    proceed=input()
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
        notAllowed=False
        title=input("- ")
        for k in range(0,len(blockedWords)):
            if blockedWords[k][0].lower() in title.lower() or blockedWords[k][0].upper() in title.upper():
                print("\nThat title cannot be posted. Change your title and make sure it does not contain profanities, personal names or other sensitive data.\n")
                notAllowed=True
                break
        if notAllowed==True:
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
                else:
                    type="Unknown"
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
    print("Specify the price for your offer(Leave blank if you'd like the customer to contact you for more information):\n")
    while True:
        wrong=False
        price=input("- ")
        if len(price)>0:
            for k in range(0,len(price)):
                if price[k].isalpha()==True:
                    print("\nYou have entered incorrect price.\n")
                    wrong=True
            if float(price)==0 and wrong!=True:
                price='Contact user for price details'
            elif float(price)>999999999:
                print("\nThat price is too high. Leave blank to discuss the price with a customer.\n")
                continue
            else:
                price+="$"
                break
        else:
            price='Contact user for price details'
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
    queryExecutor.execute(f"INSERT INTO offerpostings(accountId,offerId,title,description,TYPE,fuelType,driveType,yearProd,offerPrice,datePosted,comments) VALUES({id[0]},{offerId},'{title}','{desc}','{type}','{fType}','{drivetrain}','{year}','{price}','{postingTime}','{comments}');")
    queryExecutor.execute(f"INSERT INTO myoffers VALUES({id[0]},{offerId},'{price}','{postingTime}','Listed')")
    db_connection.commit()
    print(f"\nYour offer was successfully posted!\nOffer ID: {offerId}\n")
    main()

def MyOffers(id):
    print("Offers posted by you\n\n")
    queryExecutor.execute(f"SELECT offerpostings.title,myoffers.offerId,myoffers.askPrice,myoffers.posted,myoffers.status FROM myoffers, offerpostings WHERE myoffers.accountId={id} AND offerpostings.accountId={id}")
    myoffers=queryExecutor.fetchall()
    print(f"You have posted {len(myoffers)} offers")
    output="Title:           |  Offer ID:     |     Price:     |   Posted:        |   Status:\n"
    for k in range(0,len(myoffers)):
        for j in range(0,len(myoffers[k])):
            output+=str(myoffers[k][j])+"       "
        if k!=len(myoffers)-1:
            output+="\nTitle:     |  Offer ID:     |     Price:     |   Posted:     |   Status:\n"
    print(output)
    print("\nProceed?")
    proceed=input("- ")
    return 0

def mailbox():
    def SendMessage():
        while True:
            match=False
            recipient=input("Recipient: ")
            queryExecutor.execute("SELECT username FROM accounts")
            usersList=queryExecutor.fetchall()
            for k in range(0,len(usersList)):
                if recipient==usersList[k][0]:
                    match=True
                    break
            if match==False:
                print("\nNo user found with this name.\n")
                continue
            else:
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{recipient}'")
                recipientId=queryExecutor.fetchone()
                break
        while True:
            msg=input("Enter message: ")
            if len(msg)<3:
                print("\nMessage is too short to start a conversation.\n")
                continue
            else:
                break
        queryExecutor.execute("SELECT conversation FROM mailsystem")
        convList=queryExecutor.fetchall()
        while True:
            genAgain=False
            convNum=round(1+random.random()*1000000)
            for k in range(0,len(convList)):
                if convNum==convList[k][0]:
                    genAgain=True
                    break
            if genAgain==True:
                continue
            break
        currentTime=time.localtime(); t=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
        queryExecutor.execute(f"INSERT INTO mailsystem VALUES({id[0]},{convNum},0,'{username[0]}','{msg}','{recipient}','{t}',{round(time.time())})")
        queryExecutor.execute(f"INSERT INTO mailsystem VALUES({recipientId[0]},{convNum},0,'{username[0]}','{msg}','{recipient}','{t}',{round(time.time())})")
        queryExecutor.execute(f"INSERT INTO usernotifications VALUES({recipientId[0]},'{username[0]} messaged you.','{t}')")
        db_connection.commit()
        print("\nMessage sent!\n")
        proceed=input()

    print("\n---Your mailbox---")
    queryExecutor.execute(f"SELECT * FROM mailsystem WHERE (sender='{username[0]}' and msgN=0) and accountId={id[0]}")
    sentMessages=queryExecutor.fetchall()
    queryExecutor.execute(f"SELECT * FROM mailsystem WHERE (receiver='{username[0]}' and msgN=0) and accountId={id[0]}")
    receivedMessages=queryExecutor.fetchall()
    if len(sentMessages)==0:
        print("\nNo sent messages\n")
    else:
        messages=""
        print("\nStarted by you:\n")
        for k in range(0,len(sentMessages)):
            messages+=f"{k+1} ||| (To: {sentMessages[k][5]}): {sentMessages[k][4]} [Started: {sentMessages[k][6]}]\n"
        print(messages)
    print("-----------------------------------------------------------")
    if len(receivedMessages)==0:
        print("\nNo received messages\n")
    else:
        messages=""
        print("\nReceived:\n")
        for k in range(0,len(receivedMessages)):
            messages+=f"{k+1} ||| (From: {receivedMessages[k][3]}): {receivedMessages[k][4]} [Started: {receivedMessages[k][6]}]\n"
        print(messages)
    print("\n\n[1] Send a message   |   [2] Select a message   |   [3]Delete a conversation   |   [4] Return\n")
    deleted = False; returnBack = False; goBackToMain=False
    while True:
        if deleted == True or returnBack == True:
            break
        option=input("- ")
        if option=="1":
            SendMessage()
            break
        elif option=="2":
            while True:
                if deleted == True or returnBack == True:
                    break
                which=input("Received or Sent?: ")
                if not "Received" in which and not "received" in which and not "Sent" in which and not "sent" in which:
                    continue
                else:
                    if "Sent" in which or "sent" in which:
                        if len(sentMessages)>0:
                            while True:
                                try:
                                    n=int(input("Which message?: "))
                                    if n-1<len(sentMessages):
                                        break
                                    else:
                                        print("\nNo conversation found.\n")
                                        continue
                                except ValueError:
                                    print("\nCouldn't find a conversation with the given number. Check your mailbox again.\n")
                                    continue
                            while True:
                                if deleted == True or returnBack == True:
                                    break
                                conversation=sentMessages[n-1][1]
                                queryExecutor.execute(f"SELECT * FROM mailsystem WHERE conversation={conversation} and accountId={id[0]} ORDER BY sortTime ASC")
                                allMessages=queryExecutor.fetchall()
                                queryExecutor.execute(f"SELECT MAX(msgN) FROM mailsystem WHERE conversation={conversation}")
                                lastMsgN=queryExecutor.fetchone()
                                dialogue=""
                                for k in range(0,len(allMessages)):
                                    if username[0] != allMessages[k][3]:
                                        dialogue += f"                                          Sent by: {allMessages[k][3]} [{allMessages[k][6]}]:\n                                          --{allMessages[k][4]}\n\n"
                                    else:
                                        dialogue += f"\nSent by: {allMessages[k][3]} [{allMessages[k][6]}]:\n--{allMessages[k][4]}\n\n"
                                print(dialogue)
                                print("\n[1]Reply   |   [2]Delete conversation   |   [3]Return\n")
                                while True:
                                    option2 = input("- ")
                                    if option2 != "1" and option2 != "2" and option2 != "3":
                                        continue
                                    else:
                                        if option2 == "1":
                                            print("Enter a message:\n")
                                            msg = input("- ")
                                            queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{sentMessages[n-1][5]}'")
                                            recipientId=queryExecutor.fetchone()
                                            currentTime=time.localtime(); t=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                                            try:
                                                queryExecutor.execute(f"INSERT INTO mailsystem VALUES({recipientId[0]},{conversation},{lastMsgN[0] + 1},'{username[0]}','{msg}','{sentMessages[n - 1][5]}','{t}',{round(time.time())})")
                                                queryExecutor.execute(f"INSERT INTO mailsystem VALUES({id[0]},{conversation},{lastMsgN[0]+1},'{username[0]}','{msg}','{sentMessages[n-1][5]}','{t}',{round(time.time())})")
                                                queryExecutor.execute(f"INSERT INTO usernotifications VALUES({recipientId[0]},'{username[0]} replied to your message.','{t}')")
                                            except TypeError:
                                                print("\nCannot reply. User does not exist anymore.\n")
                                                break
                                            db_connection.commit()
                                            break
                                        elif option2 == "2":
                                            print("\nDo you really wish to delete that conversation? [Y/N]\n")
                                            yesorno = input("- ")
                                            if yesorno == "Y":
                                                print("\nDeleting conversation. . .\n")
                                                queryExecutor.execute(f"DELETE FROM mailsystem WHERE conversation={conversation} and accountId={id[0]}")
                                                db_connection.commit()
                                                deleted=True
                                                break
                                            else:
                                                continue
                                        elif option2 == "3":
                                            returnBack=True
                                        break
                        else:
                            print("\nYou have no started conversations.\n")

                    elif "Received" in which or "received" in which:
                        if len(receivedMessages)>0:
                            while True:
                                try:
                                    n=int(input("Which message?: "))
                                    if n-1<len(receivedMessages):
                                        break
                                    else:
                                        print("\nNo conversation found.\n")
                                        continue
                                except ValueError:
                                    print("\nCouldn't find a conversation with the given number. Check your mailbox again.\n")
                                    continue
                            print("\n\n")
                            while True:
                                if deleted==True or returnBack==True:
                                    break
                                conversation=receivedMessages[n-1][1]
                                queryExecutor.execute(f"SELECT MAX(msgN) FROM mailsystem WHERE conversation={conversation}")
                                lastMsgN=queryExecutor.fetchone()
                                queryExecutor.execute(f"SELECT * FROM mailsystem WHERE conversation={conversation} and accountId={id[0]} ORDER BY sortTime ASC")
                                allMessages=queryExecutor.fetchall()
                                dialogue=""
                                for k in range(0,len(allMessages)):
                                    if allMessages[k][3]!=f"{username[0]}":
                                        dialogue += f"                                          Sent by: {allMessages[k][3]} [{allMessages[k][6]}]:\n                                          --{allMessages[k][4]}\n\n"
                                    else:
                                        dialogue+=f"Sent by: {allMessages[k][3]} [{allMessages[k][6]}]:\n--{allMessages[k][4]}\n\n"
                                print(dialogue)
                                print("\n\n[1]Reply   |   [2]Delete conversation   |   [3]Return\n")
                                while True:
                                    option2=input("- ")
                                    if option2!="1" and option2!="2" and option2!="3":
                                        continue
                                    else:
                                        if option2=="1":
                                            print("Enter a message:\n")
                                            msg=input("- ")
                                            queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{receivedMessages[n - 1][3]}'")
                                            recipientId = queryExecutor.fetchone()
                                            currentTime=time.localtime(); t=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                                            try:
                                                queryExecutor.execute(f"INSERT INTO mailsystem VALUES({recipientId[0]},{conversation},{lastMsgN[0] + 1},'{username[0]}','{msg}','{receivedMessages[n - 1][3]}','{t}',{round(time.time())})")
                                                queryExecutor.execute(f"INSERT INTO mailsystem VALUES({id[0]},{conversation},{lastMsgN[0]+1},'{username[0]}','{msg}','{receivedMessages[n-1][3]}','{t}',{round(time.time())})")
                                                queryExecutor.execute(f"INSERT INTO usernotifications VALUES({recipientId[0]},'{username[0]} replied to your message.','{t}')")
                                            except TypeError:
                                                print("\nCannot reply. User does not exist anymore.\n")
                                                break
                                            db_connection.commit()
                                            break
                                        elif option2=="2":
                                            print("\nDo you really wish to delete that conversation? [Y/N]\n")
                                            yesorno=input("- ")
                                            if yesorno=="Y":
                                                print("\nDeleting conversation. . .\n")
                                                queryExecutor.execute(f"DELETE FROM mailsystem WHERE conversation={conversation} and accountId={id[0]}")
                                                db_connection.commit()
                                                deleted=True
                                                break
                                            else:
                                                continue
                                        elif option2=="3":
                                            returnBack=True
                                        break
                            else:
                                print("\nYou have no received messages.\n")
        elif option=="3":
            while True:
                if deleted==True or returnBack==True:
                    break
                which=input("Sent or received? - ")
                if not "Sent" in which and "sent" in which and "Received" in which or "received" in which:
                    continue
                else:
                    if "Sent" in which or "sent" in which:
                        while True:
                            try:
                                n=int(input("Which conversation you'd like to delete? - "))
                            except:
                                print("\nNo conversation found with the given number.\n")
                                continue
                            if n-1<len(sentMessages):
                                conversation=sentMessages[n-1][1]
                                queryExecutor.execute(f"DELETE FROM mailsystem WHERE conversation={conversation} and accountId={id[0]}")
                                db_connection.commit()
                                print("\nConversation deleted!\n")
                                deleted=True
                                break
                            else:
                                print("\nNo conversation found.\n")
                                continue
                    elif "Received" in which or "received" in which:
                        while True:
                            try:
                                n=int(input("Which conversation you'd like to delete? - "))
                            except ValueError:
                                print("\nNo conversation found with the given number.\n")
                                continue
                            if n-1<len(receivedMessages):
                                conversation=receivedMessages[n-1][1]
                                queryExecutor.execute(f"DELETE FROM mailsystem WHERE conversation={conversation} and accountId={id[0]}")
                                db_connection.commit()
                                print("\nConversation deleted!\n")
                                deleted=True
                                break
                            else:
                                print("\nNo conversation found.\n")
                                continue
        elif option=="4":
            goBackToMain=True
            break
    if goBackToMain==True:
        main()
    else:
        mailbox()

def AccountSettings():
    #print("[1] - Update your profile information | [2] - Change your password\n[3] - Delete your account\n")
    failedToVerify=False; times=0; returnBack=False
    while True:
        print("[1] - Update your profile information | [2] - Change your password\n[3] - Delete your account\n")
        if returnBack == True:
            break
        if failedToVerify==True:
            break
        option=input("- ")
        if option=="1":
            while True:
                if returnBack == True:
                    break
                if times==3:
                    print("\nPassword verification failed!\n")
                    failedToVerify=True
                    break
                passw=input("Please enter your password to access sensitive data: ")
                if len(passw)==0:
                    print("\nPlease enter your password to verify your access to sensitive data.\n")
                    continue
                passw=passw.encode(); passw=hashlib.sha256(passw); passw=passw.hexdigest()
                queryExecutor.execute(f"SELECT password FROM accounts WHERE id={id[0]}")
                currPass=queryExecutor.fetchone()
                if currPass[0]!=passw:
                    print("\nIncorrect Password\n")
                    times+=1
                    continue
                else:
                    returnBack=False
                    while True:
                        if returnBack==True:
                            break
                        print("-----Profile data-----\n")
                        queryExecutor.execute(f"SELECT * FROM accounts WHERE id={id[0]}")
                        accountData=queryExecutor.fetchone()
                        print(f"This account was created: {accountData[4]}\n\nUsername: {username[0]}\n\nE-mail: {accountData[3]}\n\nAccount rating(Based on user rates): {accountData[5]}\n\nAddress: {accountData[6]}\n\nPhone number: {accountData[7]}\n\nCompany:{accountData[8]}\n[1]Change your username  |  [2]Change your contact information\n")
                        alreadyRequested=False
                        while True:
                            failedToVerify = False
                            option2 = input("- ")
                            if option2=="1":
                                queryExecutor.execute("SELECT accountId FROM namechanges")
                                requests=queryExecutor.fetchall()
                                for k in range(0,len(requests)):
                                    if id[0]==requests[k][0]:
                                        print("\nYou have already requested a username change that is awaiting approval.\n")
                                        alreadyRequested=True
                                        break
                                if alreadyRequested==True:
                                    break
                                while True:
                                    newName=input("Enter your new username? - ")
                                    if len(newName)<2:
                                        print("\nYour username should be longer than 2 symbols\n")
                                        continue
                                    elif len(newName)>20:
                                        print("\nYour username should be shorter than 20 symbols\n")
                                        continue
                                    else:
                                        break
                                copyTxt=""; showCopy=False
                                while True:
                                    if showCopy==True:
                                        showCopy==False; print(copyTxt)
                                    reason=input("Why do you want to change your username(This is done to prevent fraud or other types of misuse)? \n(200 symbols max.)\n- ")
                                    if len(reason)==0:
                                        print("\nPlease enter a short explanation about why do you want to change your username.\n")
                                        continue
                                    elif len(reason)>200:
                                        print("\nYour text is exceeding 200 symbols. Please shorten your text before sending.\n")
                                        showCopy=True; copyTxt=reason
                                        continue
                                    else:
                                        queryExecutor.execute(f"INSERT INTO namechanges({id[0]},'{username[0]}','{newName}','{reason}')")
                                        db_connection.commit()
                                        print("Thank you for contacting us!\nYour username change request has been sent! Expect response in 24-48 hours.")
                                        proceed=input()
                                        break
                                break
                            elif option2=="2":
                                while True:
                                    print("\nChoose what do you want to update/set:\n[1]Address,[2]Phone number,[3]Email,[4]Company")
                                    change=input()
                                    if change=="1":
                                        queryExecutor.execute(f"SELECT address FROM accounts WHERE id={id[0]}")
                                        currAddr=queryExecutor.fetchone()
                                        if currAddr[0]!="Not stated":
                                            print(f"\nYour current address is: {currAddr[0]}\n")
                                        while True:
                                            newAddr=input("Set your new address: ")
                                            if len(newAddr)<2 or len(newAddr)>100:
                                                print("\nInvalid address\n")
                                                continue
                                            elif newAddr=="None" or newAddr=="":
                                                print("Your address has been removed.")
                                                if newAddr!="Not stated":
                                                    queryExecutor.execute(f"UPDATE accounts SET address='Not stated' WHERE id={id[0]}")
                                                    db_connection.commit()
                                            else:
                                                queryExecutor.execute(f"UPDATE accounts SET address='{newAddr}' WHERE id={id[0]}")
                                                db_connection.commit()
                                                print("\nYour address has been updated\n")
                                                proceed=input()
                                                break
                                    elif change=="2":
                                        queryExecutor.execute(f"SELECT telephone FROM accounts WHERE id={id[0]}")
                                        currTel=queryExecutor.fetchone()
                                        if currTel[0]!="Not stated":
                                            print(f"Your current phone number is: {currTel[0]}")
                                        while True:
                                            newTel=input("Set your new phone number: ")
                                            if not len(newTel)==10:
                                                print("\nThe given phone number is invalid.\n")
                                            elif newTel=="None" or newTel=="":
                                                print("Your phone number has been removed.")
                                                if newTel!="Not stated":
                                                    queryExecutor.execute(f"UPDATE accounts SET telephone='Not stated' WHERE id={id[0]}")
                                                    db_connection.commit()
                                            else:
                                                queryExecutor.execute(f"UPDATE accounts SET telephone='{newTel}' WHERE id={id[0]}")
                                                db_connection.commit()
                                                print("\nYour phone number has been changed.\n")
                                                break
                                    elif change=="3":
                                        queryExecutor.execute(f"SELECT email FROM accounts WHERE id={id[0]}")
                                        currEmail=queryExecutor.fetchone()
                                        print(f"\nYour current email is: {currEmail[0]}\n")
                                        while True:
                                            newEmail=input("Set your new email: ")
                                            if not "@" in newEmail or not "." in newEmail or len(newEmail)>60 or len(newEmail)==0:
                                                print("\nInvalid email\n")
                                                continue
                                            else:
                                                queryExecutor.execute(f"UPDATE accounts SET email='{newEmail}' WHERE id={id[0]}")
                                                db_connection.commit()
                                                print("Your email has been changed.")
                                    elif change=="4":
                                        queryExecutor.execute(f"SELECT company FROM accounts WHERE id={id[0]}")
                                        currComp=queryExecutor.fetchone()
                                        if currComp!="None":
                                            print(f"Your current set company name is: {currComp[0]}")
                                        while True:
                                            newComp=input("Update the name of your company: ")
                                            if len(newComp)>30:
                                                print("\nEnter a valid company name\n")
                                            elif newComp=="None" or newComp=="":
                                                print("Your company name has been removed.")
                                                if currComp!="Not stated":
                                                    queryExecutor.execute(f"UPDATE accounts SET company='Not stated' WHERE id={id[0]}")
                                                    db_connection.commit()
                                            else:
                                                queryExecutor.execute(f"UPDATE accounts SET company='{newComp}' WHERE id={id[0]}")
                                                db_connection.commit()
                                                print("\nYour company name has been updated\n")
                                                break
                                    elif change=="Return" or change=="return":
                                        break
                                break
                            elif option2=="Return" or option2=="return":
                                returnBack=True
                                break
        elif option=="2":
            times=0
            while True:
                success = False
                if times==3:
                    print("\nYou have failed to verify your access. Please try again later.\n")
                    break
                passw=input("Enter your current password to verify your access to account data: ")
                passw=passw.encode(); passw=hashlib.sha256(passw); passw=passw.hexdigest()
                queryExecutor.execute(f"SELECT password FROM accounts WHERE id={id[0]}")
                currPass=queryExecutor.fetchone()
                if passw!=currPass[0]:
                    print("\nIncorrect password\n")
                    times+=1
                    del currPass
                    continue
                else:
                    del currPass
                    while True:
                        newPass=input("Enter your new password: ")
                        if len(newPass)<4:
                            print("\nYour password is too short. It must be at least 4 symbols long.\n")
                            continue
                        else:
                            times=0
                            while True:
                                if times==3:
                                    print("\nTry setting your new password again\n")
                                    break
                                confirm=input("Confirm your new password: ")
                                if confirm!=newPass:
                                    print("\nPasswords do not match! Try again.\n")
                                    times+=1
                                    continue
                                else:
                                    newPass=newPass.encode(); newPass=hashlib.sha256(newPass); newPass=newPass.hexdigest()
                                    queryExecutor.execute(f"UPDATE accounts set password='{newPass}' WHERE id={id[0]}")
                                    db_connection.commit()
                                    print("\nYour password has been changed!\n")
                                    success=True
                                    break
                            if success==True or failedToVerify==True:
                                break
                    if success == True or failedToVerify==True:
                        break
        elif option=="3":
            times=0; deletedAccount=False
            while True:
                if times==3:
                    print("\nVerification failed. Try again later!\n")
                    returnBack=True
                    break
                passw=input("Enter your password to confirm it is you taking that action: ")
                queryExecutor.execute(f"SELECT password FROM accounts WHERE id={id[0]} ")
                currPass=queryExecutor.fetchone()
                passw=passw.encode(); passw=hashlib.sha256(passw); passw=passw.hexdigest()
                if passw!=currPass[0]:
                    times+=1
                    print("\nIncorrect password\n")
                    continue
                else:
                    print("\n---Please Read!---\nIf proceed deleting your account, all data associated with it will be removed, that includes - All personal information, all offers posted by you, your orders and opened support tickets.\nIf you'd like to delete your account permanently, please enter the following below - 'I wish to delete my account'. If you have changed your mind enter - 'Return'.")
                    while True:
                        confirmation=input("- ")
                        if confirmation=="I wish to delete my account":
                            print("\nYour account and all associated data with it has been deleted.\n")
                            proceed=input()
                            deletedAccount=True
                            break
                        elif confirmation=="Return" or confirmation=="return":
                            break
                        else:
                            print("\nCannot understand that. Try again.\n")
                            continue
                    if deletedAccount==True:
                        main(True)
                    else:
                        break
        elif option=="Return" or option=="return":
            main()
        else:
            continue
    AccountSettings()

def main(deletedAccount=False):
    global loginStatus
    if connectionFailure==True:
        return -1
    if loginStatus==True:
        if deletedAccount == True:
            queryExecutor.execute(f"DELETE FROM accounts WHERE id={id[0]}")
            queryExecutor.execute(f"DELETE FROM myoffers WHERE accountId={id[0]}")
            queryExecutor.execute(f"DELETE FROM mailsystem WHERE accountId={id[0]}")
            queryExecutor.execute(f"DELETE FROM namechanges WHERE accountId={id[0]}")
            queryExecutor.execute(f"DELETE FROM offerpostings WHERE accountId={id[0]}")
            queryExecutor.execute(f"DELETE FROM postbox WHERE sentFrom='{username[0]}'")
            queryExecutor.execute(f"DELETE FROM usernotifications WHERE accountId={id[0]}")
            queryExecutor.execute(f"DELETE FROM userorders WHERE accountId={id[0]}")
            db_connection.commit()
            loginStatus = False
            main()
        class AccountData:
            accName=username[0]; accId=id[0]
        queryExecutor.execute(f"SELECT * FROM usernotifications WHERE accountId={id[0]}")
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
    else:
        greeting="Hello"
    print("       Ed's Car Dealership\n")
    if loginStatus==True:
        print(f"{greeting}, {AccountData.accName}\n\n{alertStatus}\n\n1 - Check the current car offers | 2 - Check your offers\n3 - Post a car offer | 4 - Send special request\n5 - Contact us\n6 - Account details/settings | 7 - Check your notifications\n8 - Go to your mailbox | 9 - Log Off")
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
            else:
                title=f"Requested By: {username[0]}"
                msg=""
                while True:
                    brand=input("Specify the brand of the car you'd like to request: ")
                    if len(brand)<1:
                        print("\nPlease enter a brand name of the car you'd like to request.\n")
                        continue
                    elif brand=="Return" or brand=="return":
                        break
                    else:
                        msg+=f"[REQUEST DETAILS] Brand: {brand}  | "
                        break
                if brand=="Return" or brand=="return":
                    del msg
                    main()
                else:
                    while True:
                        model=input("Specify the model: ")
                        if len(model)<1:
                            print("\nPlease specify the model of the car you'd like to request.\n")
                            continue
                        else:
                            msg+=f"Model: {model}  | "
                            break
                    while True:
                        prodYear=input("Specify production year: ")
                        if len(prodYear)<1:
                            print("\nPlease specify the production year of the car you'd like to request.\n")
                            continue
                        else:
                            msg+=f"Production Year: {prodYear}  | "
                            break
                    while True:
                        fType=input("Specify fuel type: ")
                        if len(fType)<1:
                            print("\nPlease specify the fuel type of the car you'd like to request.\n")
                            continue
                        else:
                            msg+=f"Fuel Type: {fType}  | "
                            break
                    while True:
                        addNotes=input("Would you like to add any additional notes to this request?(If you wish to skip that, leave blank): ")
                        if len(addNotes)==0:
                            msg+=f"Additional Comments/Notes: *None*  | "
                            break
                        else:
                            msg += f"Additional Comments/Notes: {addNotes}  | "
                            break
                    currentTime=time.localtime()
                    timeTxt=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                    msg+=f"Sent: {timeTxt}"
                    queryExecutor.execute(f"INSERT INTO postbox VALUES('{username[0]}','{title}','{msg}','SPECIAL REQUEST')")
                    db_connection.commit()
            print("\nYour request has been sent! You will be contacted as soon as possible.\n")
            proceed=input()
            main()
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
                AccountSettings()
        elif option=="7":
            if loginStatus==False:
                RegisterAccount()
                main()
            else:
                print("\n\n--Notifications--\n")
                receiveNotifications=""
                if len(notifications)>0:
                    for k in range(0,len(notifications)):
                        for j in range(len(notifications[k])-1,0,-1):
                            receiveNotifications+=notifications[k][j]+"   "
                        receiveNotifications+="\n"
                else:
                    print("\nYou have no notifications to show.\n")
                    proceed=input()
                    main()
                queryExecutor.execute(f"DELETE FROM usernotifications WHERE accountId={id[0]}")
                db_connection.commit()
                print(receiveNotifications)
                proceed=input()
                main()
        elif option=="8":
            if loginStatus==True:
                mailbox()
        elif option=="9":
            if loginStatus==True:
                del AccountData
                loginStatus=False
                main()
            else:
                main()
        else:
            continue
main()
