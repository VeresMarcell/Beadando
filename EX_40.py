import random

n = random.randint(1,100)
print(n)
inp = int(input("Write your guess: "))
while inp != n:
    if inp > n:
        print('Your guess is too big')
        inp = int(input("Write your guess: "))
    else:
        print('Your guess is too small')
        inp = int(input("Write your guess: "))

print('You guessed right')