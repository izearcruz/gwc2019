from random import*
aRandomNumber = randint(1,20)
#Creates a variable that holds the number of tries a user has
trial = 3
while trial>0:
    guess = input("Guess a number between 1 and 20 (inclusive)")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        trial -= 1
        guess = int(guess)
        if (aRandomNumber == guess):
            print("Your number is the correct one! Congratulations!")
            break
        elif (aRandomNumber < guess):
            print("Your number is too high! Try again")
        else:
            print("Your number is too low! Try again!")
#hello
