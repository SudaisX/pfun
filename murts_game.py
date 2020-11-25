import random
import time
# declaration
RUL = 0
RLL = 0
PUL = 0
PLL = 0
SUL = 0
SLL = 0
rock = 0
paper = 0
scissors = 0


def win(user_win_count, computer_choice, user_choice):
    user_win_count[0] = user_win_count[0] + 1
    print("Computer:", humanify(computer_choice))
    time.sleep(1)
    print("Human:", humanify(user_choice))
    time.sleep(1)
    print("You scored!")
    time.sleep(1)


def draw(computer_choice, user_choice):
    print("Computer:", humanify(computer_choice))
    time.sleep(1)
    print("You:", humanify(user_choice))
    time.sleep(1)
    print("Draw.")
    time.sleep(1)


def lose(comp_win_count, computer_choice, user_choice):
    comp_win_count[0] = comp_win_count[0] + 1
    print("Computer:", humanify(computer_choice))
    time.sleep(1)
    print("Human:", humanify(user_choice))
    time.sleep(1)
    print("The computer scored!")
    time.sleep(1)


def power_func_rock(power, user_character, computer_choice, user_choice):
    if power == 'yes':
            if user_character == 1:
                print(" YOU USED SWITCHEROO! OPPONENT'S CHOICE HAS BEEN INVERTED!")
                computer_choice = 3
            elif user_character == 2:
                if user_choice == 3:
                    print(" You Lost!")
                    time.sleep(1)
                    print("BUT WAIT!")
                    time.sleep(1)
                    print("YOU USED SIKE!! you will have your option chosen again! RANDOMLY!")
                    user_choice = random.randint(1, 3)
            elif user_character == 3:
                print("You used Mystery Power....")


def score_func_rock(user_choice, computer_choice, user_win_count, comp_win_count):
        if user_choice == 1:
            draw(computer_choice, user_choice)
        elif user_choice == 2:
            win(user_win_count, computer_choice, user_choice)
        elif user_choice == 3:
            lose(comp_win_count, computer_choice, user_choice)


def power_func_paper(power, user_character, computer_choice, user_choice):
        if power == 'yes':
            if user_character == 1:
                print(" YOU USED SWITCHEROO! OPPONENT'S CHOICE HAS BEEN INVERTED!")
                computer_choice = 3
            elif user_character == 2:
                if user_choice == 1:
                    print(" You Lost!")
                    time.sleep(1)
                    print("BUT WAIT!")
                    time.sleep(1)
                    print("YOU USED SIKE!! you will have your option chosen again! RANDOMLY!")
                    user_choice = random.randint(1, 3)
            elif user_character == 3:
               print("You used Mystery Power....")

def score_func_paper(user_choice, computer_choice, user_win_count, comp_win_count):
        if user_choice == 1:
            lose(comp_win_count, computer_choice, user_choice)
        elif user_choice == 2:
            draw(computer_choice, user_choice)
        elif user_choice == 3:
            win(user_win_count, computer_choice, user_choice)

def power_func_scissors(power,user_character, computer_choice, user_choice):
        if power == 'yes':
            if user_character == 1:
                print(" YOU USED SWITCHEROO! OPPONENT'S CHOICE HAS BEEN INVERTED!")
                computer_choice = 1
            elif user_character == 2:
                if user_choice == 2:
                    print(" You Lost!")
                    time.sleep(1)
                    print("BUT WAIT!")
                    time.sleep(1)
                    print("YOU USED SIKE!! you will have your option chosen again! RANDOMLY!")
                    user_choice = random.randint(1, 3)
            elif user_character == 3:
                print("You used Mystery Power....")


def score_func_scissors(user_choice, computer_choice, user_win_count, comp_win_count):
        if user_choice == 1:
            win(user_win_count, computer_choice, user_choice)
        elif user_choice == 2:
            lose(comp_win_count, computer_choice, user_choice)
        elif user_choice == 3:
            draw(computer_choice, user_choice)


def humanify(computer_choice):  # defines what to print as computer's choice on terminal
    if computer_choice == 1:
        return "Rock"
    if computer_choice == 2:
        return "Paper"
    if computer_choice == 3:
        return "Scissors"


def RPS(user_choice):   # main code, imports printing and difficulty increase from functions, baaqi sab isme hai
    computer_choice = random.random()   # assigns a random value b/w 0 and 1
    power = 'no'
    if round > 2:
        power = input(
            "Do you want to use your power in this round? Use yes or no \n")
    if RUL > computer_choice > RLL:
        computer_choice = 1
        power_func_rock(power, user_character, computer_choice, user_choice)
        score_func_rock(user_choice, computer_choice, user_win_count, comp_win_count)

    if PUL > computer_choice > PLL:
        computer_choice = 2
        power_func_paper(power, user_character, computer_choice, user_choice)
        score_func_paper(user_choice, computer_choice, user_win_count, comp_win_count)

    if SUL > computer_choice > SLL:
        computer_choice = 3
        power_func_scissors(power, user_character, computer_choice, user_choice)
        score_func_scissors(user_choice, computer_choice, user_win_count, comp_win_count)
    else:
        pass



def difficulty_increase(rock, paper, scissors): # records inputs and increases difficulty based on it
    global RUL
    global RLL
    global PUL
    global PLL
    global SUL
    global SLL
    if rock >= paper and rock >= scissors:
        RUL = 0.5
        RLL = 0
        PUL = 0.75
        PLL = 0.5
        SUL = 1
        SLL = 0.75
        RPS(userchoice)
    elif paper >= rock and paper >= scissors:
        RUL = 0.25
        RLL = 0
        PUL = 0.75
        PLL = 0.25
        SUL = 1
        SLL = 0.75
        RPS(userchoice)
    elif scissors >= rock and scissors >= paper:
        RUL = 0.25
        RLL = 0
        PUL = 0.5
        PLL = 0.25
        SUL = 1
        SLL = 0.5
        RPS(userchoice)


# MAIN CODE BELOW

user_choices = []
user_win_count = [0]
comp_win_count = [0]
print("Heyo, Welcome to Rock, Paper, Scissors. A code written in <10 minutes before my Info-Age class started.")
time.sleep(1.5)
print("Choose your banda")
time.sleep(0.5)
print(" 1 is Switcheroo: Switch your opponent's move to its exact opposite! \n 2 is Sike!: Give yourself a Lifeline! \n 3 is Mystery Power: Choose and find out!")
user_character = int(input())
for round in range(1, 5):
    if round == 4:
        if user_win_count[0] == 2 or user_win_count[0] == 1:
            print("YOU HAVE SUCCESSFULLY RAISED THE BAR!")
            break
        elif comp_win_count[0] == 2 or comp_win_count[0] == 1:
            print("THE BAR HAS BEEN LOWERED, YOU LOSE!")
            break
        elif user_win_count[0] == comp_win_count[0]:
            print("IT ALL ENDS IN A STALEMATE, WANT TO TRY AGAIN?")
            break
    elif user_win_count[0] == 2:
        print("YOU HAVE SUCCESSFULLY RAISED THE BAR!")
        break
    elif comp_win_count[0] == 2:
        print("THE BAR HAS BEEN LOWERED, YOU LOSE!")
        break
    elif user_win_count[0] == 1 and comp_win_count[0] == 1:
        print("DECIDING ROUND COMING UP!")
    print("ROUND {0}!".format(round))
    time.sleep(1)
    print("Input your choice:\n 1. Rock \n 2. Paper \n 3. Scissors")
    userchoice = int(input())
    user_choices.append(userchoice)
    for choice in user_choices:
        if choice == 1 and round > 1:
            rock = rock + 1
        elif choice == 2 and round > 1:
            paper = paper + 1
        elif choice == 3 and round > 1:
            scissors = scissors + 1
    difficulty_increase(rock, paper, scissors)