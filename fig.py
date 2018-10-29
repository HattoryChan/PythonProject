# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Подключение библиотеки для рисования графиков
import matplotlib.pyplot as plt
#библитека для работы с массивами данных
import numpy as np
#задаем массив
x = np.linspace(-5,5,20)
y = x**2

#создание окна рисунка
fig = plt.figure()

#добавление осей
ax = fig.add_subplot(221)
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)

#подписи осей
ax.set_xlabel("x", size = 10)
ax.set_ylabel("y")

ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.set_xlabel("x")
ax2.set_ylabel("y")

ax3.set_xlabel("x")
ax3.set_ylabel("y")


#рисование графика
p ,= ax.plot(x, y, 'rs-')
p2 ,= ax1.plot(x, np.exp(-x), 'go-.')
p3 ,= ax2.plot(x, np.sin(x), 'bo-')
p4 ,= ax3.plot(x, y**2)

#добавить легенду
ax.legend([p, p2], ["x^2", "exp(-x)"], prop={'size':10})

#настройка диапазона по осям
ax.set_xlim(-5, 5)
ax.set_ylim(0.1, 300)

#добавить сетку
ax.grid()

#логарифмический масштаб
ax.set_yscale("log")

#показать окно
fig.show()
#fig.savefig("fig.png")

plt.tight_layout()