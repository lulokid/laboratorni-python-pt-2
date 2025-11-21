# Задано дані про кількість учнів у кожному з n=6 навчальних закладів і про тип закладів (школа, технікум або училище).
# Скласти програму, яка визначає загальну кількість учнів шкіл.
import json

# усі 6 навчальних закладів
institutions = {
    1: {"name": "Школа №1", "kind": "school"},
    2: {"name": "Коледж №1", "kind": "college"},
    3: {"name": "Технікум №1", "kind": "texnikum"},
    4: {"name": "Школа №2", "kind": "school"},
    5: {"name": "Технікум №2", "kind": "texnikum"},
    6: {"name": "Коледж №2", "kind": "college"}
}

# усі студенти та хто де навчається
students = [
    {"Name": "Vasiliy", "Surname": "Vasiliev", "Type of institutions": "school", "number": 1},
    {"Name": "Anton", "Surname": "Antonov", "Type of institutions": "texnikum", "number": 3},
    {"Name": "Alina", "Surname": "Alinova", "Type of institutions": "college", "number": 2}
]

try:
    with open("data.json", "wt", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
except Exception as e:
    print("Помилка при записі у файл:", e)

while True:
    print("\nВиберіть опцію:\n 1 - внести нові дані\n 2 - переглянути дані\n 3 - обчислити кількість учнів шкіл\n 0 - закрити")
    choice = input("Оберіть опцію:\n")

    if choice == "1":
        try:
            with open("data.json", "rt", encoding="utf-8") as file:
                students = json.load(file)

            print("Додати нового студента:")
            name = input("Name: ").strip()
            surname = input("Surname: ").strip()
            number = input("Номер навчального закладу (1-6): ").strip()

            if not number.isdigit() or int(number) not in institutions:
                print("Неіснуючий номер навчального закладу. Перевірте, чи існує такий навчальний заклад")
                continue

            number = int(number)
            type_of_institution = institutions[number]["kind"]

            students.append({
                "Name": name,
                "Surname": surname,
                "Type of institutions": type_of_institution,
                "number": number
            })

            with open("data.json", "wt", encoding="utf-8") as file:
                json.dump(students, file, ensure_ascii=False, indent=4)
            print("Дані додано.")
        except Exception as e:
            print("Помилка при додаванні даних:", e)

    elif choice == "2":
        try:
            with open("data.json", "rt", encoding="utf-8") as file:
                students = json.load(file)
                print("\nСписок студентів:")
                for student in students:
                    print(student)
        except Exception as e:
            print("Помилка при читанні файлу:", e)

    elif choice == "3":
        try:
            with open("data.json", "rt", encoding="utf-8") as file:
                students = json.load(file)
                school_count = sum(1 for student in students if student["Type of institutions"] == "school")
                print(f"\nКількість учнів у школах: {school_count}")
        except Exception as e:
            print("Помилка при обчисленні:", e)

    elif choice == "0":
        print("Програму завершено.")
        break

    else:
        print("Викникла помилка. Спробуйте ще раз, ввівши 0, 1, 2 або 3.")