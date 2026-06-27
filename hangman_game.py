# this is a Hangman game 
# you have to guess latters of word to find secret word
import random
words = ["APPLE","TIGER","PYTHON","LAPTOP","ALI","BAT","CAT"]
secret= random.choice(words)
for i in secret:
    print(" - " ,end="")
print("")

guessed_letter = []
lives = 6
while True:
    correct = input(" Guess the LETTER :").upper()
    guessed_letter.append(correct)
    if correct in secret:
        print("CORRECT")
        for latter in secret:
            if latter in guessed_letter:
                print(latter,end="")
            else:
                print(" - ", end="")
        won = True
        for latter in secret:
            if latter not in guessed_letter:
                won = False
                break
        if won:
            print(" CORRECT, YOU WON!")
            break
           
    else:
        lives = lives - 1
        print("WRONG")
        print("Lives left",lives)
    if lives == 0:
        print("GAME OVER: ")
        print("The word was : ", secret)
        break
