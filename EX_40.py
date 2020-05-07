import random

while True:
    menu = ['New Game (N)', 'Score (S)', 'Difficulty (D)', 'Quit (Q)']
    for i in menu:
        print(i)
    click = input('Which option do you choose?>> ')
    click = click.lower()
    guess = 5
    if click == 'n':
        n = random.randint(1,100)
        print(n)
        inp = int(input("Write your guess>> "))
        while guess > 1:
            guess -= 1
            if inp > n:
                print('Your guess is too big')
                inp = int(input("Write your guess>> "))
            elif inp < n:
                print('Your guess is too small')
                inp = int(input("Write your guess>> "))
            else:
                print('You guessed right')
                break
    if click == 'q':
        break