import random
import os

def choose_options(money):
    print()
    print('You have ${:.2f}'.format(money))
    print('Choose one of the following menu options: ')
    print('1) Play the slot machine. ')
    print('2) Save game. ')
    print('3) Cash out. ')
    option = int(input())
    return option

def progress():
    first_number = random.randint(0,9)
    second_number = random.randint(0,9)
    third_number = random.randint(0,9)
    print('The slot machine shows {}{}{}.'.format(first_number,second_number,third_number))
    if first_number == second_number == third_number:
        return 2
    elif first_number == second_number:
        return 1
    elif first_number == third_number:
        return 1
    elif second_number == third_number:
        return 1
    else:
        return 0

def make_request(option, money):
    if option == 1:
        check = progress()
        if check == 1:
            money -= 0.25
            print('You win 50 cents!')
        elif check == 2:
            money += 10
            print('You win the big prize, $10.00!')
        else:
            money -= 0.25
            print("Sorry you don't won anything.")
        return True, money
    elif option == 2:
        print('Your money had saved!')
        return False, money
    else:
        print('Thank you for playing! You end with ${:.2f}'.format(money))
        return False, money

def play_game(run_game, money):
    while run_game:
        option = choose_options(money)
        run_game, money = make_request(option, money)
    x = str(money)
    with open('money.txt','w') as file:
        file.write(x)

#with open('money.txt') as file:
#    money = float(file.read())

play_game(True, 10)