import random


def rps():
    list = ['rock','paper','scissors']
    print("Welcome to rock, paper, scissors. Please choose [r,p,s]")
    choice = input()#your choice
    cpu = random.choice(list) #computer's choice

    if choice == "r":
        choice = "rock"
    elif choice == "p":
        choice = "paper"
    elif choice == "s":
        choice = "scissors"
    else:
        print('That is not a legal move in rock paper scissors')
        return

    print (f'''Your choice: {choice}
Computer\'s choice: {cpu}''')

    if choice == cpu:
        print("It's a tie")
    elif choice == 'rock':#outcomes if you choose rock
        if cpu == 'scissors':
            print('You win')#rock>scissors
        elif cpu == 'paper':
            print("You lose")#rock<scissors
    elif choice == 'paper':#outcomes if you choose paper
        if cpu == 'rock':
            print('You win')
        elif cpu == 'scissors':
            print("You lose")
    elif choice == 'scissors':#outcomes if you choose scissors
        if cpu == 'paper':
            print('You win')
        elif cpu == 'rock':
            print("You lose")

rps()