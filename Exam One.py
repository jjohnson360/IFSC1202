from random import randint
name = input("What is your name? ")
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
print("You have 5 gusses. ")
number = randint(1, 20)

for i in range(1, 6):
    guess = int(input("Take a guess" + ": "))

    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Good job, " + name + "! You guessed the number in " + str(i) + " guesses.")
        break

if guess != number:
    print("Nope, " + name + ". The number I was thinking of was " + str(number))
