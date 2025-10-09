#Перестановка елементів списку у зворотньому порядку.
def reversed():

    a = list(map(int,input('Введіть масив: ').split()))

    print(a)

    reversed_a = a[::-1]

    print('Масив після запису у зворотньому порядку: ')

    print(reversed_a)

    return reversed_a

reversed()