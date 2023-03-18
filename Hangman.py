import random
import sys

def readWordList(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Remove any whitespace characters from the beginning and end of each line
    wordList = [line.strip() for line in lines]
    return wordList

def generateWord():

    wordList = readWordList("wordlist.txt")
    randomNumber = random.randint(0, len(wordList) - 1)
    randomWord = wordList[randomNumber]

    guessString = ""
    # Create a string of underscores equal to word length
    wordLength = len(randomWord)
    for length in range(wordLength):
        guessString += "_"
    return guessString, randomWord

def findAll(aStr, sub):
    start = 0
    while True:
        strLen = len(aStr)
        subLen = len(sub)
        subIndices = []
        for i in range(strLen - subLen+1):
            if aStr[i:i + subLen] == sub:
                subIndices.append(i)
        if len(subIndices) >= 1:
            return subIndices
        else:
            return -1

def mainGame(guessString, randomWord):
    mistakes=0
    gameRunning = True
    while gameRunning == True:
        print(guessString)
        userGuess = input(f"Enter a character or the word. You have {7-mistakes} mistakes remaining. ").lower()
    
        if len(userGuess) == 1:
            guessInWord = findAll(randomWord,userGuess)
        
            if guessInWord == -1:
                print(f"{userGuess} is not present in the word! ")
                mistakes += 1

                if mistakes >= 7:
                    gameRunning = False

                else:
                    gameRunning = True

            # If the character is in the code this will run
            # This inserts the character into the guess string at the correct index
            else:
                for i in guessInWord:
                    position = i
                    newCharacter = userGuess
                    guessString = guessString[:position] + newCharacter + guessString[position+1:]

                if guessString == randomWord:
                    print(f"You have guessed the word {randomWord} with {mistakes} mistakes out of 7. ")
                    gameRunning = False
                    break

        elif len(userGuess) == len(randomWord):
            if userGuess == randomWord:

                # This is just easier to do than adding another condition to break loop
                guessString = randomWord
                print(f"You have guessed the word {randomWord} with {mistakes} mistakes out of 7. ")
                gameRunning = False
                break
            else:
                print(f"{userGuess} is not the word. ")
                mistakes += 1
                if mistakes >= 7:
                    gameRunning = False
                else:
                    gameRunning = True
        else:
            print(f"Invalid input. The guess must be 1 character or the entire word ({len(randomWord)} characters long). ")

    if mistakes == 7:
        print(f"You died after too many attempts. The word was {randomWord}. ")

while True:
    results = generateWord()
    randomWord = results[1]
    guessString = results[0]
    mainGame(guessString, randomWord)
    playAgain = input("Play again? [Y/N] ").capitalize()
    if playAgain == "Y":
        True
        next
    else:
        sys.exit()
