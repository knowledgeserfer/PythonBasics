#"Guess a number" game
#Create a game that gives a player 3 attempts to guess a number
#from 1 to 10
#If the player guesses correctly then the player wins
#Otherwise the computer wins
import random
#think about pseudo code
#create number variable
numberToGuess = random.randrange(1,11)
#create counterOfAttempts variable
counterOfAttempts = 0
#create guess variable
guessOfPlayer=0
#explain the rules of the game shortly
print("Try to guess a number from 1 to 10.")
print("You have ", 3-counterOfAttempts," attempts.")

#create a while cycle and use counterOfAttempts as condition
while counterOfAttempts<3:
    #get value from player in guess variable
    guessOfPlayer = int(input("Guess a number from 1 to 10. "))
    #increase counter
    counterOfAttempts+=1
    #check if the guess is correct.
    if guessOfPlayer==numberToGuess:
        print("You have won. Congratulations.")
        print("The number was {}.".format(numberToGuess))
        break
    #if the guess is wrong write else block
    else:
        #inform that guess is wrong and how many attempts left
        print("Wrong. You have ",3-counterOfAttempts," left.")
        if counterOfAttempts==3:
            print("You are out of attempts.")
            print("You didn't guess correctly.")
            print("The number was {}.".format(numberToGuess))