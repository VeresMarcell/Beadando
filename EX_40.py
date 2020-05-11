# 40. Készítsen egy programot, ami választ egy véletlen számot [1,100] intervallumon, majd
# lehetővé teszi a felhasználó számára, hogy kitalálja melyik számot generálta a program. Ha a
# felhasználó nem találja el a számot akkor segítsen neki és mondja meg, hogy a
# próbálkozásánál kisebb vagy nagyobb a generált szám. Készítsen a programhoz egy szöveges
# menüt amiben a felhasználó a billentyűzettel beírt betűkkel tud az egyes menüpontokban
# lépni. Menüpontok: New Game, Score, Difficulty, Quit. A Score menüponton eléri a
# felhasználó az eddigi összes megnyert játékainak a számát (ehhez használjon filekezelést). A
# Difficulty-n belül állítani lehet 3 nehézségi szintet, amelyek tetszőleges probálkozások számát
# jelölik. (Pl. Easy – 10-szer próbálkozhat a felhasználó, hogy eltalálja a számot). A Quit menu
# a játék bezárását eredményezi.

import random
score = open('Score.txt','a')


def printScore(file):
    sc = ''
    for line in file:
        sc += (line)
    return sc

guess = 15

while True:
    menu = ['New Game (N)', 'Score (S)', 'Difficulty (D)(Easy by default)', 'Quit (Q)']     #Menüpontok kiíratása
    for i in menu:
        print(i)
    click = input('Which option do you choose?>> ')     #User választása
    click = click.lower()
    scr = 1
    if click == 'n':        #User Választásának vizsgálata
        n = random.randint(1,100)
        inp = int(input("Write your guess>> "))
        while guess > 1:        #Próbálkozások/pontok számlálása és vizsgálata
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
    if click == 's':        #pontok kiíratása
        score = open('Score.txt','r')
        print('Your scores are>>\n'+printScore(score))
        score.close()
    if click == 'd':
        while True:     #Nehézség kiválasztása és a választás vizsgálata
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
score.close()