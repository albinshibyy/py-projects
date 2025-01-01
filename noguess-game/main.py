### SIMPLE CLI NUMBER GUESSING GAME (PY)

import random
import time
import sys
import os
# loading section
def loading():
    print("-")
    time.sleep(.3)
    print("--")
    time.sleep(.3)
    print("---")
    time.sleep(.3)
    print("----")
    time.sleep(.3)
    print("-----")
    time.sleep(.3)
# clearing terminal history in wintows / mac / linux
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
        os.system('doskey /history')
    else:  # Unix/Linux/Mac
        os.system('clear')
        os.system('history -c')
    print("----------")
# exiting section
def exiter():
    choice = input("Do you want to play another round or exit (y/yes) | (n/no) : ")
    if choice in ("no","n","exit","nn","nnn"):
        print("You have choose  to exit.")
        clear_terminal()
        print("Calculating all data")
        loading()
        print(f"UR MAX SCORE IS {score}.")
        print("--> this data will not be saved <-")
        print("Bye, This game will now exit")
        print("EXITING...")
        os.system('kill $PPID')
        os.system('exit')
        os._exit(0)
        sys.exit()
    else:
        loading()
        clear_terminal()
        print("You will now continue to the next round. ALL THE BEST")
        print("----------")

### main section
name = input("Hello user,\nPlease enter your name: ")
print(f"Hey {name} welcome to the game,")
print("This is a number guessing game.")
print("Introduction:")
print("please enter numbers or that round will reset \n scores are enabled \n Done")
print("Let's begin, Good Luck")
print("----------")
loading()
score = 0
error = 0
while True:
    try:
        norange = int(input("Enter the range of guessing no: (10, 50, 100) : "))
        chances = int(input("Enter the no: of chances you need (5, 7, 10) : "))
        print("Choosing the secret number ###!")
        loading()
        print("Secret number decided! Gd Luck")

        randomno = random.randrange(norange)
        print(randomno)
        guess_count = 0
        flag = 0
        round = 0
        while guess_count < chances:
            u_guess = int(input("Enter your guess : "))
            guess_count += 1
            round += 1

            if u_guess == randomno:
                clear_terminal()
                print(f"CONGRATS, {randomno} IS THE CORRECT ANSWER.")
                print("UR SCORE JUST INCREASED")
                score += 1
                flag = 1
                print(f"You have found the answer in the {round} round.")
                print(f"Your current score is {score}. Good Luck Playing")
                print("----------")
                break
            elif u_guess < randomno:
                print("Your guess is too less.")
            elif u_guess > randomno:
                print("Your guess is too high.")
            else:
                print("Error occured")
    except ValueError:
        error += 1
        if error > 2:
            clear_terminal()
            print("Frequent mistakes detected...!!!")
            exiter()
        print(">----------")
        print("ENTER AN INTEGER DIGIT (EG:0-9)")
        print("THIS ROUND WILL NOW BEGIN FROM THE START")
        print(">----------")
        continue
# checking for failed ... bla bla bla
    if flag == 0:
        clear_terminal()
        print("Sorry! Maximum chances reached")
        print(f"{randomno} is the correct answer.")
        print("You have failed in this round")
        print(f"Your current score is {score}. Good Luck Playing")
        print("----------")

    exiter()
