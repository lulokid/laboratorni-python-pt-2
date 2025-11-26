# Створити датафрейм з даними використання велодоріжок за рік, заданий варіантом (за 2014 рік).
# Перевірити основні характеристики датафрейму
# Визначити загальну кількість велосипедистів за рік на усіх велодоріжках
# Визначити загальну кількість велосипедистів за рік на кожній велодоріжці
# Визначити, який місяць найбільш популярний у велосипедистів, на кожній з  трьох з обраних велодоріжок.
# Побудувати графік завантаженості однієї з велодоріжок по місяцям.

import pandas as pd
import matplotlib.pyplot as plt


df2014 = pd.read_csv('comptagevelo2014.csv') # датафрейм csv файлу з даними велодоріжок за 2014

print("\nПерші 5 записів датафрейму:")
print(df2014.head())
print("\nЗагальна інформація датафрейму:")
print(df2014.info())
print("\nОписова статистика датафрейму:")
print(df2014.describe())

# кількість велосипедистів по кожній велодоріжці за рік
sums_per_way = df2014.iloc[:, 1:].sum()
print("Кількість велосипедистів по кожній велодоріжці за рік:")
print(sums_per_way)

# загальна кількість велосипедистів на усіх велодоріжках за рік
total_sum = sums_per_way.sum()
print(f"\nЗагальна кількість велосипедистів за рік: {total_sum}")

df = pd.read_csv('comptagevelo2014.csv')
df['Date'] = pd.to_datetime(df['Date'])

# виведення усіх існуючих велодоріжок
bike_way = df.columns[1:]  # пропуск першого стовпця Date, бо це не назви велодоріжок, а дати
print("Усі велодоріжки:")
for way in bike_way:
    print("-", way)

# запит у користувача на введення 3 існуючих велодоріжок
selected_way = []
while len(selected_way) < 3:
    user_input = input(f"\nВведіть назву велодоріжки {len(selected_way)+1}: ").strip()
    if user_input in bike_way:
        selected_way.append(user_input)
    else:
        print("Велодоріжку не знайдено. Скопіюйте назву без зайвих розділових знаків")

df['Month'] = df['Date'].dt.month

# найпопулярнішй місяць для обраної користувачем велодоріжки
for way in selected_way:
    monthly_sum = df.groupby('Month')[way].sum()
    most_popular_month = monthly_sum.idxmax()
    print(f"\nНайпопулярніший місяць для '{way}': {most_popular_month}. Кількість відвідувачів за місяць: {monthly_sum[most_popular_month]})")

# введення назви існуючої велодоріжки для графіка
while True:
    first_lane = input("\nВведіть назву велодоріжки для побудови графіка: ").strip()
    if first_lane in bike_way:
        break
    else:
        print("Велодоріжку не знайдено. Скопіюйте назву без зайвих розділових знаків")

# побудова графіка для обраної існуючої велодоріжки
monthly = df.groupby('Month')[first_lane].sum()

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.plot(monthly.index, monthly.values, label=first_lane, color='purple')
plt.title(f"Завантаженість велодоріжки {first_lane} по місяцях", fontsize=15)
plt.xlabel("Місяці", fontsize=12, color='black')
plt.ylabel("Кількість велосипедистів", fontsize=12, color='black')
plt.xticks(range(1, 13))  # щоб були всі місяці від 1 до 12
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

