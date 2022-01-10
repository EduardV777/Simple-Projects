# 1-Need to add automatic procession of SQL queries
#----------------------------------------------------------------------------
#importing required modules
import webbrowser; import re; import mysql.connector
TypeCheck=re.compile("select", re.I); TypeCheck2=re.compile("update", re.I); TypeCheck3=re.compile("Scaling", re.I); TypeCheck31=re.compile("Scale",re.I)

#Functions related to the update component
def CreateOptionsList(exp):
    global list
    if exp==1:
        global VanillaOptions
        VanillaOptions=["health_min","health_max","mana_min","mana_max","armor","dmg_min","dmg_max","attack_power","ranged_dmg_min","ranged_dmg_max"]
        list=VanillaOptions
    elif exp==2:
        global TBCOptions
        TBCOptions=["MinLevelHealth", "MaxLevelHealth", "MinLevelMana", "MaxLevelMana","MinMeleeDmg", "MaxMeleeDmg","MinRangedDmg","MaxRangedDmg","Armor","MeleeAttackPower"]
        list = TBCOptions
    elif exp==3:
    #To be finished
        global WOTLKOptions
        try:
            raise ValueError("WOTLK queries are not supported at this moment")
        except ValueError as err:
            print(err)
    return list

def UpdateOption(repeat=0):
    global QueryLoc; QueryLoc = open(r"C:\Users\EdwardV\Desktop\SQLQueries.txt", "w")
    #If repeat parameter is activated, deactivate it in the beginning of this function
    if repeat==1:
        repeat=0
    error=0
    if not repeat==True:
        print("\n-----------------------------------------------------------------------------\n\nUpdate Queries have been selected\n")
    print("What do you wanna change:\n1 - NPC Health\n2 - NPC mana\n3 - NPC armor\n4 - NPC damage\n5 - NPC attack power\n6 - NPC range damage\nNOTE: You can choose multiple parameters\n'")
    ##try:
    global rep
    while True:
        rep=input("I want to make queries for this amount of NPCs[limit 150] - ")
        if CheckForCommands.CheckInput(str(rep))==True:
            continue
        elif int(rep)<=0:
            print("Incorrect selection. At least one npc is required")
            continue
        else:
            rep=int(rep)
            break
    ChoiceStarter()



def SelectionList(firstrun=1):
    global saved; global repeat; rep=0
    if dimension==0:
        if firstrun==1:
            saved=0
        print("\n1 - Create more editing queries\n2 - List Current Queries\n3 - Save queries to file\n4 - Clear Queries[Work in progress]\n5 - Perform scaling operation\n6 - Quit the program") #\n6 - Execute queries in your database[T.B.I]
        while True:
            ChoiceEnd=int(input(""))
            if CheckForCommands.CheckInput(str(ChoiceEnd))==True:
                continue
            else:
                break
        if ChoiceEnd==1:
            if saved==1:
                global QueryLoc
                QueryLoc = open(r"C:\Users\EdwardV\Desktop\SQLQueries.txt", "w")
            repeat=1
            RepeatUpdate()
            #UpdateOption(repeat)
        elif ChoiceEnd==2:
            if type==1:
                for i in SQLQuery:
                    print(i + "\n")
            else:
                for i in SQLQuery:
                    print(i+";\n")
            SelectionList()
        elif ChoiceEnd==3:
            if type==1:
                for n in SQLQuery:
                    print(n + "\n", file=QueryLoc)
                QueryLoc.close()
                saved = 1
                SelectionList(0)
            else:
                for n in SQLQuery:
                    print(n+";\n", file=QueryLoc)
                QueryLoc.close()
                saved=1
                SelectionList(0)
        #Clear Queries option here[T.B.I]
        #Perform scaling operation option here[T.B.I]
        elif ChoiceEnd==6:
            print("\nGoodbye! :)")
            return 0
    #elif ChoiceEnd==4:
    if dimension==3:
        if firstrun==1:
            saved=0
        print("\n1 - Create SQL queries\n2 - Repeat another scaling operation\n3 - Quit")
        ChoiceEnd=input("")
        if ChoiceEnd=="1":
            #Need Fix
            Main(0)
        elif ChoiceEnd=="2":
            ScalingOption()
        elif ChoiceEnd=="3":
            print("Goodbye! :)\n")
            return 0



#Functions related to the selecting component
def ChoiceStarter():
   global params; global choice; global name;choice=[]
   while True:
        name = input("Enter the name of the NPC: ")
        if CheckForCommands.CheckInput(name)==True:
            continue
        elif name=="" or name.isdigit()==True:
            print("Name seems to be wrong. Try again\n")
            del name
            continue
        else: break
   while True:
        params=int(input("How many parameters do you wanna set?"))
        if CheckForCommands.CheckInput(str(params))==True:
            continue
        else:
            break
   for i in range(params):
        choice.append(input("Choice " + str(i + 1) + ": "))
   for i in choice:
        if i.isdigit() == False or int(i) < 1 or int(i) > 6:
            for n in range(0,len(choice)):
                del choice[n]
            print("Wrong choice. Try again")
            ChoiceStarter()
   ProcessChoice(list)

#Function for selecting stats to update
def ProcessChoice(list):
   for i in range(0,len(choice)):
       if choice[i]==str("1"):
          global min_health
          min_health=input("Health Min Value: ")
          global max_health
          max_health=input("Health Max Value: ")
       elif choice[i]==str("2"):
          global mana_min
          mana_min=input("Mana Min Value: ")
          global mana_max
          mana_max=input("Mana Max Value: ")
       elif choice[i]==str("3"):
          global armor
          armor=input("Armor Value: ")
       elif choice[i]==str("4"):
          global dmg_min
          dmg_min=input("Damage Min Value: ")
          global dmg_max
          dmg_max=input("Damage Max Value: ")
       elif choice[i]==str("5"):
          global att_power
          att_power=input("Attack Power Value: ")
       elif choice[i]==str("6"):
          global range_min
          range_min=input("Range Damage Min Value: ")
          global range_max
          range_max=input("Range Damage Max Value: ")
   status=1
   if status==1:
      ReturnQuery("",list)

#Function to return and keep queries
def ReturnQuery(select_name="",optionlist=""):
    global UpdateQuery;UpdateQuery="UPDATE creature_template set "
    if iteration==1:
        global SQLQuery; SQLQuery=[]
    if type==2:
        for i in choice:
         if  i==str("1"):
            if expac==1:
                param=optionlist.index("health_min"); param2=optionlist.index("health_max")
                Query=UpdateQuery+optionlist[param]+"="+str(min_health)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
                Query=UpdateQuery+optionlist[param2]+"="+str(max_health)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==2:
                param = optionlist.index("MinLevelHealth"); param2 = optionlist.index("MaxLevelHealth")
                Query = UpdateQuery + optionlist[param] + "=" + str(min_health) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
                Query = UpdateQuery + optionlist[param2] + "=" + str(max_health) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
         elif i==str("2"):
            if expac==1:
                param = optionlist.index("mana_min"); param2 = optionlist.index("mana_max")
                Query=UpdateQuery+optionlist[param]+"="+str(mana_min)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
                Query=UpdateQuery+optionlist[param2]+"="+str(mana_max)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==2:
                param = optionlist.index("MinLevelMana"); param2 = optionlist.index("MaxLevelMana")
                Query = UpdateQuery + optionlist[param] + "=" + str(mana_min) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
                Query = UpdateQuery + optionlist[param2] + "=" + str(mana_max) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
         elif i==str("3"):
            if expac==1 or expac==2:
                param = optionlist.index("armor")
                Query=UpdateQuery+optionlist[param]+"="+str(armor)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
         elif i==str("4"):
            if expac==1:
                param=optionlist.index("dmg_min"); param2=optionlist.index("dmg_max")
                Query=UpdateQuery+optionlist[param]+"="+str(dmg_min)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
                Query=UpdateQuery+optionlist[param2]+"="+str(dmg_max)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==2:
                param = optionlist.index("MinMeleeDmg"); param2 = optionlist.index("MaxMeleeDmg")
                Query = UpdateQuery + optionlist[param] + "=" + str(dmg_min) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
                Query = UpdateQuery + optionlist[param2] + "=" + str(dmg_max) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
         elif i==str("5"):
            if expac==1:
                param = optionlist.index("attack_power")
                Query=UpdateQuery+optionlist[param]+"="+str(att_power)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==2:
                param = optionlist.index("MeleeAttackPower")
                Query = UpdateQuery + optionlist[param] + "=" + str(att_power) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
         elif i==str("6"):
            if expac==1:
                param = optionlist.index("ranged_dmg_min"); param2 = optionlist.index("ranged_dmg_max")
                Query=UpdateQuery+optionlist[param]+"="+str(range_min)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
                Query=UpdateQuery+optionlist[param2]+"="+str(range_max)+' WHERE name="'+name+'"'
                SQLQuery.append(Query)
            elif expac==2:
                param = optionlist.index("MinRangedDmg"); param2 = optionlist.index("MaxRangedDmg")
                Query = UpdateQuery + optionlist[param] + "=" + str(range_min) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
                Query = UpdateQuery + optionlist[param2] + "=" + str(range_max) + ' WHERE name="' + name + '"'
                SQLQuery.append(Query)
            elif expac==3:
                return 0
    if type==1 and len(select_name)>0:
        if count==1:
            UpdateQuery = 'SELECT * from creature_template WHERE name="'+select_name+'"'
        else:
            UpdateQuery = 'SELECT * from creature_template WHERE name="' + select_name + '"'+"\nUNION\n"
        SQLQuery.append(UpdateQuery)
    return SQLQuery

def SelectQueryInitial():
    print("\n-----------------------------------------------------------------------------\nSELECT queries have been selected\n")
    global count
    while True:
        count=input("How many NPCs would you want to select? - ")
        if CheckForCommands.CheckInput(count)==True:
            continue
        elif CheckForCommands.CheckInput(count)=="QUIT_REQUESTED":
            return 0
        elif int(count)<=0:
            print("\nError: The numbers of NPCs is wrong! Try again.\n")
            continue
        else:
            break
    return count


def ProcessSelects(SelectQueryInitial):
    global iteration
    if int(count)>0:
        for i in range(int(count)):
            #print(it is iteration)
            name=input("NPC name: ")
            ReturnQuery(name)
            iteration=iteration+1
            if i==count-1:
                del iteration
                SelectionList()
    else:
        print("Something went wrong")

#Function to repeat update operation if requested from user
def RepeatUpdate():
    iteration=1
    if repeat==1:
        UpdateOption(repeat)
        for i in range(rep):
            if i == rep - 1:
                # del rep
                SelectionList()
            else:
                iteration = iteration + 1
                ChoiceStarter()

#Function related to scaling component(Not finished)
def ScalingOption():
    dungeon=re.compile("Dungeon", re.I); raid=re.compile("Raid", re.I); hp=re.compile("hp",re.I); dmg=re.compile("dmg",re.I); hp2=re.compile("Health",re.I); dmg2=re.compile("Damage",re.I)
    while True:
        scaleType=input("Scaling type[Dungeon/Raid]? - ")
        if CheckForCommands.CheckInput(scaleType)==True:
            continue
        elif CheckForCommands.CheckInput(scaleType)=="QUIT_REQUESTED":
            break; return 0
        if dungeon.search(scaleType) or raid.search(scaleType):
            break
        else:
            print("\nError: You need to select the correct scaling type - Dungeon / Raid\n")
            continue
    while True:
        scaleStat=input("HP or DMG? - ")
        if CheckForCommands.CheckInput(scaleStat)==True:
            continue
        elif CheckForCommands.CheckInput(scaleStat)=="QUIT_REQUESTED":
            break; return 0
        if hp.search(scaleStat) or hp2.search(scaleStat):
            break
        else:
            print("\nError: You need to select one of both available stats\n")
            continue
    while True:
        AdminLvl=int(input("Admin Player Level - "))
        if CheckForCommands.CheckInput(AdminLvl)==True:
            continue
        elif CheckForCommands.CheckInput(AdminLvl)=="QUIT_REQUESTED":
            break; return 0
        if AdminLvl<=0:
            print("Error: Admin player level must be over 0")
            continue
        else:
            break
    while True:
        NPCLvl=int(input("NPC Level - "))
        if CheckForCommands.CheckInput(NPCLvl)==True:
            continue
        elif CheckForCommands.CheckInput(NPCLvl)=="QUIT_REQUESTED":
            break; return 0
        if NPCLvl<=0:
            print("Error: NPC Level must be over 0")
            continue
        else:
            break

    #DUNGEON SCALING FOR BOTH: HP/DMG
            #If HP selected
    if dungeon.search(scaleType) and (hp.search(scaleStat) or hp2.search(scaleStat)):
        while True:
            AdminHP=int(input("Admin Player HP - "))
            if CheckForCommands.CheckInput(AdminHP)==True:
                continue
            elif CheckForCommands.CheckInput(AdminHP)=="QUIT_REQUESTED":
                break; return 0
            if AdminHP<=0:
                print("\nError: Admin Player HP must be over 0")
                continue
            else:
                break
        while True:
            NPCHP=int(input("NPC HP - "))
            if CheckForCommands.CheckInput(NPCHP)==True:
                continue
            elif CheckForCommands.CheckInput(NPCHP)=="QUIT_REQUESTED":
                break; return 0
            if NPCHP<=0:
                print("\nError: NPC HP must be over 0")
                continue
            else:
                break
        #Scaling down  (May need to be revised)
        if NPCHP>AdminHP:
            print("\nNOTICE: Scaling down of NPC's health started...\n")
            RH=NPCHP-AdminHP; LD_10=(AdminLvl-NPCLvl)*1/10
            if LD_10<0: LD_10=abs(LD_10)
            formula_down=(RH*LD_10)+RH
            print("Final NPC HP = "+str(formula_down)+"\n\n")
            SelectionList()
        #Scaling up
        elif NPCHP<AdminHP:
            print("\nNOTICE: Scaling up of NPC's health started...\n")
            formula_up=(AdminHP+NPCHP)*0.5
            print("Final NPC HP = "+str(formula_up)+"\n\n")

            #If DMG is selected
    if dungeon.search(scaleType) and (dmg.search(scaleStat) or dmg2.search(scaleStat)):
        while True:
            AdminDmgMin=input("Admin Min Dmg: ")
            if CheckForCommands.CheckInput(AdminDmgMin)==True:
                continue
            elif CheckForCommands.CheckInput(AdminDmgMin)=="QUIT_REQUESTED":
                break; return 0
            if AdminDmgMin<=0:
                print("Error: Damage rate must be over 0! Try again.\n")
                continue
            else:
                break
        while True:
            AdminDmgMax=input("Admin Max Dmg: ")
            if CheckForCommands.CheckInput(AdminDmgMax)==True:
                continue
            elif CheckForCommands.CheckInput(AdminDmgMax)=="QUIT_REQUESTED":
                break; return 0
            if AdminDmgMax<=0:
                print("Error: Damage rate must be over 0! Try again.\n")
                continue
            else:
                break
        while True:
            NPCDMGMin=input("NPC Min Dmg: ")
            if CheckForCommands.CheckInput(NPCDMGMin)==True:
                continue
            elif CheckForCommands.CheckInput(NPCDMGMin)=="QUIT_REQUESTED":
                break; return 0
            if NPCDMGMin<=0:
                print("\nError: Damage rate must be over 0! Try again.\n")
                continue
            else:
                break
        while True:
            NPCDMGMax=input("NPC Max Dmg: ")
            if CheckForCommands.CheckInput(NPCDMGMax)==True:
                continue
            elif CheckForCommands.CheckInput(NPCDMGMax)=="QUIT_REQUESTED":
                break; return 0
            if NPCDMGMax<=0:
                print("\nError: Damage rate must be over 0! Try again.\n")
                continue
            else:
                break
        if NPCDMGMin>AdminDmgMin and NPCDMGMax>AdminDmgMax:
            LD_10=(AdminLvl-NPCLvl)*1/10
            if LD_10<0: LD_10=abs(LD_10)
           #Scaling down    (May need to be revised)
            formula_down=(NPCDMGMin-AdminDmgMin)*LD_10
            print("Final NPC Min Dmg: "+str(formula_down)+";\n")
            formula_down = (NPCDMGMax - AdminDmgMax) * LD_10
            print("Final NPC Max Dmg: " + str(formula_down) + ";\n")
            #Scaling up[TO BE IMPLEMENTED]
        if NPCDMGMin<AdminDmgMin and NPCDMGMax<AdminDmgMax:
            print("Error: Scaling up is still not implemented! For more information execute special command '/version'\n")

    #RAID SCALING[T.B.I]
    if raid.search(scaleType):
        print("\nError: Raid scaling is work in progress! For more information check '/version'\n")

#Bugtracker functionality
def EstablishBugTrackerConnection():
    # IP search needs fixing!!!!!
    isItIp = re.compile("[0-255].[0-255].[0-255].[0-255]"); isItLocalhost = re.compile("localhost", re.I)
    global hostname; global database; global username; global password
    print("\nNOTICE: Connecting to bugtracker...\n\nSome data is required to establish the connection\n")
    while True:
        hostname = input("Hostname: ")
        if CheckForCommands.CheckInput(hostname)==0:
            return 0
        elif isItIp.search(hostname) or isItLocalhost.search(hostname):
            break
        else:
            print("\n[Error: Invalid hostname]\n")
            continue
    while True:
        database = input("Database name: ")
        bugtrackerDB = re.compile("bugtracker", re.I)
        if bugtrackerDB.search(database):
            break
        elif CheckForCommands.CheckInput(database)==0:
            return 0
        else:
            print("\n[Error: The database name is invalid. Unexpected name '" + database + "' (Database must be named 'Bugtracker') ]\n")
            continue
    while True:
        username = input("Username: ")
        if CheckForCommands.CheckInput(username) == 0:
            return 0
        elif username != "" or not len(username) < 3:
            break
        else:
            print("\n[Error: Incorrect Username]\n")
            continue
    while True:
        password = input("Password: ")
        if CheckForCommands.CheckInput(password)==0:
            return 0
        elif password != "" or not len(password) < 3:
            break
        else:
            print("\n[Error: Incorrect Password]\n")
            continue
    try:
        connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password)
    except mysql.connector.errors.ProgrammingError:
        print("\n[Error: Something went wrong!]")

    print("\nProcessing...\n")
    try:
        if mysql.connector.MySQLConnection.is_connected(connection):
            print("NOTICE: Connection established successfully!\n")
            BugTrackerOperations(1, connection)
        else:
            print("Error: Something went wrong!\n")
    except UnboundLocalError:
        print("\n[Connection_Error: Given data is incorrect, try again]\n  !--Initializing Bugtracker interrupted--!")
    return "BUGTRACKER_CONNECTION_REQUESTED"

def BugTrackerOperations(firstrun, connection_var):
    if firstrun==1:
        print(mysql.connector.MySQLConnection.is_connected(connection_var))
        print("\n------------------BugTracker component initialized------------------\n1 - Register a bug       2 - Check current bugs\n3 - Return to start and close connection\n")
    else:
        print("\n------------------BugTracker------------------\n1 - Register a bug       2 - Check current bugs\n3 - Return to start and close connection\n")
    while True:
        choice=input()
        if CheckForCommands.CheckInput(choice)==True:
            continue
        else:
            break
    if choice=="1":
        def RegisterBug(connection_var):
            #print(connection_var)
            values={'type':"0", 'Content_Expansion':"0", 'Title':"", 'Description':"", 'Date_of_report':"", 'Solution':""}
            Query="Insert into Bugtracker (Type,Content_Expansion,Title,Description,Date_of_report,Solution) values("
            for k in values:
                if k=="Solution":
                    n=input(k+": ")
                    Query+='"'+n+'");'
                else:
                    if values[k].isdigit():
                        n=int(input(k+": "))
                        Query+=str(n)+","
                    else:
                        n=input(k+": ")
                        Query+='"'+n+'",'
            cursor=connection_var.cursor()
            cursor.execute(Query); cursor.fetchall(); connection_var.commit()
            print("Action finished!")
        RegisterBug(connection_var); del RegisterBug
        BugTrackerOperations(0, connection_var)
    elif choice=="2":
        def ListBugs():
            Query="Select * from bugtracker"
            cursor=connection_var.cursor()
            cursor.execute(Query); list=cursor.fetchall()
            print("Current bugs found in the database:\n")
            for k in range(len(list)):
                print(list[k])
            print("\n")
        ListBugs(); del ListBugs
        BugTrackerOperations(0,connection_var)
    elif choice=="3":
        connection_var.close(); del connection_var; print("\nLeaving bugtracker and closing connection...\n")

#Classes
class SpecialCommands:
    def CheckInput(self,inputsource):
        restart=re.compile("/restart", re.I); version=re.compile("/version",re.I); help=re.compile("/help",re.I); website=re.compile("/website", re.I); license=re.compile("/license", re.I)
        bugtracker=re.compile("/connect_bugtracker", re.I); quit=re.compile("/quit", re.I); InterruptEstablishingConnection=re.compile("/quit_bugtracker", re.I); q=re.compile("/q", re.I)
        if restart.search(inputsource):
            print("Restart requested...\n\n")
            Main()
        elif version.search(inputsource):
            ver_msg="\nNPC Creator 0.2v[ALPHA]"
            description="This is the second release of NPCQueriesCreator. The current version is 0.2A.\n It has been expanded with more functionalities and minor bug fixes have been performed.\n Thank you for using NPCQueriesCreator 0.2v!\nUPCOMING VERSION: 0.3v\nRELEASE DATE: ? September 2021\nPATCH NOTES: TBA"
            print("%50s" % ver_msg+"\n")
            print("%20s" % description+"\n")
            return True
        elif help.search(inputsource):
            print("Help command is not finished yet")
            return True
        elif website.search(inputsource):
            reloc=open(r"C:\Users\EdwardV\Desktop\Reloc.html","w")
            htmlcode="<!DOCTYPE html><html><head><script type='text/javascript'>window.onload=function(){window.location.assign('http://192.168.0.109/index.php'); }</script></head><body><h5>Redirecting...</h5></body></html>"
            print(htmlcode, file=reloc); reloc.close()
            print("\nOpening website...\n\n")
            webbrowser.open_new_tab(r"C:\Users\EdwardV\Desktop\Reloc.html")
            return True
        elif license.search(inputsource):
            print("\nLicense not available\n")
            return True
        elif bugtracker.search(inputsource):
            EstablishBugTrackerConnection()
        elif InterruptEstablishingConnection.search(inputsource):
            return 0
        elif quit.search(inputsource) or q.search(inputsource):
            print("\nGoodbye :)\n"); return "QUIT_REQUESTED"

#Classes

#Objects based on classes
CheckForCommands=SpecialCommands()
#Objects based on classes

#Defining Main() function of the program
def Main(firstrun=1):
    if firstrun==1:
        global params; global status; global iteration; global type; global repeat; global expac; global expac_input; global dimension
        params=0;status=0;iteration=1;type=0; repeat=0; expac=0; dimension=0
        print("\n\n_____________________________________________________________________________\n          Welcome to 'NPC Queries Creator V0.2'\n")
    dimension=0
    while True:
        QueryType=input("What kind of operation would you like to complete? (SELECT/UPDATE/Scaling): \n(NOTICE: If you want to connect to bugtracker use command '/connect_bugtracker') - ")
        if CheckForCommands.CheckInput(QueryType)==True:
            continue
        elif CheckForCommands.CheckInput(QueryType) == "QUIT_REQUESTED":
            break; return 0
        elif TypeCheck.search(QueryType) or TypeCheck2.search(QueryType) or TypeCheck3.search(QueryType) or TypeCheck31.search(QueryType):
            break
        else:
            print("\nQuery Type is not recognised, try again.\n")
            continue
    #If SELECT component is choosen, push user into alternate path and show different version of selectionList at the end
    if TypeCheck3.search(QueryType) or TypeCheck31.search(QueryType):
        type=3
        dimension=3
        ScalingOption()

    elif TypeCheck2.search(QueryType):
        type=2
        while True:
            expac_input=input("What expansion are queries created for? (1: Vanilla; 2: Burning Crusade; 3: Wrath of The Lich King) - ")
            if CheckForCommands.CheckInput(expac_input)==True:
                continue
            elif CheckForCommands.CheckInput(expac_input)=="QUIT_REQUESTED":
                break; return 0
            elif expac_input!="3" and expac_input!="2" and expac_input!="1":
                print("Expansion has not been recognised, try again.\n")
                continue
            else:
                break
        if expac_input==str(1):
            expac=1
            CreateOptionsList(expac)
        elif expac_input==str(2):
            expac=2
            CreateOptionsList(expac)
        elif expac_input==str(3):
            expac=3
            CreateOptionsList(expac)
        UpdateOption()
        for i in range(rep):
            if i == rep-1:
                #del rep
                SelectionList()
            else:
                iteration=iteration+1
                ChoiceStarter()

    elif TypeCheck.search(QueryType):
        type=1
        ProcessSelects(SelectQueryInitial())
#Beginning
Main()


#NOTES
#Wrath of the Lich King stats are not implemented
#/quit_bugtracker command needs to be entered twice to leave EstablishingBugTrackerConnection()