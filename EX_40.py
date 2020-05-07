import random
score = open('Score.txt','a')


def printScore(file):
    sc = ''
    for line in file:
        sc += (line)
    return sc


while True:
    menu = ['New Game (N)', 'Score (S)', 'Difficulty (D)', 'Quit (Q)']
    for i in menu:
        print(i)
    click = input('Which option do you choose?>> ')
    click = click.lower()
    guess = 5
    scr = 1
    if click == 'n':
        n = random.randint(1,100)
        print(n)
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
        print('You are out of tries')
    if click == 's':
        score = open('Score.txt','r')
        print('Your scores are>>\n'+printScore(score))
        score.close()
    if click == 'q':
        break