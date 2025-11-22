#Побудуйте графік функції Y(x)=-5*cos(10*x)*sin(3*x)/(x^(1/2)), x=[0...10].
# Оберіть суцільний тип лінії, задайте колір та товщину графіку та позначте осі, виведіть назву графіка на екран, вставте легенду.
# Використайте бібліотеку Matplotlib.
import numpy as np
import matplotlib.pyplot as plt 

t = np.linspace(0.01, 10, 101)  # Починаємо з 0.01, щоб уникнути ділення на нуль

y = -5 * np.cos(10 * t) * np.sin(3 * t) / np.sqrt(t) 

plt.plot(t, y, label='Y(x) = -5*cos(10*x)*sin(3*x)/(x^(1/2))', color="black", linewidth=2)

plt.title('My plot', fontsize=15)  # Назва графіка
plt.xlabel('t', fontsize=12, color='blue')  # Вісь абсцис
plt.ylabel('y', fontsize=12, color='blue')  # Вісь ординат
plt.legend()
plt.grid(True)

plt.show()  
