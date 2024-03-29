import mysql.connector; import time; import hashlib; import random; import re
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
            queryExecutor.execute("SELECT orderId FROM userorders")
            currentOrders=queryExecutor.fetchall()

            while True:
                repeat=False
                uniqueId=round(1+random.random()*10000001)
                for k in range(0,len(currentOrders)):
                    if uniqueId==currentOrders[k][0]:
                        repeat=True
                        break
                if repeat==True:
                    continue
                break
            queryExecutor.execute(f"SELECT * FROM offerpostings WHERE offerId={offerId} AND accountId={accId}")
            offerChoice=queryExecutor.fetchone()
            queryExecutor.execute(f"SELECT username FROM accounts WHERE id={offerChoice[0]}")
            sellerName=queryExecutor.fetchone()
            queryExecutor.execute(f"INSERT INTO userorders VALUES({uniqueId},{accountId},{offerId},'{offerChoice[2]}','{offerChoice[3]}','{offerChoice[4]}','{offerChoice[5]}','{offerChoice[6]}','{offerChoice[7]}','{offerChoice[8]}','{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}','PENDING','{sellerName[0]}','Waiting for seller response','')")
            queryExecutor.execute(f"UPDATE myoffers SET status='Ordered' WHERE accountId={accId} AND offerId={offerId}")
            queryExecutor.execute(f"INSERT INTO usernotifications VALUES({accId},'[Ordered offer]User {username[0]} has ordered a car you offer - Offer ID[{offerId}]. You can contact them to discuss more about the order.','{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}')")
            db_connection.commit()
            print("Order placed successfully! Expect to be contacted by the seller soon.")

        if loginStatus==False:
            print("You can't view any additional information about this user and their offer, unless you log in your account.")
            proceed=input("- ")
        else:
            noContactsAvailable=False
            while True:
                if noContactsAvailable==False:
                    choice=input("\n[1] - Reveal seller's contact info\n[2] - View seller's rating\n[3] - Order Now\n[4] - Return\n- ")
                else:
                    choice = input("\n[1] - Reveal seller's contact info\n[2] - View seller's rating\n[3] - Order Now\n[4] - Return\n[5]Contact through our platform\n- ")
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
                        queryExecutor.execute(f"SELECT address FROM accounts where username='{sellerName}'")
                        address=queryExecutor.fetchone()
                        queryExecutor.execute(f"SELECT telephone FROM accounts where username='{sellerName}'")
                        phone=queryExecutor.fetchone()
                        queryExecutor.execute(f"SELECT company FROM accounts where username='{sellerName}'")
                        company=queryExecutor.fetchone()
                        print(f"Contact information for seller:\n")
                        queryExecutor.execute(f"SELECT accountFlags FROM accounts WHERE username='{sellerName}'")
                        sellerPrivacySettings=queryExecutor.fetchone()
                        if not "[HideCompany]" in sellerPrivacySettings[0]:
                            if company[0]!="None":
                                print(f"Company: {company[0]}")
                        else:
                            print(f"{sellerName} has preferred not show company name publicly.")
                        if not "[HideEmail]" in sellerPrivacySettings[0]:
                            print(f"E-mail: {email[0]}")
                        else:
                            print(f"{sellerName} has preferred not to show their email publicly.")
                        if not "[HidePhone]" in sellerPrivacySettings[0]:
                            if phone[0]!="Not stated":
                                print(f"Phone: {phone[0]}")
                        else:
                            print(f"{sellerName} has preferred not to show their phone number publicly.")
                        if not "[HideAddress]" in sellerPrivacySettings[0]:
                            if address[0]!="Not stated":
                                print(f"Address: {address}")
                                proceed=input(" - ")
                        else:
                            print(f"{sellerName} has preferred not to show their address publicly.")
                        if "[HideEmail]" in sellerPrivacySettings[0] and "[HidePhone]" in sellerPrivacySettings[0] and "[HideAddress]" in sellerPrivacySettings[0] and "[HideCompany]" in sellerPrivacySettings[0]:
                            noContactsAvailable=True
                elif choice=="2":
                    queryExecutor.execute(f"SELECT rating, ratedBy FROM accounts WHERE username='{sellerName}'")
                    rating=queryExecutor.fetchone()
                    try:
                        avg=rating[0]/rating[1]
                    except:
                        avg="0.00"
                    print(f"\n{sellerName}'s current rating: {avg}\n")
                    proceed=input()
                    continue
                elif choice=="3":
                    queryExecutor.execute(f"SELECT offerId FROM myoffers where accountId={id[0]}")
                    ids=queryExecutor.fetchall(); isThisMyOwnOffer=False; isItAlreadyOrdered=False
                    queryExecutor.execute(f"SELECT offerId FROM userOrders")
                    orders=queryExecutor.fetchall()
                    for k in range(0,len(ids)):
                        if ids[k][0]==offerId:
                            print("\nThis is your own offer!\n")
                            proceed=input()
                            isThisMyOwnOffer=True
                            break
                    for k in range(0,len(orders)):
                        if orders[k][0]==offerId:
                            print("\nThis offer is currently ordered by someone else. You can try again later or contact the seller.\n")
                            isItAlreadyOrdered=True
                            proceed=input()
                    if isThisMyOwnOffer==True:
                        continue
                    elif isItAlreadyOrdered==True:
                        continue
                    else:
                        print("Are you sure you wish to order that car?[Y]/[N]\n")
                        yesOrNo=input("- ")
                        if yesOrNo=="Y" or yesOrNo=="y":
                            ProcessOrder(username[0],id[0],offerId)
                        else:
                            continue
                elif choice=="4":
                    return 0
                elif choice=="5":
                    if noContactsAvailable==True:
                        mailbox(True,sellerName)

    currentTime=time.localtime()
    print(f"\n\n---------LIST OF CURRENT CAR OFFERS POSTED HERE({currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min})---------")
    queryExecutor.execute("SELECT accounts.username, offerpostings.offerId, offerpostings.title, offerpostings.description, offerpostings.TYPE, offerpostings.fuelType, offerpostings.driveType,offerpostings.yearProd, offerpostings.offerPrice, offerpostings.datePosted, offerpostings.comments FROM accounts, offerpostings WHERE accounts.id=offerpostings.accountId and not offerpostings.specialflags=\"[THISOFFERISCURRENTLYDELISTED]\" limit 15")
    offers=queryExecutor.fetchall()
    offer="№: / By: / Offer id: / Title: / Description:     / Type: / Fuel Type: / Drive Type: / Production Year: / Price:  / Posted:       /   Additional notes:\n\n"
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
            viewedOffer = False
            usrChoice=input("- ")
            if usrChoice=="return" or usrChoice=="Return" or usrChoice=="RETURN":
                return 0
            elif usrChoice=="1" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice)-1][0]}'")
                accId=queryExecutor.fetchone(); offerId=offers[int(usrChoice)-1][1]
                SpecificOfferChoice(offersList[int(usrChoice)-1][0],offerId,accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="2" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone()
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="3" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="4" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:\n\n"
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="5" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="6" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="7" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="8" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="9" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="10" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="11" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="12" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="13" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone();
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="14" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone()
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            elif usrChoice=="15" and not int(usrChoice)>len(offersList):
                offerOutput = "\n  Seller:    Offer id:    Brand/Model/General info:    Description:    Type:    Fuel Type:    Drive Type:    Production Year:    Price:\n\n"
                for k in range(0, len(offersList[int(usrChoice) - 1])):
                    offerOutput += "  " + str(offersList[int(usrChoice) - 1][k]) + "  /  "
                    j += 1
                print(offerOutput)
                queryExecutor.execute(f"SELECT id FROM accounts WHERE username='{offers[int(usrChoice) - 1][0]}'")
                accId = queryExecutor.fetchone()
                offerId = offers[int(usrChoice) - 1][1]
                SpecificOfferChoice(offersList[int(usrChoice) - 1][0], offerId, accId[0])
                del offerOutput
                viewedOffer = True
                break
            else:
                print("\nInvalid choice.\n")
                continue
    else:
        print("No offers currently found. 'Return' to continue to the menu.")
        usrChoice=input()
        main()
    if viewedOffer == True:
        listCurrentCarOffers()

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
    queryExecutor.execute(f"INSERT INTO accounts(username,PASSWORD,email, dateCreated, ratedUsers) VAlUES('{username}','{passwordCrypted}','{email}','{currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year}','');")
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
        elif title=="Return" or title=="return":
            return 0
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
    queryExecutor.execute(f"INSERT INTO myoffers(accountId,offerId,askPrice,posted,status) VALUES({id[0]},{offerId},'{price}','{postingTime}','Listed')")
    db_connection.commit()
    print(f"\nYour offer was successfully posted!\nOffer ID: {offerId}\n")
    proceed=input()
    return 0

def MyOffers(id):
    print("Offers posted by you\n\n")
    queryExecutor.execute(f"SELECT offerpostings.title,myoffers.offerId,myoffers.askPrice,myoffers.posted,myoffers.status FROM myoffers, offerpostings WHERE myoffers.accountId={id} AND offerpostings.accountId={id}")
    myoffers=queryExecutor.fetchall()
    print(f"You have posted {len(myoffers)} offers")
    output="№:           |      Title:           |  Offer ID:     |     Price:     |   Posted:        |   Status:\n"
    for k in range(0,len(myoffers)):
        output+=f"{k+1}           "
        for j in range(0,len(myoffers[k])):
            output+=str(myoffers[k][j])+"       "
        if k!=len(myoffers)-1:
            output+="\n№:           |      Title:           |  Offer ID:     |     Price:     |   Posted:        |   Status:\n"
    print(output)
    print("\n[1]I wish to manage my offers   |   [2]Return\n")
    getBack=False
    while True:
        if getBack == True:
            break
        option=input("- ")
        if option=="1":
            while True:
                if getBack==True:
                    break
                option2=input("Choose an offer from your list by number: ")
                if option2=="Return" or option2=="return":
                    break
                elif int(option2)>len(myoffers) or int(option2)<1:
                    print("\nCouldn't find an offer with the given number.\n")
                    continue
                else:
                    print("\n")
                    n=int(option2)-1
                    output2=""
                    pickedOffer=myoffers[n]
                    for k in range(0,len(pickedOffer)):
                        output2+=str(pickedOffer[k])+"   "
                    print(output2)
                    while True:
                        if getBack == True:
                            break
                        print("\n[1]Change status of this offer  |   [2]Delete this offer   |   [3]Change offer's price   |   [4]Add additional notes   |   [5]Return\n")
                        manageOpt=input("- ")
                        if manageOpt=="1":
                            print("\nChoose status for your offer('List','Delist','Remove ordered label','Processing','Finished'):\n ")
                            statusChanged=False
                            while True:
                                if statusChanged==True:
                                    break
                                status=input("- ")
                                if status=="List" or status=="list":
                                    if pickedOffer[4]=="Listed":
                                        print("\nYour offer is already listed!\n")
                                        break
                                    currTime=time.localtime(); t=f"{currTime.tm_mday}.{currTime.tm_mon}.{currTime.tm_year} {currTime.tm_hour}:{currTime.tm_min}"
                                    queryExecutor.execute(f"UPDATE myoffers SET status='Listed' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                    queryExecutor.execute(f"UPDATE offerpostings SET specialflags='',datePosted='{t}' WHERE offerId={pickedOffer[1]}")
                                    db_connection.commit()
                                    print("\nOffer's status has been set to - 'Listed'\n")
                                    proceed=input()
                                    break
                                elif "Delist" in status or "delist" in status:
                                    if pickedOffer[4]=="Delisted":
                                        print("\nYour offer is already delisted!\n")
                                        break
                                    queryExecutor.execute(f"UPDATE myoffers SET status='Delisted' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                    queryExecutor.execute(f"UPDATE offerpostings SET specialflags='[THISOFFERISCURRENTLYDELISTED]' WHERE offerId={pickedOffer[1]}")
                                    db_connection.commit()
                                    print("\nYour offer has been removed from public list and set to - 'Delisted'. You can now delete it or repost it if you wish to do so.\n")
                                    proceed=input()
                                    break
                                elif status=="Remove ordered label" or status=="remove ordered label" or status=="Remove Ordered Label":
                                    currentTime = time.localtime();
                                    t = f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                                    queryExecutor.execute(f"SELECT orderId FROM userorders WHERE offerId={pickedOffer[1]}")
                                    orderId=queryExecutor.fetchone()
                                    queryExecutor.execute(f"SELECT accountId FROM userorders WHERE offerId={pickedOffer[1]}")
                                    buyerId=queryExecutor.fetchone()
                                    queryExecutor.execute(f"UPDATE myoffers SET status='Listed' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                    queryExecutor.execute(f"UPDATE userorders SET offerId=offerId*-1, orderstatus=\"Cancelled by seller\", ExpectedDelivery='N/A' WHERE offerId={pickedOffer[1]}")
                                    queryExecutor.execute(f"INSERT INTO usernotifications VALUES({buyerId[0]},'[Order status] Order {orderId[0]} has been cancelled by the seller.','{t}')")
                                    db_connection.commit()
                                    print("\nOrder's status is back to 'Listed' and anyone's order on this car has now been cancelled.\n")
                                    proceed=input()
                                    break
                                elif status=="Processing" or status=="processing":
                                    if pickedOffer[4]=="Ordered":
                                        print("[Format: D.M.Y]")
                                        scheme=re.compile(r"^[0-3][0-9].[0-1][0-9].[2][0][2-4][0-9]$")
                                        while True:
                                            ED=input("Please enter time of expected delivery or leave blank if you wish to discuss it with your customer: ")
                                            if not scheme.search(ED) and not ED=="":
                                                print("\nYour expected delivery date is incorrect. Try again.\n")
                                                continue
                                            else:
                                                if ED=="":
                                                    ED="N/A"
                                                break
                                        currentTime=time.localtime(); t=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                                        queryExecutor.execute(f"SELECT orderId FROM userorders WHERE offerId={pickedOffer[1]}")
                                        orderId =queryExecutor.fetchone()
                                        queryExecutor.execute(f"SELECT accountId FROM userorders WHERE offerId={pickedOffer[1]}")
                                        buyerId=queryExecutor.fetchone()
                                        queryExecutor.execute(f"UPDATE myoffers SET status='Processing' WHERE offerId={pickedOffer[1]} and accountId={id}")
                                        queryExecutor.execute(f"UPDATE userorders SET orderstatus='Processing', ExpectedDelivery=\"{ED}\" WHERE offerId={pickedOffer[1]}")
                                        queryExecutor.execute(f"UPDATE offerpostings SET specialflags='[THISOFFERISCURRENTLYDELISTED]' WHERE offerId={pickedOffer[1]}")
                                        queryExecutor.execute(f"INSERT INTO usernotifications VALUES({buyerId[0]},'[Order status] Order {orderId[0]} is in processing phase now.','{t}')")
                                        db_connection.commit()
                                        print("\nOrder's status is set to 'Processing' and customer who ordered this car is notified.\n")
                                        proceed=input()
                                        break
                                    else:
                                        print("\nCannot do that. Your offer is still not ordered by anyone.\n")
                                        break
                                elif status=="Finished" or status=="finished" or status=="FINISHED":
                                    if pickedOffer[4]=="Processing":
                                        currentTime = time.localtime(); t = f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                                        queryExecutor.execute(f"SELECT accountId FROM userorders WHERE offerId={pickedOffer[1]}")
                                        buyerId=queryExecutor.fetchone()
                                        queryExecutor.execute(f"SELECT orderId FROM userorders WHERE offerId={pickedOffer[1]} and accountId={buyerId[0]}")
                                        orderId=queryExecutor.fetchone()
                                        queryExecutor.execute(f"UPDATE myoffers SET status='Finished' WHERE offerId={pickedOffer[1]} and accountId={id}")
                                        queryExecutor.execute(f"UPDATE userorders SET orderstatus='Finished' WHERE offerId={pickedOffer[1]}")
                                        queryExecutor.execute(f"INSERT INTO usernotifications VALUES({buyerId[0]},'[Order status] Your order [{orderId[0]}] has been finished. You can now rate the seller or report a problem.','{t}')")
                                        db_connection.commit()
                                        print("\nThis car is sold\n")
                                        statusChanged=True
                                        proceed=input()
                                        continue
                                    else:
                                        print("\nThis offer is still not in processing stage. Please put into processing stage first.\n")
                                        proceed=input()
                                        continue
                                else:
                                    continue
                            continue
                        elif manageOpt=="2":
                            queryExecutor.execute(f"SELECT flags FROM myoffers WHERE offerId={pickedOffer[1]}")
                            currentFlags=queryExecutor.fetchone()
                            if "[REPORTED]" in currentFlags:
                                print("\nYou cannot delete that offer right now as it is under administrative review. If you think this is a mistake contact us.\n")
                                proceed=input(); getBack=True
                                break
                            confirm=input("Confirm you want to delete this offer[Y/N]")
                            if confirm=="Y" or confirm=="y":
                                queryExecutor.execute(f"DELETE FROM myoffers WHERE accountId={id} and offerId={pickedOffer[1]} LIMIT 1")
                                queryExecutor.execute(f"DELETE FROM offerpostings WHERE accountId={id} and offerId={pickedOffer[1]}")
                                db_connection.commit()
                                print(f"\nOffer {pickedOffer[1]} has been deleted.\n")
                                proceed=input(); getBack=True
                                break
                        elif manageOpt=="3":
                            queryExecutor.execute(f"SELECT askPrice FROM myoffers WHERE accountId={id} and offerId={pickedOffer[1]}")
                            currPrice=queryExecutor.fetchone()
                            if currPrice[0]!="Contact user for price details":
                                print(f"\nCurrent price: {currPrice[0]}\n")
                            newPrice=input("Set new price - ")
                            if newPrice=="" or newPrice.isdigit()==False:
                                queryExecutor.execute(f"UPDATE myoffers SET askPrice='Contact user for price details' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                queryExecutor.execute(f"UPDATE offerpostings SET offerPrice='Contact user for price details' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                print("\nPrice was set to 'Contact user for price details'\n")
                                proceed=input()
                            else:
                                newPrice+="$"
                                queryExecutor.execute(f"UPDATE myoffers SET askPrice='{newPrice}' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                queryExecutor.execute(f"UPDATE offerpostings SET offerPrice='{newPrice}' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                print("\nOffer's price has been updated.\n")
                                proceed=input()
                            db_connection.commit()
                        elif manageOpt=="4":
                            queryExecutor.execute("SELECT * FROM reservednames")
                            blockedWords=queryExecutor.fetchall(); profanitiesDetected=False
                            print("\nUpdate your additional information to this offer:\n")
                            copyTxt=""
                            while True:
                                if len(copyTxt)>0:
                                    print(f"\nYour tried to submit the following:\n{copyTxt}")
                                comments=input("- ")
                                for k in range(0,len(blockedWords)):
                                    if blockedWords[k][0] in comments:
                                        profanitiesDetected=True
                                        print("\nCannot add this. Your text contains profanities or other sensitive information that is not allowed.\n")
                                        proceed=input()
                                        break
                                if profanitiesDetected==False:
                                    if len(comments)>100:
                                        print("\nYour text exceeds the limitation of 100 symbols. Please edit your text.\n")
                                        copyTxt=comments
                                        continue
                                    elif len(comments)==0:
                                        print("\nYour notes to the offer have been updated\n")
                                        queryExecutor.execute(f"UPDATE offerpostings SET comments='' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                        db_connection.commit()
                                        break
                                    else:
                                        print("\nYour notes to the offer have been updated\n")
                                        queryExecutor.execute(f"UPDATE offerpostings SET comments='{comments}' WHERE accountId={id} and offerId={pickedOffer[1]}")
                                        db_connection.commit()
                                        break
                        elif manageOpt=="5":
                            getBack=True
                        continue

        elif option=="2":
            return 0
        else:
            continue
    MyOffers(id)

def CheckMyOrders(id):
    def Report(orderId,offerId,reportedUser):
        currentTime = time.localtime(); t = f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
        name=username[0]
        report=f"[REPORT TIME: {t}] [REPORT BY: {name}]  [REPORTED ORDER: {orderId}]    [REPORTED USER: {reportedUser}]"
        while True:
            title=input("Title:\n- ")
            if len(title)<4:
                print("\nTitle is too short to continue.\n")
                continue
            elif len(title)>100:
                print("\nTitle is too long. It should not exceed 100 symbols.\n")
                continue
            else:
                report+=f"Report Title:"
                break
        copyTxt=""
        while True:
            if len(copyTxt)>0:
                print("\nYour previous text:")
                print(copyTxt)
                print("\n")
            message=input("Report details(Please explain as much as possible about the problem so we can help you):\n- ")
            if len(message)>5000:
                copyTxt=message
                print("\nYour report exceeds 5000 characters. Cannot proceed sending your report, please shorten your text.\n")
                continue
            elif len(message)<15:
                print("\nYour report is too short.\n")
                continue
            else:
                report+=f"  Report details: {message}"
                queryExecutor.execute(f"UPDATE userorders SET orderFlags='[REPORTED]' WHERE orderId={orderId}")
                queryExecutor.execute(f"UPDATE myoffers SET status='Being reviewed by administrator',flags='[REPORTED]' WHERE offerId={offerId}")
                queryExecutor.execute(f"INSERT INTO postbox VALUES('{name}','{title}','{report}','REPORT')")
                db_connection.commit()
                print("\nReport has been sent. An administrator will review as soon as possible.\n")
                proceed=input()
                break
        return 0

    queryExecutor.execute(f"\nSELECT orderId,offerId,title,description,TYPE,fuelType,driveType,yearProd,posted,ordered,orderstatus,SoldBy,ExpectedDelivery,orderFlags FROM userorders WHERE accountId={id}\n")
    allOrders=queryExecutor.fetchall()
    output=""; anyFinishedOrders=False
    for k in range(0,len(allOrders)):
        if allOrders[k][10]=="Finished":
            anyFinishedOrders=True
    for k in range(0,len(allOrders)):
        output += str(k + 1)+" || "
        for j in range(0,len(allOrders[k])):
            output+=str(allOrders[k][j])+" || "
        output+="\n"
    print("\nMy current orders:\n")
    print(output)
    returnBack=False; returnToBeginning=False
    outputOptions="[1]Delete/Cancel order || [2]Return"
    if anyFinishedOrders == True:
        outputOptions += " || [3]Rate seller || [4]Report a problem with an order || [5]Delete all finished orders"
    while True:
        print(outputOptions)
        option=input("- ")
        if option=="1":
            while True:
                if len(allOrders)==0:
                    print("\nYou have no orders.\n")
                    proceed=input()
                    break
                try:
                    n=int(input("Choose order: "))
                except:
                    print("\nCannot find an order with this entry.\n")
                    continue
                if n>len(allOrders) or n<1:
                    print("\nCannot find an order with this entry.\n")
                    continue
                else:
                    pickedOrder=allOrders[n-1]
                    print("\nAre you sure you want to cancel this order?[Y/N]\n")
                    confirm=input("- ")
                    if confirm=="Y" or confirm=="y":
                        currentTime = time.localtime(); t = f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
                        queryExecutor.execute(f"DELETE FROM userorders WHERE orderId={pickedOrder[0]} and accountId={id}")
                        queryExecutor.execute(f"SELECT accountId, status FROM myoffers WHERE offerId={pickedOrder[1]}")
                        offerStatus=queryExecutor.fetchone()
                        if offerStatus[1]=="Processing" or offerStatus[1]=="Ordered":
                            queryExecutor.execute(f"INSERT INTO usernotifications VALUES({offerStatus[0]},'[Offer order]User {username[0]} has cancelled their order on offer ID {pickedOrder[1]}','{t}')")
                        queryExecutor.execute(f"UPDATE myoffers SET status='Listed' WHERE offerId={pickedOrder[1]}")
                        db_connection.commit()
                        print("\nYour order has been successfully cancelled.\n")
                        proceed=input(); returnToBeginning==True
                        break
                    else:
                        break
        elif option=="2":
            returnBack=True
            break
        elif anyFinishedOrders==True and option=="3":
            while True:
                try:
                    n=int(input("Pick one of your finished offers: "))
                    n-=1
                    if n>=len(allOrders) or n<0:
                        print("\nInvalid choice.\n")
                        continue
                    elif allOrders[n][10]!='Finished':
                        print("\nThis is not one of your finished orders\n")
                        continue
                    else:
                        break
                except:
                    print("\nInvalid choice.\n")
                    continue
            sellerName=allOrders[n][11]; alreadyVoted=False
            while True:
                try:
                    rating=float(input(f"Rate user {sellerName}(From 0.00 to 6.00): "))
                    if rating<0.00 or rating>6.00:
                        print("\nYour rating must be between 0.00 and 6.00 . Try again.\n")
                        continue
                    else:
                        queryExecutor.execute(f"SELECT ratedUsers FROM accounts WHERE id={id}")
                        ratedUsers=queryExecutor.fetchone()
                        if sellerName in ratedUsers[0]:
                            print("\nYou have already voted for this user.\n")
                            alreadyVoted=True
                            break
                        if alreadyVoted==True:
                            break
                        queryExecutor.execute(f"SELECT rating FROM accounts WHERE username='{sellerName}'")
                        sellerRating=queryExecutor.fetchone(); sellerRatingVar=sellerRating[0]; sellerRatingVar+=rating
                        queryExecutor.execute(f"SELECT ratedBy FROM accounts WHERE username='{sellerName}'")
                        ratedBy=queryExecutor.fetchone(); ratedByVar=ratedBy[0]; ratedByVar+=1
                        queryExecutor.execute(f"SELECT ratedUsers FROM accounts WHERE id={id}")
                        ratedUsers=queryExecutor.fetchone(); ratedUsersVar=ratedUsers[0]; ratedUsersVar+=f"{sellerName}"
                        queryExecutor.execute(f"UPDATE accounts SET rating={sellerRatingVar} WHERE username='{sellerName}'"); queryExecutor.execute(f"UPDATE accounts SET ratedBy={ratedByVar} WHERE username='{sellerName}'"); queryExecutor.execute(f"UPDATE accounts SET ratedUsers='{ratedUsersVar}' WHERE id={id}")
                        db_connection.commit()
                        print("\nUser has been rated.\n")
                        proceed = input()
                        break
                except:
                    print("\nInvalid rating. Try again\n")
                    continue
        elif anyFinishedOrders==True and option=="4":
            while True:
                try:
                    n=int(input("Choose an order you'd like to report: "))
                    if n>len(allOrders) or n<0:
                        print("\nInvalid choice.\n")
                        continue
                    else:
                        reportedOrderN=allOrders[n-1][0]; reportedOfferN=allOrders[n-1][1]
                        break
                except:
                    print("\nInvalid choice.\n")
                    continue
            offerFlags=allOrders[n-1][13]; sellerName=allOrders[n-1][11]
            if '[REPORTED]' in offerFlags:
                print("\nYou have already sent a report for that order!\n")
                proceed=input()
            else:
                Report(reportedOrderN,reportedOfferN,sellerName)
        elif anyFinishedOrders==True and option=="5":
            confirm=input("Are you sure you want to perform that action?[Y/N]\n- ")
            currentlyReviewedFound=False
            for k in range(0,len(allOrders)):
                if "[REPORTED]" in allOrders[k][13]:
                    currentlyReviewedFound=True
            if confirm=="Y" or confirm=="y":
                queryExecutor.execute(f"DELETE FROM userorders WHERE (accountId={id} and orderstatus='Finished') and (not orderFlags='[REPORTED]')")
                if currentlyReviewedFound==True:
                    print("\nAll finished orders were cleared. Some orders are currently under review so they can't be deleted.\n")
                    db_connection.commit()
                    proceed = input(); returnToBeginning = True
                    break
                else:
                    db_connection.commit()
                    print("\nAll finished orders were cleared.\n")
                    proceed=input(); returnToBeginning=True
                    break
        if returnToBeginning==True:
            break
    if returnBack==True:
        return 0
    elif returnToBeginning==True:
        CheckMyOrders(id)
    else:
        CheckMyOrders(id)
def mailbox(expressReference=False, recipient=""):
    def SendMessage(recipient=""):
        while True:
            match=False
            if recipient=="":
                recipient=input("Recipient: ")
            if recipient==username[0]:
                print("\nYou can't send a message to yourself.\n")
                recipient=""
                continue
            queryExecutor.execute("SELECT username FROM accounts")
            usersList=queryExecutor.fetchall()
            for k in range(0,len(usersList)):
                if recipient==usersList[k][0]:
                    match=True
                    break
            if match==False:
                if expressReference==True:
                    print("\nThis user no longer exists or their access is restricted.\n")
                    return 0
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
    if expressReference==True:
        SendMessage(recipient)
        return 0
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
                        print(f"This account was created: {accountData[4]}\n\nUsername: {username[0]}\n\nE-mail: {accountData[3]}\n\nAccount rating(Based on user rates): {accountData[5]}\n\nAddress: {accountData[6]}\n\nPhone number: {accountData[7]}\n\nCompany:{accountData[8]}\n[1]Change your username  |  [2]Change your contact information  |  [3]Privacy settings\n")
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
                            elif option2=="3":
                                print("\nHere you can set what contact information can be seen by other users\n")
                                while True:
                                    queryExecutor.execute(f"SELECT accountFlags FROM accounts WHERE id={id[0]}")
                                    accountFlags = queryExecutor.fetchone()
                                    print("\nCurrently:\n")
                                    if "[HideEmail]" in accountFlags[0]:
                                        print("\nYour email is: Hidden")
                                    else:
                                        print("\nYour email is: Visible")
                                    if "[HideAddress]" in accountFlags[0]:
                                        print("\nYour address is: Hidden")
                                    else:
                                        print("\nYour address is: Visible")
                                    if "[HidePhone]" in accountFlags[0]:
                                        print("\nYour phone number is: Hidden")
                                    else:
                                        print("\nYour phone number is: Visible")
                                    if "[HideCompany]" in accountFlags[0]:
                                        print("\nYour company name is: Hidden\n")
                                    else:
                                        print("\nYour company name is: Visible\n")
                                    settingChanged=False
                                    while True:
                                        if settingChanged==True:
                                            break
                                        setting=input("Choose a certain setting by name('Phone','Company','Address','Email'): ")
                                        if setting=="Email" or setting=="Company" or setting=="Address" or setting=="Phone":
                                            print("\n1 - Show | 2 - Hide\n")
                                            while True:
                                                privacyChoice=input("- ")
                                                if privacyChoice=="1":
                                                    if setting=="Email":
                                                        accountFlagsList=[]; k=0
                                                        while k<len(accountFlags[0]):
                                                            if accountFlags[0][k]=="[":
                                                                val=""
                                                                for j in range(k,len(accountFlags[0])):
                                                                    if accountFlags[0][j]!="]":
                                                                        val+=accountFlags[0][j]
                                                                        k+=1
                                                                    else:
                                                                        val+=accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k+=1
                                                                        break
                                                            else:
                                                                k+=1
                                                        try:
                                                            index=accountFlagsList.index("[HideEmail]")
                                                            del accountFlagsList[index]
                                                            newAccountFlags = "".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour email is now visible\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            print("\nYour email is now visible.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Address":
                                                        accountFlagsList=[]; k=0
                                                        while k<len(accountFlags[0]):
                                                            if accountFlags[0][k]=="[":
                                                                val=""
                                                                for j in range(k,len(accountFlags[0])):
                                                                    if accountFlags[0][j]!="]":
                                                                        val+=accountFlags[0][j]
                                                                        k+=1
                                                                    else:
                                                                        val+=accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k+=1
                                                                        break
                                                            else:
                                                                k+=1
                                                        try:
                                                            index=accountFlagsList.index("[HideAddress]")
                                                            del accountFlagsList[index]
                                                            newAccountFlags="".join(accountFlags)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour address is now visible\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            print("\nYour address is now visible\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Phone":
                                                        accountFlagsList=[]; k=0
                                                        while k<len(accountFlags[0]):
                                                            if accountFlags[0][k]=="[":
                                                                val=""
                                                                for j in range(k,len(accountFlags[0])):
                                                                    if accountFlags[0][j]!="]":
                                                                        val+=accountFlags[0][j]
                                                                        k+=1
                                                                    else:
                                                                        val += accountFlags[0][j]
                                                                        k+=1
                                                                        accountFlagsList.append(val)
                                                                        break
                                                            else:
                                                                k+=1
                                                        print(accountFlags)
                                                        try:
                                                            index=accountFlagsList.index("[HidePhone]")
                                                            del accountFlagsList[index]
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour phone number is now visible\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            print("\nYour phone number is now visible\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Company":
                                                        accountFlagsList=[]; k=0
                                                        while k<len(accountFlags[0]):
                                                            if accountFlags[0][k]=="[":
                                                                val=""
                                                                for j in range(k,len(accountFlags[0])):
                                                                    if accountFlags[0][j]!="]":
                                                                        val+=accountFlags[0][j]
                                                                        k+=1
                                                                    else:
                                                                        val += accountFlags[0][j]
                                                                        k+=1
                                                                        accountFlagsList.append(val)
                                                                        break
                                                            else:
                                                                k+=1
                                                        try:
                                                            index=accountFlagsList.index("[HideCompany]")
                                                            del accountFlagsList[index]
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour company name is now visible.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            print("\nYour company name is now visible.\n")
                                                            proceed=input(); settingChanged = True
                                                            break
                                                if privacyChoice=="2":
                                                    queryExecutor.execute(f"SELECT accountFlags FROM accounts WHERE id={id[0]}")
                                                    accountFlags=queryExecutor.fetchone()
                                                    if setting=="Email":
                                                        accountFlagsList=[]; k=0
                                                        while k<len(accountFlags[0]):
                                                            if accountFlags[0][k]=="[":
                                                                val=""
                                                                for j in range(k,len(accountFlags[0])):
                                                                    if accountFlags[0][j]!="]":
                                                                        val+=accountFlags[0][j]
                                                                        k+=1
                                                                    else:
                                                                        val+=accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k+=1
                                                                        break

                                                            else:
                                                                k+=1
                                                        try:
                                                            index=accountFlagsList.index("[HideEmail]")
                                                            print("\nYour email is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            accountFlagsList.append("[HideEmail]")
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour email is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Address":
                                                        accountFlagsList = []; k = 0
                                                        while k < len(accountFlags[0]):
                                                            if accountFlags[0][k] == "[":
                                                                val = ""
                                                                for j in range(k, len(accountFlags[0])):
                                                                    if accountFlags[0][j] != "]":
                                                                        val += accountFlags[0][j]
                                                                        k += 1
                                                                    else:
                                                                        val += accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k += 1
                                                                        break
                                                            else:
                                                                k += 1
                                                        try:
                                                            index=accountFlagsList.index("[HideAddress]")
                                                            print("\nYour address is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            accountFlagsList.append("[HideAddress]")
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour address is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Phone":
                                                        accountFlagsList = []; k = 0
                                                        while k < len(accountFlags[0]):
                                                            if accountFlags[0][k] == "[":
                                                                val = ""
                                                                for j in range(k, len(accountFlags[0])):
                                                                    if accountFlags[0][j] != "]":
                                                                        val += accountFlags[0][j]
                                                                        k += 1
                                                                    else:
                                                                        val += accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k += 1
                                                                        break
                                                            else:
                                                                k += 1
                                                        try:
                                                            index=accountFlagsList.index("[HidePhone]")
                                                            print("\nYour phone is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            accountFlagsList.append("[HidePhone]")
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour phone is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                    elif setting=="Company":
                                                        accountFlagsList = []; k = 0
                                                        while k < len(accountFlags[0]):
                                                            if accountFlags[0][k] == "[":
                                                                val = ""
                                                                for j in range(k, len(accountFlags[0])):
                                                                    if accountFlags[0][j] != "]":
                                                                        val += accountFlags[0][j]
                                                                        k += 1
                                                                    else:
                                                                        val += accountFlags[0][j]
                                                                        accountFlagsList.append(val)
                                                                        k += 1
                                                                        break
                                                            else:
                                                                k += 1
                                                        try:
                                                            index=accountFlagsList.index("[HideCompany]")
                                                            print("\nYour company name is now hidden.\n")
                                                            proceed=input(); settingChanged=True
                                                            break
                                                        except:
                                                            accountFlagsList.append("[HideCompany]")
                                                            newAccountFlags="".join(accountFlagsList)
                                                            queryExecutor.execute(f"UPDATE accounts SET accountFlags='{newAccountFlags}' WHERE id={id[0]} LIMIT 1")
                                                            db_connection.commit()
                                                            print("\nYour company name is now hidden.\n")
                                                            proceed=input(); settingChanged=True
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

def SpecialRequest():
    title = f"Requested By: {username[0]}"
    msg = ""; getBack=False
    while True:
        brand = input("Specify the brand of the car you'd like to request: ")
        if len(brand) < 1:
            print("\nPlease enter a brand name of the car you'd like to request.\n")
            continue
        elif brand == "Return" or brand == "return":
            getBack=True
            break
        else:
            msg += f"[REQUEST DETAILS] Brand: {brand}  | "
            break
    if getBack==True:
        return 0
    if brand == "Return" or brand == "return":
        del msg
        main()
    else:
        while True:
            model = input("Specify the model: ")
            if len(model) < 1:
                print("\nPlease specify the model of the car you'd like to request.\n")
                continue
            else:
                msg += f"Model: {model}  | "
                break
        while True:
            prodYear = input("Specify production year: ")
            if len(prodYear) < 1:
                print("\nPlease specify the production year of the car you'd like to request.\n")
                continue
            else:
                msg += f"Production Year: {prodYear}  | "
                break
        while True:
            fType = input("Specify fuel type: ")
            if len(fType) < 1:
                print("\nPlease specify the fuel type of the car you'd like to request.\n")
                continue
            else:
                msg += f"Fuel Type: {fType}  | "
                break
        while True:
            addNotes = input("Would you like to add any additional notes to this request?(If you wish to skip that, leave blank): ")
            if len(addNotes) == 0:
                msg += f"Additional Comments/Notes: *None*  | "
                break
            else:
                msg += f"Additional Comments/Notes: {addNotes}  | "
                break
        currentTime = time.localtime()
        timeTxt = f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year} {currentTime.tm_hour}:{currentTime.tm_min}"
        msg += f"Sent: {timeTxt}"
        queryExecutor.execute(f"INSERT INTO postbox VALUES('{username[0]}','{title}','{msg}','SPECIAL REQUEST')")
        db_connection.commit()
        print("\nYour request has been sent! You will be contacted as soon as possible.\n")
        proceed = input()
        return 0

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
        currentTime=time.localtime(); t=f"{currentTime.tm_mday}.{currentTime.tm_mon}.{currentTime.tm_year}"
        queryExecutor.execute(f"SELECT orderId, ExpectedDelivery, offerId FROM userorders WHERE accountId={id[0]}")
        userOrders=queryExecutor.fetchall()
        for k in range(0,len(userOrders)):
            if userOrders[k][1]==t:
                queryExecutor.execute(f"UPDATE myoffers SET status='Finished' WHERE offerId={userOrders[2]}")
                queryExecutor.execute(f"INSERT INTO usernotifications VALUES({id[0]},'[Order status] Your order [{userOrders[k][0]}] has reached the expected delivery date, so it was automatically marked as 'Finished'\nYou can now rate the seller or report a problem.', '{t}')")
                db_connection.commit()
        class AccountData:
            accName=username[0]; accId=id[0]
        queryExecutor.execute(f"SELECT * FROM usernotifications WHERE accountId={id[0]}")
        notifications=queryExecutor.fetchall()
        if len(notifications)>0:
            alertStatus=f"You have {len(notifications)} new notifications!"
        else:
            alertStatus = "You have no notifications."
        #currentTime=time.localtime()
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
        print(f"{greeting}, {AccountData.accName}\n\n{alertStatus}\n\n1 - Check the current car offers | 2 - Check your offers\n3 - Post a car offer  |  4 - Check your current orders\n5 - Send special request | 6 - Contact us\n7 - Account details/settings | 8 - Check your notifications\n9 - Go to your mailbox | 10 - Log Off")
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
            if loginStatus == False:
                if option == "4":
                    print("\nPlease log in your accounts or create one first.\n")
                    continue
                elif option == "5":
                    name = ""; getBack=False
                    while True:
                        sender = input("Introduce yourself: ")
                        if len(sender) < 1:
                            continue
                        else:
                            if sender=="RETURN" or sender=="Return" or sender=="return":
                                getBack=True
                                print("\n")
                                break
                            name = sender
                            break
                    if getBack==True:
                        main()
                    print("Title: \n")
                    title = input("- ")
                    print("Message(Please add information about how to contact you at the end):\n")
                    msg = input("- ")
                    print("Confirm you are not a robot:\n")
                    k = 0
                    while k < 3:
                        a = round(1 + random.random() * 15); b = round(1 + random.random() * 15)
                        res = a + b
                        print(f"{a}+{b}=?")
                        userSol = input()
                        if int(userSol) != res:
                            print("\nFailed verification\n")
                            k += 1
                        else:
                            break
                    if k == 3:
                        print("Verification failed 3 times! Try again later.")
                        main()
                    else:
                        queryExecutor.execute(f"INSERT INTO postbox(sentFrom,title,message,category) VALUES('{name}','{title}','{msg}','FEEDBACK/SUPPORT REQUEST');")
                        db_connection.commit()
                        print("Message sent! Thank you for contacting us.\n\n")
                        proceed = input("Proceed?\n")
                        main()
                elif option == "6":
                    if loginStatus == False:
                        print("\n\n\n\n\n\n")
                        if LogInAcc() == True:
                            loginStatus = True
                        main()
                elif option == "7":
                    RegisterAccount()
                    main()
            else:
                if option=="4":
                    CheckMyOrders(id[0])
                    main()
                elif option=="5":
                        SpecialRequest()
                        main()
                elif option=="6":
                    name=AccountData.accName
                    print("Title: \n")
                    title=input("- ")
                    if title=="RETURN" or title=="Return" or title=="return":
                        main()
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
                elif option=="7":
                    AccountSettings()
                elif option=="8":
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
                elif option=="9":
                    mailbox()
                elif option=="10":
                    del AccountData
                    loginStatus=False
                    main()
                else:
                    continue
main()
