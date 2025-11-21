# Розглянути показник Inflation, consumer prices (annual %) для Австралії та Австрії у діапазоні від 2000 до 2015 року включно
# та на основі цих даних побудувати графіки, що показують динаміку показника для двох країн
import numpy as np

import matplotlib.pyplot as plt

import sys

import os

x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

y = [4.5, 4.4, 3.0, 2.7, 2.3, 2.7, 3.6, 2.3, 4.4, 1.8, 2.9, 3.3, 1.8, 2.4, 2.5, 1.5] # Inflation, consumer prices (annual %) для Австралії

z = [2.3, 2.7, 1.8, 1.4, 2.1, 2.3, 1.4, 2.2, 3.2, 0.5, 1.8, 3.3, 2.5, 2.0, 1.6, 0.9] # Inflation, consumer prices (annual %) для Австрії

np.array(x)

np.array(y)

np.array(z)

plt.plot(x, z, label='Australia', color = "blue") # синій, бо один з кольорів прапора Австралії

plt.plot(x, y, label='Austria', color = "red") # червоний, бо один з кольорів прапора Австрії

plt.title('Inflation, consumer prices (annual %)', fontsize=15)   # назва графіка

plt.xlabel('Year', fontsize=12, color='black') # вісь абсцис

plt.ylabel('Indicator', fontsize=12, color='black') # вісь ординат

plt.legend()

plt.grid(True)

plt.show()