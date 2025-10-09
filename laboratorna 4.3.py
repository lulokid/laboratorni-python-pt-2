#Видалення всіх елементів з парним порядковим номером.
def delete():

    a = list(map(int,input('Введіть масив: ').split()))

    print(a)

    result = []

    for x in range(len(a)):

        if x %2 != 0:

            result.append(x)

    print('Масив після видалення парних елементів: ')

    print(result)

    return result

delete()