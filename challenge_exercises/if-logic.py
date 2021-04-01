#!/usr/bin/env python3

# to initialize the round
roundCount = 0

# the while loop for the golf quiz
while True:
    roundCount += 1

    print("How many major championships has Tiger Woods won during his illustrious career?")
    print("How many total PGA tour wins does Tiger Woods have?\n")
    answer = input("Your answer to the first question:  \n")
    answer2 = input("Your answer to the second question: \n")

    if str(answer) == "" and str(answer2) == "":
        print("You did not enter anything, dummy!\n")

    elif answer == "15" and answer2 == "82":
        print("That is the correct! Tiger Woods is the GOAT!!")
        break

    if roundCount == 3:
        print("Sorry you have failed the most important test in your life!!")
        break

    else:
        print("Sorry that is incorrect, try again!\n")
