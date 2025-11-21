#Знайти дані Population, total для уcіх країн світу за 2019 рік.
# Вивести вміст .csv файлу на екран.
# Організувати пошук даних для введених користувачем назв країн та записати результат пошуку у новий .csv файл.

import csv
import os

source_file = "laboratorna9.csv" # Файл, завантажений з порталу
output_file = "new_laboratorna9.csv" # Файл з даними про країни, які обрав користувач

if not os.path.exists(source_file):
    print("Файл не знайдено.")
    exit()

# Створення нового файлу з заголовками
with open(output_file, "w", newline='', encoding="utf-8") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Country Name", "2019 [YR2019]"])

print("Введіть назву країни англійською (введіть 'стоп' для завершення):")

while True:
    country = input("Країна: ").strip().lower()
    if country == "стоп":
        break

    found = False
    with open(source_file, "r", encoding="cp1251") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if row["Country Name"] and row["2019 [YR2019]"]:
                if row["Country Name"].strip().lower() == country:
                    print(f"{row['Country Name']}: {row['2019 [YR2019]']}")
                    with open(output_file, "a", newline='', encoding="utf-8") as out_file:
                        writer = csv.writer(out_file)
                        writer.writerow([row["Country Name"], row["2019 [YR2019]"]])
                    found = True
                    break

    if not found:
        print("Країну не знайдено. Можливо, були введенені цифри чи розділові знаки або одруківка у назві країни."
              " Введіть назву країни тільки англійською мовою.")
