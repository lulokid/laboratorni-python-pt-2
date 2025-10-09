#Дано одномірний масив, що складається з N цілочисельних елементів.
#Масив користувач має ввести з клавіатури. Знайти максимальний додатний елемент.
n = int(input("n = "))
print(f"Введіть {n} елементів масиву:")
arr = [int(input()) for _ in range(n)]
print("Масив з заданими елементами: ", arr)

maxelement = arr[0]

for element in arr:
    if element > maxelement:
        maxelement = element

print("Найбільший елемент масиву:", maxelement)