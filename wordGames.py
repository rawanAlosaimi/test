import random 


# function of get Random Word
def getRandomWord():
    words = ["pizza", "cheese", "apples", "ckake", "pasta", "orange"]
    word = words[random.randint(0, len(words)-1)]
    return word 

# function of show Word
def showWord(word):
    for character in word:
        print(character, " ", end="")

    print("")


# function of get Guess:
def getGuess():
    print("Enter a letter:")
    return input()


# function of process Letter
def processLetter(letter, word, blankedWord):
    result = False

    for i in range(0, len(word)):
        if word[i] == letter:
            result = True
            blankedWord[i] = letter

    return result

# function of printStrikes
def printStrikes(numberOfStrikes):
    for i in range(0, numberOfStrikes):
        print("X ", end="")
    print("")    
    
    
# function of play Word Game
def playWordGame():
    strikes = 0
    maxStrikes = 3
    playing = True
    
    word = getRandomWord()
    blankedWord = list("_" * len(word))


    while playing:

        showWord(blankedWord)
        letter = getGuess()
        found = processLetter(letter, word, blankedWord) 

        if not found:
            strikes +=1
            printStrikes(strikes)

        if strikes >= maxStrikes:
            playing = False


        if not "_" in blankedWord:
            playing = False

    if strikes >= maxStrikes:
        print("Loser!")

    else:
        print("Winner!")


print("Game started")

playWordGame()

print("Game over")
