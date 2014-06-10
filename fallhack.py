## Fallout Hacking Game
import random

#difficulty settings
wordLength = [4,7,10,13,15]
wordNumber = [5,8,10,12,14]

difficultyLevel = input("Difficulty Level (1-5): ")-1

#Checks similarity, returns number of similar letters
def checkwords(guess, correct):
    corLetters = 0
    for i in range(wordLength[difficultyLevel]):
        if guess[i]==correct[i]:
            corLetters +=1
    print str(corLetters) + " out of "+ str(wordLength[difficultyLevel]) + " correct"
    return corLetters

#Selects words of certain length from dictionary
validWords = []
wordFile = open('enable1.txt')
for line in wordFile:
    if len(line.strip())==wordLength[difficultyLevel]:
        validWords.append(line.strip())
#Selects random set of words to use in game
gameWords = []
for i in range(wordNumber[difficultyLevel]):
    gameWords.append(random.choice(validWords))
#Selects one word as correct answer
correctWord = random.choice(gameWords)

#Iterates for the four guesses
for i in range(4):
    for word in gameWords:
        print word
    guess = raw_input("Guess? ("+str(4-i)+" left) ")
    nCorrect = checkwords(guess, correctWord)
    if nCorrect == wordLength[difficultyLevel]:
        print("You win!")
        break
