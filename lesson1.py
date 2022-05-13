import os

# 1.
import random


def table(lenght):

    for i in range(1, lenght + 1):
        for j in range(1, 11):
            print(f'{i} x {j} = {i*j}')
        print('-'*5)


table(3)

#2.
def print_directory_contents(sPath):

    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
print_directory_contents('C:\Temp')

# 3.
def gen(start, finish):
    spisok = []
    slovar = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        spisok.append(rnd)
        slovar.update({'elem_{}'.format(rnd): rnd})

    return (spisok, slovar)


print(gen(1, 40))

# 4.
def get_percent(amount, months):
    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False


def deposit(amount, months):
    percent = get_percent(amount, months)
    if not percent:
        print('Нет подходящего тарифа')


    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit

    print(f'сумму вклада на конец срока {round(total, 2)} руб.')


deposit(10000, 12)

# 5.
def chargable_deposit(amount, months, charge=0):
    percent = get_percent(amount, months)
    if not percent:
        print('Нет подходящего тарифа')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit
        if month != 0 and month != months - 1:
            total += charge + charge * percent / 100 / 12

    print(f'сумму вклада на конец срока {round(total, 2)} руб.')


chargable_deposit(10000, 24, 100)