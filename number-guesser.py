import random

top_range = input("Type a Number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
else:
    print("Please Type a number next time.")
    quit()

ran_num = random.randint(0, top_range)
no_guess=0

while True:
    no_guess += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please Type a number next time. ")
        continue

    if user_guess == ran_num:
        print("Well Done! You've guessed it correct! ")
        break

    else:
        if user_guess > ran_num:
            print("You were above the number! ")
        else:
            print("You were below the number! ")

print("You got it in",no_guess, "guesses")

