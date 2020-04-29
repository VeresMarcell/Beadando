# 10. feladat
# Írjon programot, amely az alábbi módon mindig hibásan ad össze két számot. A program mindig
# megkapja először a teszt esetek számát (1<=T<=100), majd A és B összeadandó számokat
# (1<=A,B<=109)

ins = int(input('Number of instances: '))
if 1 <= ins <= 100:
    for i in range(ins):
        a = int(input('A: '))
        b = int(input('B: '))
        print((lambda a, b: ((a+b)-10) if 1<=b<=10**9 and 1<=b<=10**9 else print('A or B is not in the sufficient interval[1,10^9]'))(a,b))
else:
    print('Insufficient number of instances')