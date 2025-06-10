import random

print("This is the number guessing game \nNumber if guesses is 7. Lets start")

high = int(input("Give the Highest number:"))
low = int(input("Give the Lowest number:"))

print(f"Guess the number between {low} and {high}")

num = random.randint(low,high)
chances = 7
guesses = 0

while guesses < chances :
    guesses += 1
    guess = int(input("Guess the number: "))

    if guess == num:
        print(f"Correct.It is {num}. You did it in {guesses} guesses.")
        break

    elif guesses >= chances and guess != num:
        print(f"The correct number is {num}. \nBetter luck next time.")
        break

    elif guess > num :
        print(f"you guessed to high. Number of guesses {guesses}")

    elif guess < num :
        print(f"You guessed to low. Number of guesses {guesses}")