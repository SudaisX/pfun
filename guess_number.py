from random import randint

def guessing_game(secret_num, num_tries):
    win = False
    while num_tries < 6:
        print(f'Attempt number {num_tries}')
        attempt = int(input())
        if attempt == secret_num:
            win = True
            break
        elif attempt < secret_num:
            if num_tries == 5:
                break
            else:
                print("Try again! Your guess is too low.")
                num_tries += 1
        elif attempt > secret_num:
            if num_tries == 5:
                break
            else:
                print("Try again! Your guess is too high.")
                num_tries += 1

    if win == True:
        print(f'Congratulations, you won! You guessed the secret number {secret_num} in {num_tries} guesses.')
    else:
        print("Sorry, you lose! Too many wrong guesses.")

secret_number = int(input())
guessing_game(secret_number, 1)