# Побудувати кругову діаграму, яка відображає кількість студентів/учнів у кожному з 6 навчальних закладів.
import matplotlib.pyplot as plt
import numpy as np

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
    {"Name": "Alina", "Surname": "Alinova", "Type of institutions": "college", "number": 2},
    {"Name": "Igor", "Surname": "Igorov", "Type of institutions": "college", "number": 2},
    {"Name": "Oleksii", "Surname": "Oleksiev", "Type of institutions": "college", "number": 4},
    {"Name": "Kateryna", "Surname": "Katerynova", "Type of institutions": "college", "number": 1},
    {"Name": "Illya", "Surname": "Illich", "Type of institutions": "college", "number": 2},
    {"Name": "Hrystyna", "Surname": "Hrystunova", "Type of institutions": "college", "number": 2},
    {"Name": "Oleksandra", "Surname": "Oleksandrova", "Type of institutions": "college", "number": 2}
]
# Підрахунок кількості студентів у кожному закладі
counts = {inst["name"]: 0 for inst in institutions.values()}
for student in students:
    num = student["number"]
    inst_name = institutions[num]["name"]
    counts[inst_name] += 1

data = list(counts.values())
labels = list(counts.keys())

# Функція для підписів
def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} students)"

# Побудова кругової діаграми про кількість здобувачів освіти у кожному навчальному закладі
fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    data,
    autopct=lambda pct: func(pct, data),
    textprops=dict(color="w")
)

# Легенда діаграми
ax.legend(
    wedges, labels,
    title="Заклади освіти",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.setp(autotexts, size=6, weight="bold")
ax.set_title("Кількість студентів у закладах освіти") # Назва діаграми
plt.show()
