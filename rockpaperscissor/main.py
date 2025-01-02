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

# clearing terminal history in windows / mac / linux
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
        os.system('doskey /history')
    else:  # Unix/Linux/Mac
        os.system('clear')
        os.system('history -c')
    print("----------")

# exiting section
def exiter(score):
    choice = input("Do you want to play another round or exit (y/yes) | (n/no) : ")
    if choice in ("no","n","exit","nn","nnn"):
        print("You have chosen to exit.")
        clear_terminal()
        print("Calculating all data")
        loading()
        print(f"The current scores are: \nUser: {scoreu}\nComputer: {scorec}\nTie: {tie}")
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
        print(f"The current scores are: \nUser: {scoreu}\nComputer: {scorec}\nTie: {tie}")
        print("----------")

scoreu = 0
scorec = 0
tie = 0
error = 0
print("Introduction:")
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
print("----------")
startt = input("Can we begin.?")
loading()
clear_terminal()
print("---------------")
name = input("Hello user,\nPlease enter your name: ")
print("----------")
print(f"Hey {name} welcome to the game,")
print("Let's begin the game")
if __name__ == "__main__":
    while True:
        try:
            print("Enter your choice: ")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissor")

            u_choice = int(input("Enter your choice: "))
        except ValueError:
            error += 1
            if error > 1:
                clear_terminal()
                print("Frequent mistakes detected...!!!")
                exiter(scoreu)
            print(">----------")
            print("ENTER AN INTEGER DIGIT (EG:1-3)")
            print("THIS ROUND WILL NOW BEGIN FROM THE START")
            print(">----------")
            continue
        while u_choice > 3 or u_choice < 1:
            u_choice = int(input('Enter a valid choice please: '))

        if u_choice == 1:
            u_choice_name = 'Rock'
        elif u_choice == 2:
            u_choice_name = 'Paper'
        else:
            u_choice_name = 'Scissors'

        print('User choice is:', u_choice_name)
        print("Now it's Computer's Turn...")
        c_choice = random.randint(1, 3)

        if c_choice == 1:
            c_choice_name = 'Rock'
        elif c_choice == 2:
            c_choice_name = 'Paper'
        else:
            c_choice_name = 'Scissors'

        print("Computer choice is:", c_choice_name)
        print(u_choice_name, 'vs', c_choice_name)

        if u_choice == c_choice:
            result = "DRAW"
        elif (u_choice == 1 and c_choice == 2) or (c_choice == 1 and u_choice == 2):
            result = 'Paper'
        elif (u_choice == 1 and c_choice == 3) or (c_choice == 1 and u_choice == 3):
            result = 'Rock'
        elif (u_choice == 2 and c_choice == 3) or (c_choice == 2 and u_choice == 3):
            result = 'Scissors'

        if result == "DRAW":
            print("<== It's a tie! ==>")
            tie += 1
        elif result == u_choice_name:
            print("<== User wins! ==>")
            scoreu += 1
        else:
            print("<== Computer wins! ==>")
            scorec += 1

        exiter(scoreu)
