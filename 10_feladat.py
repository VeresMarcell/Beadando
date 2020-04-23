# ins = int(input('Teszt esetek: '))
# if 1<= ins <=100:
#     for i in range(ins):
#         a, b = input('A és B: ').split()
#         a = int(a)
#         b = int(b)
#         if 1 <= a <= 10**9 and 1 <= b <= 10**9:
#             print((a+b)-10)
#         else:
#             print('A vagy B nem esik a megfelelő tartományba ([1,10^9])')
# else:
#     print('A teszt esetek száma nem megfelelő')

ins = int(input('Number of instances: '))
if 1 <= ins <= 100:
    for i in range(ins):
        a = int(input('A: '))
        b = int(input('B: '))
        print((lambda a, b: ((a+b)-10) if 1<=b<=10**9 and 1<=b<=10**9 else print('A or B is not in the sufficient interval[1,10^9]'))(a,b))
else:
    print('Insufficient number of instances')