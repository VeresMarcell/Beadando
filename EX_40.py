import random
score = open('Score.txt','a')


def printScore(file):
    sc = ''
    for line in file:
        sc += (line)
    return sc

guess = 15

while True:
    menu = ['New Game (N)', 'Score (S)', 'Difficulty (D)(Easy by default)', 'Quit (Q)']
    for i in menu:
        print(i)
    click = input('Which option do you choose?>> ')
    click = click.lower()
    scr = 1
    if click == 'n':
        n = random.randint(1,100)
        inp = int(input("Write your guess>> "))
        while guess > 1:
            guess -= 1
            scr += 1
            if inp > n:
                print('Your guess is too big')
                inp = int(input("Write your guess>> "))
            elif inp < n:
                print('Your guess is too small')
                inp = int(input("Write your guess>> "))
            elif inp == n:
                print('You guessed right')
                print(scr-1,file=score)
                score.close()
                break
        if guess == 1:
            print('You are out of tries')
    if click == 's':
        score = open('Score.txt','r')
        print('Your scores are>>\n'+printScore(score))
        score.close()
    if click == 'd':
        while True:
            try:
                tmp = int(input('Set your difficulty(easy(1), normal(2), hard(3))>> '))
                if tmp == 1:
                    guess = 15
                    sett = ('Difficulty is now set to {} tries').format(guess)
                    print(sett)
                    break
                elif tmp == 2:
                    guess = 10
                    sett = ('Difficulty is now set to {} tries').format(guess)
                    print(sett)
                    break
                elif tmp == 3:
                    guess = 5
                    sett = ('Difficulty is now set to {} tries').format(guess)
                    print(sett)
                    break
                else:
                    print('Please give a valid difficulty')
                    continue
            except ValueError:
                print('Please give a valid difficulty')
                continue
    if click == 'q':
        break
    elif click != 'q' and click != 'd' and click != 's' and click != 'n':
        print('Unsupported input')