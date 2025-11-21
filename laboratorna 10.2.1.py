import numpy as np

import matplotlib.pyplot as plt

import sys

import os

x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

y = [4.5, 4.4, 3.0, 2.7, 2.3, 2.7, 3.6, 2.3, 4.4, 1.8, 2.9, 3.3, 1.8, 2.4, 2.5, 1.5] # Inflation, consumer prices (annual %) для Австралії

z = [2.3, 2.7, 1.8, 1.4, 2.1, 2.3, 1.4, 2.2, 3.2, 0.5, 1.8, 3.3, 2.5, 2.0, 1.6, 0.9] # Inflation, consumer prices (annual %) для Австрії

while True:
    choice = input("Введіть 0, якщо бажаєте побудувати стовпчасту діаграму для Австралії, "
                   "1 - для Австрії, 2 - завершити програму: ")

    if choice == "0":
        plt.bar(x, y, label='Australia', color='blue')  # синій, бо один з кольорів прапора Австралії
        plt.title(' Inflation in Australia (annual %)', fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel(' Inflation (%)', fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.show()

    elif choice == "1":
        plt.bar(x, z, label='Austria', color='red')  # червоний, бо один з кольорів прапора Австрії
        plt.title(' Inflation in Austria (annual %)', fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel(' Inflation (%)', fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.show()

    elif choice == "2":
        print("Завершення програми.")
        break

    else:
        print("Введено неправильне число. Введіть ще раз, тільки 0, 1 або 2.")