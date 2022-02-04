import os, pyperclip

if os.name=="nt":
    forbiddenNames=["con","nul","prn","aux","com1","com2","com3","com4","com5","com6","com7","com8","com9","lpt1","lpt2","lpt3","lpt4","lpt5","lpt6","lpt7","lpt8","lpt9",\
                    "\\","/","<",">",":","\"","|","?","*"]
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

class File:
    readyToClose=False; generatedErrors=False
    def OpenSourcePath(self):
        try:
            self.openSourceWrite=open(self.filePath, "a")
        except:
            print("This path is unavailable!")
        try:
            self.openSourceRead=open(self.filePath, "r")
        except:
            print("This path is unavailable")
    def UnloadFileData(self):
        self.openSourceWrite.close(); self.openSourceRead.close()
        del self.openSourceWrite; del self.openSourceRead
    def __init__(self,fileName,path, openingFile=False):
        if openingFile==True:
            self.saveState=1
        else:
            self.saveState=0
        self.fileName=fileName
        self.filePath=path
    def SaveFile(self,saveAs=False, saveState=0, contents=""):
        if saveState==0 or saveAs==True:
            while True:
                validName = True
                if saveAs==True:
                    print("(!_skip_! to skip if you wish to keep the current name)")
                newFilename = input("Enter file name: ")
                if "!_skip_!" in newFilename.lower() and saveAs==True:
                    break
                else:
                    for k in range(0,len(forbiddenNames)):
                        if forbiddenNames[k] in newFilename.lower():
                            validName=False
                    if validName == True:
                        self.fileName=newFilename
                        break
                    else:
                        print("Chosen file name is invalid. Forbidden names/symbols detected.")
                        continue
            while True:
                validPath=False
                saveLoc = input("(You can choose a system folder like 'Documents','Downloads'...or enter absolute file path)\nWhere do you want to save the file? -")
                if ":\\" in saveLoc:
                    if os.path.exists(saveLoc)==True:
                        validPath=True
                    else:
                        print("Path is invalid!")
                        continue
                else:
                    if saveLoc.lower()=="downloads":
                        saveLoc=f"C:\\Users\\{os.getlogin()}\\Downloads"
                        validPath==True
                    elif saveLoc.lower()=="pictures":
                        saveLoc = f"C:\\Users\\{os.getlogin()}\\Pictures"
                        validPath=True
                    elif saveLoc.lower()=="videos":
                        saveLoc = f"C:\\Users\\{os.getlogin()}\\Videos"
                        validPath=True
                    elif saveLoc.lower()=="documents":
                        saveLoc = f"C:\\Users\\{os.getlogin()}\\Documents"
                        validPath=True
                    elif saveLoc.lower()=="users":
                        saveLoc = f"C:\\Users\\{os.getlogin()}"
                        validPath=True
                    elif saveLoc.lower()=="desktop":
                        saveLoc = f"C:\\Users\\{os.getlogin()}\\Desktop"
                        validPath=True
                if validPath==True:
                    break
            while True:
                validType=False
                fileType=input("Enter file type/extension: ")
                if "." in fileType:
                    for j in extensionsList:
                        for k in range(0,len(extensionsList[j])):
                            if extensionsList[j][k]==fileType:
                                validType=True
                                break
                        if validType==True:
                            break
                    if validType==True:
                        saveLoc+="\\"+self.fileName+fileType
                        break
                else:
                    for j in extensionsList:
                        if j==fileType:
                            fileType="\\"+self.fileName+extensionsList[j][0]
                            validType=True
                            break
                    if validType==True:
                        saveLoc+=fileType
                        break
            self.UnloadFileData()
            self.filePath=saveLoc
            self.OpenSourcePath()
            self.openSourceWrite.write(contents)
            self.openSourceWrite.flush()
            if saveAs==True:
                print(f"File {self.fileName} has been saved!")
            else:
                print("File has been saved!")
        elif saveState==1:
            self.openSourceWrite.write(contents)
            self.openSourceWrite.flush()
            print("Changes Saved!")

    def Edit(self):
        quitRequest = False; returnRequest = False
        while True:
            self.OpenSourcePath()
            if returnRequest==False:
                fileContents=""
            outputName=f"{' '*35}{self.fileName}"
            if self.saveState==0:
                outputName+="*"
            else:
                self.filePath=self.filePath.split(".")
                ext=self.filePath[-1]; del self.filePath[-1]
                outputName+=f".{ext}"
                self.filePath=''.join(self.filePath); self.filePath+="."+ext
            print(f"{'-' * 100}")
            print(outputName)
            print(f"{'-' * 100}")
            if self.saveState!=0:
                text=self.openSourceRead.read()
                pyperclip.copy(text)
                text=text.split("\n")
                for k in range(0,len(text)):
                    print(f"{k+1}|{'    '}{text[k]}")
            elif returnRequest==True:
                text=fileContents.split("\n")
                for k in range(0,len(text)):
                    print(f"{k+1}|{'    '}{text[k]}")
                returnRequest=False
            while True:
                userInput=input()
                if userInput.find("!_save_!")==0:
                    if self.saveState == 0:
                        self.SaveFile(contents=fileContents)
                        fileContents=""; self.saveState+=1
                        break
                    else:
                        self.SaveFile(saveState=1,contents=fileContents)
                        fileContents=""
                        break
                elif userInput.find("!_save_as_!")==0:
                    self.SaveFile(saveAs=True, contents=fileContents)
                    saveState=1
                    break
                elif userInput.find("!_quit_!")==0:
                    if self.saveState==0:
                        print("You have unsaved changes!\n")
                        print(f"Do you want to save this file?[Y/N/Return]")
                        while True:
                            userChoice=input("- ")
                            if userChoice.lower()=="y" or userChoice.lower()=="yes":
                                self.SaveFile(contents=fileContents)
                                self.UnloadFileData()
                                del fileContents
                                quitRequest=True
                                break
                            elif userChoice.lower()=="n" or userChoice.lower()=="no":
                                quitRequest=True
                                break
                            elif userChoice.lower()=="return":
                                returnRequest=True
                                break
                    else:
                        quitRequest=True
                        break
                else:
                    fileContents+=userInput+"\n"
                if returnRequest==True or quitRequest==True:
                    break
            if quitRequest==True:
                if os.path.exists("C:\\Users\\EdwardV\\AppData\\Local\\Programs\\Python\\Python39\\lib\\New file"):
                    os.remove("C:\\Users\\EdwardV\\AppData\\Local\\Programs\\Python\\Python39\\lib\\New file")
                break

def main():
    quitRequest=False
    while True:
        print(f"{' '*20}Notepad Python 0.1\n")
        print("'Create' - to create a new file | 'Open' - to open new file\n'Quit' - to quit the program")
        while True:
            userInput=input("- ")
            if userInput.lower()=="create":
                fileName="New file"
                initP = str(os.path); initP = initP.split("'")
                initP = initP[-2]; initP = initP.split("\\"); del initP[-1]; initP = '\\'.join(initP); initP+=fileName
                cFile=File(fileName,initP)
                cFile.OpenSourcePath()
                cFile.Edit()
                del cFile
                break
            elif userInput.lower()=="open":
                validPath=False
                while True:
                    print("Please enter the path to the file you'd like to edit:\n")
                    usrPath=input("- ")
                    if os.path.exists(usrPath):
                        validPath=True
                        break
                    else:
                        print("File not found or path is invalid...")
                        hold=input()
                        continue
                if validPath==True:
                    fileName=usrPath.split("\\"); fileName=fileName[-1].split("."); fileName=fileName[0]
                    oFile=File(fileName,usrPath,True)
                    oFile.OpenSourcePath()
                    oFile.Edit()
                    del oFile
                    break
            elif userInput.lower()=="quit":
                quitRequest=True
                break
        if quitRequest==True:
            break
main()
