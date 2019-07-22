import random

# A list of potential words
potential_words = ["example", "words", "someone", "can", "guess", "fire", "hello", "world"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

#Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = list(word) # TIP: the number of letters should match the word
#print(current_word)

# Some useful variables
guesses = [] # holds all previously guessed letters
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ").lower()
    # checking that guess is a single letter and check if the current guess has not been previously guessed
    if guess.isalpha() and len(guess) == 1 and guess not in guesses:
        #guess is a single letter and is new
        guesses.append(guess)
        print(guesses)
        if guess in current_word:
            print("You guesses a letter correctly!")
            #our guess is right
        else:
            #our guess is wrong
            fails += 1
            print("You guessed incorrectly!")
    else:
        #invalid input
        print(f"Invalid Answer:{guess}")
    print("You have " + str(maxfails - fails) + " tries left!")

    #display the status of our word
    display = ""
    winning = ""
    for i in current_word:
        if i in guesses:
            display += i + " "
            winning += i
            #print(i)
        else:
            display += "_ "
            #print("_ ")
    print(display)
    if winning == word:
        print("You won!")
        exit(0)
print(f"You have lost, the word was {word}")
