# Імпортувати бібліотеку NLTK та текст chesterton-brown.txt із електронного архіву  текстів Project Gutenberg,
# для виконання завдань взяти текст, заданий варіантом.
# Визначити кількість слів у тексті.
# Визначити 10 найбільш вживаних слів у тексті, побудувати на основі цих даних стовпчасту діаграму.
# Виконати видалення з тексту стоп-слів та пунктуації,
# після чого знову знайти 10 найбільш вживаних слів у тексті та побудувати на їх основі стовпчасту діаграму.


import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
from collections import Counter

with open("chesterton-brown.txt", "r", encoding="utf-8") as f: # тхт файл з розповіддю
    text = f.read()

# розбиття тексту на слова без видалення пунктуації
words = text.split()
print("Кількість слів у тексті з урахуванням пунктуації:", len(words))

# найбільш вжваних 10 слів у тексті без видалення пунктуації
counter_before = Counter(words)
top10_before = counter_before.most_common(10)
print("10 найуживаніших слів у тексті з урахуванням пунктуації):", top10_before)

# побудова стовпчастої діаграми для найбільш вжваних 10 слів у тексті без видалення пунктуації
labels, values = zip(*top10_before)
plt.figure(figsize=(10,6))
plt.bar(labels, values, color="green")
plt.title("10 найуживаніших слів у тексті з урахуванням пунктуації та стоп-слів", fontsize=14)
plt.xlabel("Слова", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# токенізація
tokens = word_tokenize(text, language="english")  # для тексту, написаного англійською мовою

# видалення усієї пунктуації з тексту
words = [w.lower() for w in tokens if w.isalpha()]

# видалення стоп-слів (артиклі + найчастіше вживані слова серед займенників + прийменників,
# бо вони не маюьть ніякої смислової нагрузки, тому їх прибираю з тексту)
stop_words = {"a", "the", "an", "of", "in", "on", "or", "and", "he", "she", "it", "we", "they", "to", "with", "i"}
deleted_words = [w for w in words if w not in stop_words]

counter = Counter(deleted_words)

# найбільш вжваних 10 слів у тексті після видалення пунктуації та слів, які не маюьть ніякої смислової нагрузки
most_common_10 = counter.most_common(10)
print("10 найуживаніших слів у тексті без пунктуації та без часто вживаних займенників/прийменників):", most_common_10)

# побудова стовпчастої діаграми для найбільш вжваних 10 слів у тексті після видалення пунктуації та слів, які не маюьть ніякої смислової нагрузки
labels, values = zip(*most_common_10)
plt.figure(figsize=(10,6))
plt.bar(labels, values, color='red')
plt.title("10 найвживаніших слів у тексті після видалення пунктуації та стоп-слів", fontsize=14)
plt.xlabel("Слова", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()