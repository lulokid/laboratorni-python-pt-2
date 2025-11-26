# є словник учнів та студентів 6 начальних закладів: шкіл, технікумів та коледжів.
# Треба перетворити словник на датафрейм, вивести його основні характеристики, додати новий стовпець (стипендія).
# Визначити кількість студентів зі стипендіями, відсортувати студентів за зростанням стипендій,
# а також відфільтровування студентів, але тільки тих, які мають будь-яку стипендію,
# і обчислити середню стипендію по всім 6 закладам освіти з урахуванням навіть тих, у кого її немає,
# плюс вивести студента(ів) з найбільшою і найменшою стипендією
import pandas as pd

# словник з лабораторної 5
data = {
    "andrii": {"institution_id": 1, "institution_name": "Школа №1", "kind": "school"},
    "artem": {"institution_id": 2, "institution_name": "Коледж №1", "kind": "college"},
    "anastasia": {"institution_id": 3, "institution_name": "Технікум №1", "kind": "texnikum"},
    "alina": {"institution_id": 4, "institution_name": "Школа №2", "kind": "school"},
    "anna": {"institution_id": 5, "institution_name": "Технікум №2", "kind": "texnikum"},
    "alex": {"institution_id": 6, "institution_name": "Коледж №2", "kind": "college"}
}

# перетворення словника у датафрейму та виведення основних характеристик датафрейму
df = pd.DataFrame.from_dict(data, orient="index")
df.index.name = "name"

print("\nПерші 3 рядки датафрейму:")
print(df.head(3))

print("\nТипи даних датафрейму:")
print(df.dtypes)

print("\nКількість рядків та стовпців датафрейму:")
print(df.shape)

print("\nОписова статистика датафрейму:")
print(df.describe())

# новий стовпець scholarship (стипендія)
df["scholarship"] = [2900, 2900, 1800, 1500, 0, 0]

print("\nДатафрейм з новим стовпцем scholarship (стипендія):")
print(df)

# кількість студентів, які отримують стипендію
count_scholarship = (df["scholarship"] > 0).sum()
print("\nКількість студентів зі стипендією:", count_scholarship)

# сортування студентів за зростанням стипендій
sorted_df = df.sort_values(by="scholarship", ascending=True)
print("\nСортування за зростанням стипендій:")
print(sorted_df)

# відфільтровування студентів, але тільки тих, які мають будь-яку стипендію
scholarship_students = df[df["scholarship"] > 0]
print("\nСтуденти зі стипендією:")
print(scholarship_students)

# середня стипендія по всім 6 закладам освіти з урахуванням навіть тих, у кого її немає
average_scholarship = df["scholarship"].mean()
print("\nСередня стипендія:", average_scholarship)

# студенти з найбільшою стипендію
max_value = df["scholarship"].max()
max_rows = df[df["scholarship"] == max_value]
print("\nСтуденти з найбільшою стипендією:")
print(max_rows)

# студенти з найменшою стипендію
min_value = df["scholarship"].min()
min_rows = df[df["scholarship"] == min_value]
print("\nСтуденти з найменшою стипендією:")
print(min_rows)
