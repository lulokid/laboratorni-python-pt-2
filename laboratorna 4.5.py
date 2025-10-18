#Задано текст з малих латинських літер. Скласти програму, яка формує множину з літер,
# що входять у цей текст, та визначає кількість розділових знаків у тексті.
def text():
    rechennya = input("Введіть текст: ")

    letters = set()
    for ch in rechennya:
        if 'a' <= ch <= 'z':
            letters.add(ch)
    sorted_letters = sorted(letters)
    print(f"Множина літер: {set(sorted_letters)}")

    znaky = ".,!?;:-()[]\"'/"

    count = 0
    for ch in rechennya:
        if ch in znaky:
            count += 1
    print(f"Кількість розділових знаків: {count}")


text()
