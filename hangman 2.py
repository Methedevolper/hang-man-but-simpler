import time

name = input("what is your name?")
print("Hello," + name)
print(" ")
time.sleep(1)
print("Start Playing ...")
time.sleep(0.2)
word = "centeral proccesing unit"
guesses = ""
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Yaaahhhh, You WON!")
        break
    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("You Guessed Wrong")
        print("You have only", + turns, "left")

        if turns == 0:
            print("You loose")

