import os

class File:
    def __init__(self,filePath):
        self.file=open(filePath,"a")
        self.filePath=filePath.split("\\")
        self.extension=self.filePath[len(self.filePath)-1]; self.extension=self.extension.split("."); self.extension=self.extension[1]
        self.fileName=self.filePath[len(self.filePath)-1]
        self.filePath="".join(self.filePath)
        self.fileMode="a"
        self.readFile=open(self.filePath,"r")
        self.contents=self.readFile.read()
    def edit(self):
        try:
            saveState = 1; stopEditingCurrFile=0
            extension = ""; content=""
            editing = False
            while True:
                if stopEditingCurrFile == 1:
                    return 0
                if editing == False:
                    if stopEditingCurrFile == 1:
                        break
                    head = f"\n{'-' * 156}\n{' ' * 80}{self.fileName}{' ' * 80}\n{'-' * 156}"
                    self.fileName = self.fileName.split("*"); self.fileName = self.fileName[0]
                    print(head)
                    print("You can enter the command !_quit_! to exit | !_save_! / !_save_as_! to save the new changes to the file")
                    print("\n\n")
                    print(self.contents)
                    editing = True
                if stopEditingCurrFile == 1:
                    break
                while True:
                    if stopEditingCurrFile == 1:
                        return 0
                    textEntry = input("-")
                    if textEntry.find("!_quit_!") == 0:
                        if saveState == 0:
                            print("You have unsaved changes to this file! Select an option - Save | Do not save")
                            while True:
                                option=input("- ")
                                if option.lower()=="save":
                                    self.file.write(content)
                                    self.file.close()
                                    del self.file
                                    stopEditingCurrFile=1
                                    break
                                elif option.lower()=="do not save":
                                    stopEditingCurrFile=1
                                    break
                        else:
                            self.file.close()
                            del self.file
                            stopEditingCurrFile = 1

                    elif textEntry.find("!_save_!") == 0:
                        self.file.write(content)
                        self.file.close()
                        content=""
                        print("Changes saved.")
                    # save as command doesn't save file contents!
                    elif textEntry.find("!_save_as_!") == 0:
                        confirm = input("Do you want to change the file name[Y/N]?:  ")
                        if confirm.lower() == "y":
                            newFileName = input("New File Name: ")
                            if extension != "":
                                newFileName += extension
                            fileName = newFileName
                        confirm = input("Do you want to change file type[Y/N]?: ")
                        if confirm.lower() == "y":
                            while True:
                                newExt = input("New File Type: ")
                                if "." in newExt:
                                    if ShowExtensions(False, True, newExt):
                                        extension = ValidExt
                                        if "." in self.fileName:
                                            self.fileName = self.fileName.split("."); self.fileName[1] = ValidExt
                                            fileName = ".".join(self.fileName)
                                        else:
                                            fileName += newExt
                                        if "." in filePath:
                                            filePath = filePath.split(".");
                                            filePath[1] = ValidExt;
                                            filePath = ".".join(filePath)
                                        else:
                                            filePath += ValidExt
                                        break
                                else:
                                    if ShowExtensions(True, False, newExt):
                                        extension = ValidExt
                                        if "." in fileName:
                                            fileName = fileName.split("."); fileName[1] = ValidExt;
                                            fileName = ".".join(fileName)
                                        else:
                                            fileName += newExt
                                        if "." in filePath:
                                            filePath = filePath.split("."); filePath[1] = ValidExt
                                            filePath = ".".join(filePath)
                                        else:
                                            filePath += ValidExt
                                        break
                        confirm = input("Do you want to change save location[Y/N]?: ")
                        if confirm.lower() == "y":
                            while True:
                                newSaveLoc = SaveLocation(fileName)
                                try:
                                    fileLoc.close()
                                    fileLoc = open(newSaveLoc, "a")
                                    filePath = newSaveLoc
                                    fileLoc.write(content)
                                    fileLoc.close()
                                    break
                                except FileNotFoundError:
                                    continue
                        print("File has been saved!")
                        saveState += 1; content = ""
                    else:
                        content += f"{textEntry}\n"
                        saveState=0

        except FileNotFoundError:
            print("The path you selected does not exist!")
            hold = input("Press any button to continue...")
        if stopEditingCurrFile == 1:
            return 0
    def UpdatePath(self):
        pass

def ShowExtensions(searchForType=False, searchForExtension=False, ext=""):
    global ValidExt
    extensionsList = {"Normal Text": [".txt"], "Flash ActionScript": [".as", ".mx"],
                      "Ada": [".ada", ".ads", ".adb"], "Assembly Language Source": [".asm"],
                      "Abstract Syntax Notation One": [".mib"], "Active Server Pages Script": [".asp"],
                      "Autolt": [".au3"], "AviSynth Scripts": [".avs", ".avsi"],
                      "BaanC": [".bc", ".cln"],
                      "Unix Script": ["bash", ".sh", ".bsh", ".csh", ".bash_profile", ".bashrc",
                                      ".profile"], "Batch": [".bat", ".cmd", ".nt"],
                      "BlitzBasic": [".bb"], "C Source": [".c", ".lex"],
                      "Categorical Abstract Machine Language": [".ml", ".mli", ".sml", ".thy"],
                      "CMake": [".cmake"],
                      "COmmon Bussiness Oriented Language": [".cbl", ".cbd", ".cdb", ".cdc", ".cob",
                                                             ".cpy", ".copy", ".lst"],
                      "Csound": [".orc", ".sco", ".csd"], "CoffeeScript": [".coffee", ".litcoffee"],
                      "C++ Source": [".cpp", ".cxx", ".cc", ".h", ".hh", ".hpp", ".hxx", ".ino"],
                      "C# Source": [".cs"], "Cascade Style Sheets": [".css"],
                      "D Programming Language": [".d"], "Diff": [".diff", ".patch"],
                      "Erlang": [".erl", ".hrl"], "ESCRIPT": [".src", ".em"], "Forth": [".forth"],
                      "Fortran free form source": [".f", ".for", ".f90", ".f95", ".f2k", "f23"],
                      "Fortran fixed form source": [".f77"], "FreeBasic": [".bas", ".bi"],
                      "Haskell": [".hs", ".lhs", ".las"],
                      "Hyper Text Markup Language": [".html", ".htm", ".shtml", ".shtm", ".xhtml",
                                                     ".xht", ".hta"],
                      "MS ini": [".ini", ".inf", "url", "wer"], "Inno Setup": [".iss"],
                      "Intel HEX binary data": [".hex"], "Java source": [".java"],
                      "JavaScript": [".js", ".jsm", ".jsx", ".ts", ".tsx"], "JSON": [".json"],
                      "JavaServer Pages script": [".jsp"], "KiXtart": [".kix"],
                      "List Processing Language": [".lsp", ".lisp"], "LaTeX": [".tex", ".sty"],
                      "Lua source": [".lua"], "Makefile": [".mak", ".mk"], "MATrix LABoratory": [".m"],
                      "MMIXAL": [".mms"], "Nimrod": [".nim"], "extended crontab": [".tab", ".spf"],
                      "MSDOS Style/ASCII Art": [".nfo"],
                      "NullSoft Scriptable Install System script": [".nsi", ".nsh"],
                      "OScript source": [".osx"], "Objective-C source": [".mm"],
                      "Pascal source": [".pas", ".pp", ".p", ".inc", ".lpr"],
                      "Perl Source": [".pl", ".pm", ".plx"],
                      "PHP Hypertext Preprocessor": [".php", ".php3", ".php4", ".php5", ".phps",
                                                     ".phpt", ".phtml"], "PostScript": [".ps"],
                      "Windows PowerShell": [".ps1", ".psm1"], "Properties": [".properties"],
                      "PureBasic": [".pb"], "Python": [".py", ".pyw"],
                      "R programming language": [".r", ".s", ".splus"]}
    if searchForType==False and searchForExtension==False:
        for j in extensionsList:
            print(f"{', '.join(extensionsList[j])} -- {j}")
            print("\n")
    elif searchForType==False and searchForExtension==True:
        extensionFound=False
        for j in extensionsList:
            for k in range(0, len(extensionsList[j])):
                if ext == extensionsList[j][k]:
                    extensionFound = True
                    ValidExt=ext
                    break
            if extensionFound == True:
                break
        if extensionFound == False:
            print("No such file extension exists. Try again.")
        return extensionFound
    elif searchForType==True and searchForExtension==False:
        typeFound = False
        for j in extensionsList:
            if j.lower() == ext:
                typeFound = True
                ValidExt=extensionsList[j][0]
                break
        if typeFound == False:
            print("No such type exists. Try again.")
        return typeFound

def SaveLocation(fileName):
    isItWin11=False
    while True:
        path = input("Where would you like to save your file?(Desktop, Documents...or enter specific path) - ")
        user = os.getlogin(); possibleDriveName = []; ind = 0; absolutePath = False
        if os.path.exists(f"C:\\Users\\{user}\\OneDrive\\Desktop"):
            isItWin11=True
        for k in range(65, 91):
            possibleDriveName.append(chr(k))
        while ind < len(possibleDriveName):
            if f"{possibleDriveName[ind]}:\\" in path:
                absolutePath = True
                break
            else:
                ind += 1
                continue
        if absolutePath == True:
            break
        else:
            if "desktop" in path.lower():
                if isItWin11==False:
                    return f"C:\\Users\\{user}\\Desktop\\{fileName}"
                else:
                    return f"C:\\Users\\{user}\\OneDrive\\Desktop"
            elif "documents" in path.lower():
                if isItWin11==False:
                    return f"C:\\Users\\{user}\\Documents\\{fileName}"
                else:
                    return f"C\\Users\\{user}\\OneDrive\\Documents"
            elif "pictures" in path.lower():
                if isItWin11==False:
                    return f"C:\\Users\\{user}\\Pictures\\{fileName}"
                else:
                    return f"C:\\Users\\{user}\\OneDrive\\Pictures"
            elif "videos" in path.lower():
                return f"C:\\Users\\{user}\\Videos\\{fileName}"
            elif "downloads" in path.lower():
                return f"C:\\Users\\{user}\\Downloads\\{fileName}"
            elif "music" in path.lower():
                return f"C:\\Users\\{user}\\Music\\{fileName}"
            elif "users" in path.lower():
                return f"C:\\Users\\{user}\\{fileName}"

    if absolutePath==True:
        return path

def menu():

    while True:
        stopEditingCurrFile = 0
        print(f"{' '*10}Python Notepad 0.1\n")
        print(f"'Create' - create a new file | 'Open' - open a file to edit\n\n'Quit' - leave the program\n")
        quitReq=False
        while True:
            userInput=input("- ")
            fileMode = "w"
            if userInput.lower()=="create":
            #---------------------------------Create-------------------------------------------------------------------#
                forbiddenSymbols="\\/*:<>|"
                while True:
                    fileName=input("Enter name of file: ")
                    if fileName.lower()=="con":
                        print('Invalid filename')
                        continue
                    else:
                        invalidFile=False
                        for k in range(0,len(forbiddenSymbols)):
                            if forbiddenSymbols[k] in fileName:
                                print("Invalid filename")
                                invalidFile=True
                                break
                        if invalidFile==True:
                            continue
                        else:
                            break
                filePath=SaveLocation(fileName)
                try:
                    fileLoc=open(f"{filePath}", f"{fileMode}")
                    saveState=0; newFile=True; content=""; extension=""
                    editing=False
                    while True:
                        if editing==False:
                            fileLoc = open(f"{filePath}", f"r")
                            if stopEditingCurrFile == 1:
                                break
                            if saveState == 0:
                                fileName+="*"
                            head = f"\n{'-'*156}\n{' ' * 80}{fileName}{' '*80}\n{'-'*156}"
                            fileName=fileName.split("*"); fileName=fileName[0]
                            print(head)
                            print("You can enter the command !_quit_! to exit | !_save_! / !_save_as_! to save the new changes to the file")
                            print("\n\n")
                            if saveState != 0:
                                print(fileLoc.read())
                            editing=True
                            fileLoc.close()
                        if stopEditingCurrFile == 1:
                            break
                        fileLoc = open(f"{filePath}", f"{fileMode}")
                        textEntry=input("-")
                        if textEntry.find("!_quit_!")==0:
                            if saveState==0:
                                print("What extension/type do you want to save the file in?('Show Extensions' - to show you a list with possible extensions)")
                                while True:
                                    ext=input("- ")
                                    if "show extensions" in ext.lower():
                                        ShowExtensions()
                                    else:
                                        if "." in ext:
                                            if ShowExtensions(False,True,ext)==True:
                                                filePath+=ValidExt
                                                fileLoc=open(filePath,"w")
                                                fileLoc.write(content)
                                                fileLoc.close()
                                                saveState+=1
                                                print(f"File {fileName} has been saved successfully!")
                                                hold=input()
                                                stopEditingCurrFile=1
                                                break
                                        else:
                                            if ShowExtensions(True,False,ext)==True:
                                                filePath+=ValidExt
                                                fileLoc=open(filePath,"w")
                                                fileLoc.write(content)
                                                fileLoc.close()
                                                print(f"File {fileName} has been saved successfully!")
                                                hold=input()
                                                stopEditingCurrFile=1
                                                break
                            else:
                                fileLoc.close()
                                del fileLoc
                                stopEditingCurrFile=1

                        elif textEntry.find("!_save_!")==0:
                            if saveState==0 and newFile==True:
                                print("What extension/type do you want to save the file as?('Show Extensions' - to show you a list with possible extensions)")
                                while True:
                                    ext = input("- ")
                                    if "show extensions" in ext.lower():
                                        ShowExtensions()
                                    else:
                                        if "." in ext:
                                            if ShowExtensions(False,True,ext)==True:
                                                fileName+=ValidExt
                                                fileLoc=open(f"{filePath}", fileMode)
                                                fileLoc.write(content)
                                                fileLoc.close()
                                                extension=ValidExt
                                                content=""; fileMode="a"; newFile=False
                                                saveState+=1
                                                print("Changes saved.")
                                                editing=False
                                                break
                                        else:
                                            if ShowExtensions(True,False,ext)==True:
                                                filePath+=ValidExt
                                                filePath += ValidExt
                                                fileLoc = open(f"{filePath}", fileMode)
                                                fileLoc.write(content)
                                                fileLoc.close()
                                                content = ""; fileMode = "a"; newFile = False
                                                saveState += 1
                                                print("Changes saved.")
                                                editing=False
                                                break
                            else:
                                fileMode = "a"
                                fileLoc.write(content)
                                fileLoc.close()
                                print("Changes saved.")
                        #save as command doesn't save file contents!
                        elif textEntry.find("!_save_as_!")==0:
                            confirm=input("Do you want to change the file name[Y/N]?:  ")
                            if confirm.lower()=="y":
                                newFileName=input("New File Name: ")
                                if extension!="":
                                    newFileName+=extension
                                fileName=newFileName
                            confirm=input("Do you want to change file type[Y/N]?: ")
                            if confirm.lower()=="y":
                                while True:
                                    newExt=input("New File Type: ")
                                    if "." in newExt:
                                        if ShowExtensions(False,True,newExt):
                                            extension=ValidExt
                                            if "." in fileName:
                                                fileName=fileName.split("."); fileName[1]=ValidExt; fileName=".".join(fileName)
                                            else:
                                                fileName+=newExt
                                            if "." in filePath:
                                                filePath=filePath.split("."); filePath[1]=ValidExt; filePath=".".join(filePath)
                                            else:
                                                filePath+=ValidExt
                                            break
                                    else:
                                        if ShowExtensions(True,False,newExt):
                                            extension=ValidExt
                                            if "." in fileName:
                                                fileName=fileName.split("."); fileName[1]=ValidExt; fileName=".".join(fileName)
                                            else:
                                                fileName+=newExt
                                            if "." in filePath:
                                                filePath=filePath.split("."); filePath[1]=ValidExt; filePath=".".join(filePath)
                                            else:
                                                filePath+=ValidExt
                                            break
                            confirm=input("Do you want to change save location[Y/N]?: ")
                            if confirm.lower()=="y":
                                while True:
                                    newSaveLoc=SaveLocation(fileName)
                                    try:
                                        fileLoc.close()
                                        fileLoc=open(newSaveLoc, fileMode)
                                        filePath = newSaveLoc
                                        fileLoc.write(content)
                                        fileLoc.close()
                                        break
                                    except FileNotFoundError:
                                        continue
                            print("File has been saved!")
                            saveState+=1; content=""
                        else:
                            content += f"{textEntry}\n"

                except FileNotFoundError:
                    print("The path you selected does not exist!")
                    hold=input("Press any button to continue...")
                    break
            if stopEditingCurrFile==1:
                break
            #---------------------------------Create-------------------------------------------------------------------#
            elif userInput.lower()=="open":
                while True:
                    path=input("Please enter the path of the file: ")
                    if os.path.exists(path):
                        path=path.split("\\"); testFileName=path[len(path)-1]; testFileName=testFileName.split("."); testFileName[1]="."+testFileName[1]
                        if ShowExtensions(False,True,testFileName[1]):
                            path="\\".join(path)
                            openedFile=File(path)
                            break
                        else:
                            print("This is not a valid file!")
                            continue
                    else:
                        print("Invalid file path!\n")
                        continue
                openedFile.edit()
            # ---------------------------------Open--------------------------------------------------------------------#
            elif "quit" in userInput.lower():
                print("Leaving Python Notepad...")
                quitReq = True
                break
        if quitReq==True:
            break
    return 0

menu()
