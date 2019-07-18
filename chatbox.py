# --- Define your functions below! ---
import random
def greetingFunction():
    print("---------------------------")
    print("Greetings!")
def hangman_game(game_choice):
    if game_choice == "hangman":

        potential_words = ["example", "words", "someone", "can", "guess", "fire", "hello", "world"]
        word = random.choice(potential_words)
        word = word.lower()
        current_word = list(word)
        guesses = []
        maxfails = 7
        fails = 0
        while fails < maxfails:
            guess = input("Guess a letter: ").lower()
            if guess.isalpha() and len(guess) == 1 and guess not in guesses:
                guesses.append(guess)
                print(guesses)
                if guess in current_word:
                    print("You guesses a letter correctly!")
                else:
                    fails += 1
                    print("You guessed incorrectly!")
            else:
                print(f"Invalid Answer:{guess}")
            print("You have " + str(maxfails - fails) + " tries left!")
            display = ""
            winning = ""
            for i in current_word:
                if i in guesses:
                    display += i + " "
                    winning += i
                else:
                    display += "_ "
            print(display)
            if winning == word:
                print("You won!")
                exit(0)
        print(f"You have lost, the word was {word}")
    else:
        aRandomNumber = random.randint(1,20)
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
def respondToUser(userAnswer):
    if(userAnswer == "good"):
        print("I am happy to hear, I'm good too")
    if(userAnswer == "bad"):
        print("I'm sorry, How can I help?")
def question1(ans1):
    if(ans1 == "nice" or "sunny"):
        print("Nice weather! I am so glad!")
    else:
        print("That's bad :(")

def question2(ans2):
    if(ans2 == "o"):
        print("I like oranges too! yeah!")
    if(ans2 == "s"):
        print("I like strawberries too! yeah!")
def question3(ans3):
    if (ans3 == "cats"):
        print("I like cats too!")
    if (ans3 == "dogs"):
        print("I like dogs too!")
def question4(ans4):
    print(f"I like {ans4} too!")

def main():
  while True:
    greetingFunction()
    user_input = input("How are you today? Good or bad?")
    respondToUser(user_input)
    q1 = input("How is the weather today?")
    question1(q1)
    q2 = input("Which one you like more? Strawberries or Oranges? Enter s or o.")
    question2(q2)
    q3 = input("Do you like cats or dogs?")
    question3(q3)
    q4 = input("What kind of music you like? ")
    question4(q4)
    q5 = input("Do you want to play a game? Enter yes or no.")
    if q5 == "yes":
        game_choice = input("Do you want to play hangman or guess a number? Enter hangman or number")
        if game_choice == "hangman" or "number":
            hangman_game(game_choice)
    else:
        print("You are so boring...")

if __name__ == "__main__":
  main()
