import os
#print(os.getlogin())

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
                while True:
                    filePath=input("Where would you like to save your file?(Desktop, Documents...or enter specific path) - ")
                    user = os.getlogin(); possibleDriveName=[]; ind=0; absolutePath=False
                    for k in range(65,91):
                        possibleDriveName.append(chr(k))
                    while ind<len(possibleDriveName):
                        if f"{possibleDriveName[ind]}:\\" in filePath:
                            absolutePath=True
                            break
                        else:
                            ind+=1
                            continue
                    if absolutePath==True:
                        break
                    else:
                        if "desktop" in filePath.lower():
                            filePath=f"C:\\Users\\{user}\\Desktop\\{fileName}"
                            break
                        elif "documents" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\Documents\\{fileName}"
                            break
                        elif "pictures" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\Pictures\\{fileName}"
                            break
                        elif "videos" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\Videos\\{fileName}"
                            break
                        elif "downloads" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\Downloads\\{fileName}"
                            break
                        elif "music" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\Music\\{fileName}"
                            break
                        elif "users" in filePath.lower():
                            filePath = f"C:\\Users\\{user}\\{fileName}"
                            break

                try:
                    fileLoc=open(f"{filePath}", f"{fileMode}")
                    saveState=0; newFile=False; extension=""; content=""
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
                    while True:
                        if stopEditingCurrFile==1:
                            break
                        head=f"\n\n{' '*15}{fileName}"
                        if saveState==0:
                            head+="*"
                        print(head)
                        print("You can enter the command !_quit_! to exit | !_save_! / !_save_as_! to save the new changes to the file")
                        print("\n\n")
                        if saveState!=0:
                            if len(fileLoc.read())>0:
                                print(fileLoc.read())
                        while True:
                            if stopEditingCurrFile == 1:
                                break
                            textEntry=input("-")
                            if textEntry.find("!_quit_!")==0:
                                if saveState==0:
                                    print("What extension/type do you want to save the file in?('Show Extensions' - to show you a list with possible extensions)")
                                    while True:
                                        ext=input("- ")
                                        if "show extensions" in ext.lower():
                                            for j in extensionsList:
                                                print(f"{', '.join(extensionsList[j])} -- {j}")
                                                print("\n")
                                        else:
                                            typeFound=False; extensionFound=False
                                            extensionString=""
                                            if "." in ext:
                                                for j in extensionsList:
                                                    for k in range(0,len(extensionsList[j])):
                                                        if ext==extensionsList[j][k]:
                                                            extensionFound=True
                                                            extensionString=extensionsList[j][k]
                                                            break
                                                    if extensionFound==True:
                                                        break
                                                if extensionFound==False:
                                                    print("No such file extension exists. Try again.")
                                                else:
                                                    filePath+=ext
                                                    fileLoc=open(filePath,"w")
                                                    print(content, file=fileLoc)
                                                    saveState+=1
                                                    print(f"File {fileName} has been saved successfully!")
                                                    hold=input()
                                                    stopEditingCurrFile=1
                                                    break
                                            else:
                                                typeFound=False
                                                for j in extensionsList:
                                                    if j.lower()==ext:
                                                        typeFound=True
                                                        filePath+=extensionsList[j][0]
                                                        break
                                                if typeFound==False:
                                                    print("No such type exists. Try again.")
                                                else:
                                                    filePath+=ext
                                                    fileLoc=open(filePath,"w")
                                                    print(content, file=fileLoc)
                                                    print(f"File {fileName} has been saved successfully!")
                                                    hold=input()
                                                    stopEditingCurrFile=1
                                                    break
                                else:
                                    stopEditingCurrFile=1

                            elif textEntry.find("!_save_!")==0:
                                if saveState==0 and newFile==False:
                                    print("What extension/type do you want to save the file in?('Show Extensions' - to show you a list with possible extensions)")
                                    while True:
                                        ext = input("- ")
                                        if "show extensions" in ext.lower():
                                            for j in extensionsList:
                                                print(f"{', '.join(extensionsList[j])} -- {j}")
                                                print("\n")
                                        else:
                                            typeFound = False
                                            extensionFound = False
                                            extensionString = ""
                                            if "." in ext:
                                                for j in extensionsList:
                                                    for k in range(0, len(extensionsList[j])):
                                                        if ext == extensionsList[j][k]:
                                                            extensionFound = True
                                                            extensionString = extensionsList[j][k]
                                                            filePath+=ext
                                                            break
                                                    if extensionFound == True:
                                                        break
                                                if extensionFound == False:
                                                    print("No such file extension exists. Try again.")
                                        fileLoc=open(f"{filePath}", "w")
                                        print(content, file=fileLoc)
                                        saveState+=1
                                        print("Changes saved.")
                                        break
                                else:
                                    fileMode = "a"
                                    print(content, file=fileLoc)
                                    fileLoc.close()
                                    print("Changes saved.")
                            elif textEntry.find("!_save_as_!")==0:
                                pass
                            else:
                                content += f"{textEntry}+\n"

                except FileNotFoundError:
                    print("The path you selected does not exist!")
                    hold=input("Press any button to continue...")
                    break
            if stopEditingCurrFile==1:
                break
            #---------------------------------Create-------------------------------------------------------------------#
            elif userInput.lower()=="open":
                pass
            elif "quit" in userInput.lower():
                print("Leaving Python Notepad...")
                quitReq = True
                break
        if quitReq==True:
            break
    return 0

menu()