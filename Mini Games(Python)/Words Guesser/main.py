import random
class AccountsData:
    AccountName=["Sec2727", "JohnDoe"]; AccountPoints=[200,300]; AccountPos=[1,2]
def ShowGuide():
    print("In this guide you will see how the game is played and how points are earned.\nIn Word Guesser you will be given a certain amount of words depending on the difficulty level you chose. The harder the difficulty the more points you are going to earn for every word you guess correctly.")
    print("For every word you will have the chance to use a tip that may help you to guess the word, but be careful! If you are playing on harder difficulty the tip you get could be wrong. So check carefully what tip you get. On easier difficulty you can rely on the tips, but you can use them only one time per game.")
    print("You will have 3 words on easy difficulty, that are going to be shorter and will often have only one hidden letter. If you chose medium difficulty you will get 5 words to guess, but two or more letters will be hidden. On hard difficulty you will get 10 words, they will be longer and will have more than 3 letter hidden.")
    print("You can lose a lot more points if you get the word wrong on hard difficulty. The amount of points you lose/earn are as follows:\n\nEasy difficulty: You earn 5 points per correctly guessed word/ You lose 10 points otherwise\nMedium difficulty: You earn 10 points per correctly guessed word/ You lose 20 points otherwise.\nHard difficulty: You earn 30 points per correctly guessed word/ You lose 60 points otherwise.\n\n")
    print("And lastly, you get 2/2/1 tries per word respectively.\nHave fun and get the 1st place in leaderboards! :)\n\n")

def StartGame(name, difficulty, wordsList):
    accountId=AccountsData.AccountName.index(name)
    totalPoints=0; failed=False
    if difficulty=="Easy":
        wordsCount=3
        range1=0.00; range2=0.94; range3=0.95; range4=1
        minWordLength=3;wordLength1=4; wordLength2=4
        winPoints=5; losePoints=10
        guessTries=2; maxHiddenLetters=1
    elif difficulty=="Medium":
        wordsCount=5
        range1 = 0.00; range2 = 0.70; range3 = 0.71; range4 = 1
        minWordLength=4; wordLength1 = 6; wordLength2 = 6
        winPoints = 10; losePoints = 20
        guessTries = 2; maxHiddenLetters=3
    elif difficulty=="Hard":
        wordsCount=7
        range1 = 0.00; range2 = 0.70; range3 = 0.71; range4 = 1
        minWordLength = 6; wordLength1 = 9; wordLength2 = 9
        winPoints = 30; losePoints = 60
        guessTries = 1; maxHiddenLetters=3
    print("Choosing words . . .")
    shortWords=[]
    for k in range(0,len(wordsList)):
        if len(wordsList[k])<wordLength2+1:
            shortWords.append(wordsList[k])
    chosenWords=[]; k=0
    while k<wordsCount:
        chance=round(random.random(),2)
        if range1<=chance<=range2:
            #length=len(shortWords)-1
            while True:
                randomWord=round(random.random()*len(shortWords)-1)
                if minWordLength<=len(shortWords[randomWord])<wordLength1:
                    chosenWords.append(shortWords[randomWord])
                    del shortWords[randomWord]
                    break
                else:
                    continue
        elif range3<=chance<=range4:
            while True:
                randomWord=round(random.random()%len(shortWords))
                if len(shortWords[randomWord])==wordLength2:
                    chosenWords.append(shortWords[randomWord])
                    del shortWords[randomWord]
                    break
                else:
                    continue
        k+=1
    print("Hiding letters . . .\n\n\n")
    #print(chosenWords)
    wordN=1
    for k in range(0,len(chosenWords)):
        originalWord=chosenWords[k]; triesPerWord=guessTries
        currentWord=[]; hideLetters=maxHiddenLetters; h=0
        for j in range(0,len(chosenWords[k])):
            currentWord.append(chosenWords[k][j])
        if maxHiddenLetters>1 and difficulty!="Hard":
            hideChance=round(random.random())
            if 0.01<hideChance:
                hideLetters-=1
        while h<hideLetters:
            hideRandLetter=round(random.random()*len(currentWord)-1)
            if currentWord[hideRandLetter]=="_" or hideRandLetter==0:
                continue
            else:
                currentWord[hideRandLetter]="_"
                h+=1
        currentWord="".join(currentWord); currentWinningPts=winPoints; currentLosePts=losePoints
        print(f"\n\nWord number №{wordN}:\n")
        print(currentWord)
        while triesPerWord!=0:
            answer=input()
            if answer==originalWord:
                print("Yes, that's correct answer!")
                totalPoints+=winPoints
                wordN+=1
                break
            else:
                triesPerWord-=1
                if triesPerWord==0:
                    failed=True
                    totalPoints-=currentLosePts
                    if totalPoints<0:
                        totalPoints=0
                    break
                print(f"No, that's not the word. ({triesPerWord} tries left)\nCurrent winning points have been decreased 50%")
                currentWinningPts-=currentWinningPts*0.5
                continue
        if failed==True:
            break
    if failed==False:
        print(f"You guessed all words correctly!\nEarned points={totalPoints}")
        AccountsData.AccountPoints[accountId]+=totalPoints
        UpdateAccountStats()
    else:
        print(f"You couldn't guess all the words.\nEarned points={totalPoints}")
        if totalPoints>0:
            AccountsData.AccountPoints[accountId]+=totalPoints
def UpdateAccountStats():
    k=0
    while k<len(AccountsData.AccountPoints)-1:
        if AccountsData.AccountPoints[k]<AccountsData.AccountPoints[k+1]:
            #exchange points
            temp=AccountsData.AccountPoints[k]
            AccountsData.AccountPoints[k]=AccountsData.AccountPoints[k+1]
            AccountsData.AccountPoints[k+1]=temp
            #exchange names in AccountName list
            temp=AccountsData.AccountName[k]
            AccountsData.AccountName[k]=AccountsData.AccountName[k+1]
            AccountsData.AccountName[k+1]=temp
            k=0
        else:
            k+=1
def ShowAccountStats(name):
    id=AccountsData.AccountName.index(name)
    points=AccountsData.AccountPoints[id]
    leaderboardsPos=AccountsData.AccountPos[id]
    print(f"\nName: {name}\nTotal points: {points}\nLeaderboards position: {leaderboardsPos}\n")
def main():
    #randomNum=round(random.random(),2)
    #print(randomNum)
    while True:
        name=input("Enter your name: ")
        if len(name)<2:
            print("\nUmm, I can't understand that name.\n\n")
            continue
        else:
            AccountsData.AccountName.append(name); AccountsData.AccountPoints.append(0); AccountsData.AccountPos.append(max(AccountsData.AccountPos)+1)
            break
    print(f"[Words Guesser]\n\nHey, {name}! Welcome to Words Guesser.\nWe recommend you to read the guide first, before starting the game.")
    while True:
        print("1 - Start a new game     2 - Check your account stats\n3 - Read the guide     4 - Check the leaderboards")
        option=input()
        if option=="1":
            words=["game","global","unreal","dictionary","month","bread","spices","potato","city","car","stop","tag","skip","loud","break","turn","will","power","day","way","stay","wanderer","deal","seal","bill","drill","still","spill","water","bottle","scratch","food"]
            while True:
                diff=input("Select Difficulty(Easy/Medium/Hard): ")
                if diff!="Easy" and diff!="Medium" and diff!="Hard":
                    print("\nHmm, What difficulty did you choose?\n")
                    continue
                else:
                    break
            StartGame(name, diff, words)
        elif option=="2":
            ShowAccountStats(name)
            continue
        elif option=="3":
            ShowGuide()
            continue
        elif option=="4":
            print("Leaderboard:\n")
            UpdateAccountStats()
            for k in range(0,len(AccountsData.AccountPoints)):
                accPos=AccountsData.AccountPos[k]; accName=AccountsData.AccountName[k]; accPoints=AccountsData.AccountPoints[k]
                print(f"{accPos} -- {accName} -- {accPoints}")
            print("\n")
            continue

main()
