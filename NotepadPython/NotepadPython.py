import os, pyperclip

if os.name=="nt":
    clearCommand="cls"
    forbiddenNames=["con", " nul", "prn", "aux", "com1", "com2", "com3", "com4", "com5", "com6", "com7", "com8", "com9", "lpt1", "lpt2", "lpt3", "lpt4", "lpt5", "lpt6", "lpt7", "lpt8", "lpt9",\
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
    def OpenSourcePath(self, openWriteMode=False):
        if openWriteMode==True:
            try:
                self.openSourceWrite=open(self.filePath, "w")
            except:
                self.generatedErrors = True
                print("This path is unavailable!")
        try:
            self.openSourceRead=open(self.filePath, "r")
        except:
            self.generatedErrors = True
            print("This path is unavailable")
    def UnloadFileData(self):
        self.openSourceRead.close()
        del self.openSourceRead
    def __init__(self,fileName,path, openingFile=False):
        if openingFile==True:
            self.tempFilePath="None"
            self.openingFile=openingFile
            self.saveState=1
        else:
            self.tempFilePath=path
            self.openingFile=openingFile
            self.saveState=0
        self.fileName=fileName
        self.filePath=path
    def SaveFile(self,saveAs=False, saveState=0, contents=""):
        if saveState==0 or saveAs==True:
            originalFileName = self.fileName; originalFilePath = self.filePath
            fileExists=False; rewrite=False; saveLoc=""; isItWin11=False
            if os.path.exists(f"C:\\Users\\{os.getlogin()}\\OneDrive\\Desktop"):
                isItWin11=True
            def ProcessFileName():
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
                            break
                        else:
                            print("Chosen file name is invalid. Forbidden names/symbols detected.")
                            continue
                return newFilename
            self.fileName=ProcessFileName()
            if "!_skip_!" in self.fileName:
                #save the original file name
                self.fileName=originalFileName
            def ProcessSaveLocation():
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
                            if isItWin11==True:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\OneDrive\\Pictures"
                            else:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\Pictures"
                            validPath=True
                        elif saveLoc.lower()=="videos":
                            saveLoc = f"C:\\Users\\{os.getlogin()}\\Videos"
                            validPath=True
                        elif saveLoc.lower()=="documents":
                            if isItWin11==True:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\OneDrive\\Documents"
                            else:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\Documents"
                            validPath=True
                        elif saveLoc.lower()=="users":
                            saveLoc = f"C:\\Users\\{os.getlogin()}"
                            validPath=True
                        elif saveLoc.lower()=="desktop":
                            if isItWin11==True:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\OneDrive\\Desktop"
                            else:
                                saveLoc = f"C:\\Users\\{os.getlogin()}\\Desktop"
                            validPath=True
                    if validPath==True:
                        break
                return saveLoc
            saveLoc=ProcessSaveLocation()
            def ProcessFileTypeExtChoice(saveLoc,fileName):
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
                            saveLoc+=f"\\{fileName}{fileType}"
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
                return saveLoc
            saveLoc=ProcessFileTypeExtChoice(saveLoc, self.fileName)
            while True:
                cancelAction=False
                if os.path.exists(saveLoc) and rewrite==False:
                    fileExists = True
                    print("\nA file with this name already exists. Do you want to change the save data or rewrite the file in this location?\nPossible options: 'Change save data', 'Rewrite', 'Cancel'")
                    while True:
                        userResponse=input()
                        if userResponse.lower()=="rewrite":
                            rewrite=True
                            break
                        elif userResponse.lower()=="change save data":
                            changeName=False; changeExt=False; changeLoc=False
                            print("Possible options:\n'Change File Name', 'Change Type/Extension, Change Save Location'")
                            while True:
                                userResponse=input()
                                if userResponse.lower()=="change file name":
                                    changeName=True
                                    break
                                elif userResponse.lower()=="change type" or userResponse.lower()=="change extension":
                                    changeExt=True
                                    break
                                elif userResponse.lower()=="change save location":
                                    changeLoc=True
                                    break
                            if changeName==True:
                                saveLoc=saveLoc.split("\\")
                                currentExt=saveLoc[-1].split("."); currentExt="."+currentExt[-1]
                                del saveLoc[-1]; saveLoc='\\'.join(saveLoc)
                                self.fileName = ProcessFileName()
                                saveLoc+=f"\\{self.fileName}{currentExt}"
                                break
                            elif changeExt==True:
                                saveLoc=saveLoc.split("\\"); del saveLoc[-1]; saveLoc='\\'.join(saveLoc)
                                saveLoc = ProcessFileTypeExtChoice(saveLoc,self.fileName)
                                break
                            elif changeLoc==True:
                                saveLoc=saveLoc.split("\\")
                                currentExtension=saveLoc[-1].split("."); currentExtension="."+currentExtension[-1]
                                saveLoc=ProcessSaveLocation()
                                saveLoc+="\\"+self.fileName+currentExtension
                                break
                        elif userResponse.lower() == "cancel":
                            cancelAction = True
                            break
                    if cancelAction==True:
                        break
                else:
                    break
            if fileExists==False or rewrite==True:
                del originalFilePath; del originalFileName
                self.UnloadFileData()
                self.filePath=saveLoc
                self.OpenSourcePath(openWriteMode=True)
                self.openSourceWrite.write("\n".join(contents))
                self.openSourceWrite.flush()
                self.openSourceWrite.close()
                if self.saveState==0:
                    if os.path.exists(self.tempFilePath):
                        os.remove(self.tempFilePath)
                        self.tempFilePath = "None"
                    self.saveState += 1
                print(f"File {self.fileName} has been saved!")
            else:
                print("Saving cancelled")
                self.fileName=originalFileName; self.filePath=originalFilePath
                return False
        elif saveState==1 or saveState==2:
            self.OpenSourcePath(openWriteMode=True)
            self.openSourceWrite.write('\n'.join(contents))
            self.openSourceWrite.flush()
            self.openSourceWrite.close()
            if saveState==2:
                self.saveState-=1
            print("Changes Saved!")

    def Edit(self):
        quitRequest = False; returnRequest = False; text=[]
        if self.saveState==0:
            self.OpenSourcePath(openWriteMode=True)
        else:
            self.OpenSourcePath()
            if self.generatedErrors==True:
                print("The file could not be found!")
                hold = input("Press ENTER to continue")
                return -1
        if self.openingFile==True:
            self.openingFile=False
            text=self.openSourceRead.read()
            text = text.split("\n")
        while True:
            os.system(clearCommand)
            outputName=f"{' '*35}{self.fileName}"
            self.filePath=self.filePath.split("\\")
            if "." in self.filePath[-1]:
                ext=self.filePath[-1].split(".")
                ext=ext[-1]
                self.filePath='\\'.join(self.filePath)
                outputName+=f".{ext}"
            else:
                self.filePath = '\\'.join(self.filePath)
            if self.saveState==0 or self.saveState==2:
                outputName+="*"
            print(f"{'-' * 100}")
            print(outputName)
            print(f"{'-' * 100}")
            if len(text)!=0:
                for k in range(0,len(text)):
                    print(f"{k+1}|{'    '}{text[k]}")
            if returnRequest==True:
                returnRequest=False
            while True:
                userInput=input()
                if userInput.find("!_save_!")==0:
                    self.OpenSourcePath(openWriteMode=True)
                    if self.SaveFile(saveState=self.saveState,contents=text)==False:
                        text=[]
                    break
                elif userInput.find("!_save_as_!")==0:
                    self.SaveFile(saveAs=True, contents=text)
                    break
                elif userInput.find("!_quit_!")==0:
                    if self.saveState==0 or self.saveState==2:
                        print("You have unsaved changes!\n")
                        print(f"Do you want to save this file?[Y/N/Return]")
                        while True:
                            userChoice=input("- ")
                            if userChoice.lower()=="y" or userChoice.lower()=="yes":
                                self.SaveFile(saveState=self.saveState, contents=text)
                                del text; del userInput
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
                elif userInput.find("!_edit_row_!")==0:
                    print("Which row do you want to edit?")
                    while True:
                        rowN=input()
                        if rowN.isnumeric()==False:
                            print("Please enter row number!")
                            continue
                        else:
                            rowN=int(rowN)-1
                            if rowN>len(text)-1:
                                print("Invalid row.")
                                continue
                            else:
                                print(f"{rowN+1} |    {text[rowN]}")
                                print("(You can leave empty to remove this row)\n(The row has been copied. You can paste it and edit part of it.)")
                                pyperclip.copy(text[rowN])
                                rewriteRow=input()
                                if len(rewriteRow)!=0:
                                    text[rowN]=rewriteRow
                                else:
                                    del text[rowN]
                                self.saveState=2
                                returnRequest=True
                                break
                else:
                    text.append(userInput)
                    if self.saveState==1:
                        self.saveState+=1
                    break
                if returnRequest==True or quitRequest==True:
                    break
            if quitRequest==True:
                os.system(clearCommand)
                self.UnloadFileData()
                if os.path.exists(self.tempFilePath):
                    os.remove(self.tempFilePath)
                break

def main():
    #check if config file exists, otherwise create one and fill with default values
    # configPath=str(os.path); configPath=configPath.split("'"); configPath=configPath[-2]; configPath=configPath.split("\\"); del configPath[-1]
    # configPath='\\'.join(configPath); configPath+="notepadConf.conf"
    # if not os.path.exists(configPath):
    #     createConfig=open(configPath,"w")
    #     configData="Autosaving: OFF\nAutosave Time: 15 minutes\nLanguage: EN"
    #     createConfig.write(configData)
    #     createConfig.flush()
    quitRequest=False
    while True:
        print(f"{' '*20}Notepad Python 0.1\n")
        print("'Create' - to create a new file | 'Open' - to open file\n\n'Quit' - to quit the program | License - to see more about the license\n\n'Commands' - to see more about available commands")
        while True:
            userInput=input("- ")
            if userInput.lower()=="create":
                fileName="New file"
                initP = str(os.path); initP = initP.split("'")
                initP = initP[-2]; initP = initP.split("\\"); del initP[-1]; initP = '\\'.join(initP); initP+=fileName
                cFile=File(fileName,initP)
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
                    oFile.Edit()
                    del oFile
                    break
            elif userInput.lower()=="quit":
                quitRequest=True
                break
            elif userInput.lower()=="license":
                print(f"\n{' '*15}GNU GENERAL PUBLIC LICENSE\n{' '*15}Version 3, 29 June 2007\n{' '*15}Copyright (C) 2022  Eduard Velkov\
    \n\nThis program is free software: you can redistribute it and/or modify\
    \nit under the terms of the GNU General Public License as published by\
    \nthe Free Software Foundation, either version 3 of the License, or\
    \n(at your option) any later version.\
    \nThis program is distributed in the hope that it will be useful,\
    \nbut WITHOUT ANY WARRANTY; without even the implied warranty of\
    \nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
    \nGNU General Public License for more details.\
    \nYou should have received a copy of the GNU General Public License\
    \nalong with this program.  If not, see <https://www.gnu.org/licenses/>.")
                proceed=input()
                os.system(clearCommand)
                break
            elif userInput.lower()=="commands":
                print("1. Editing Commands\n")
                while True:
                    userChoice=input()
                    if userChoice=="1":
                        print(f"{' '*15}Editing commands:\n\
        '*Commands while editing a file usually have the following format - !_command_!.'\n\
        !_save_! - to save the file;\n \
        !_save_as_! - save the file with different name, location or type\n\
        !_edit_row_! - select row number and edit the text there\n \
        !_quit_! - leave editing mode\n\
        !_skip_! - skip actions at specific stages. You will be notified when you can use it.\n")
                        hold=input()
                        break
                    elif "/return" in userChoice.lower():
                        break
                    else:
                        continue
                os.system(clearCommand)
                break
            # elif userInput.lower()=="configure":
            #     rConfig=open(configPath,"r")
            #     readConfigData=rConfig.read()
            #     print(f"Current settings applied:\n\n{readConfigData}\nWrite the name of the option you'd like to change or 'Return' to go back")
            #     readConfigData=readConfigData.split("\n")
            #     opt=input()
            #     if "return" in opt:
            #         break
        if quitRequest==True:
            break
main()
