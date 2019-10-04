# -*- coding: utf-8 -*-

from scipy import integrate
from scipy import constants
import numpy as np
from matplotlib import pyplot as plt
import pylab


x0 = 0.0
y0 = 0.0
z0 = 0.0

vx0 = 10.0
vy0 = 0.0
vz0 = 0.0

E = 10
B = 10

w = (constants.e/constants.m_e)*B 
F = -(constants.e/constants.m_e)*E - w*vy0


def f(a, t):
    
    f0 = a[1]
    f1 = 0
    
    return [f0, f1]

def g(a, t):
    
    x = a[0]
    g0 = a[1]
    g1 = -w**2 * x + F
    g2 = w*x + vy0
    
    return [g0, g1, g2]

#Set time
t = np.linspace(0, 5*10e-12, 2000)

#Analitical solution
x_an = (vx0/w) * np.sin(w*t) - (F/w**2) * np.cos(w*t) + (F/w**2)
y_an = -(vx0/w) * np.cos(w*t) - (F/w**2) * np.sin(w*t) + (F/w)*t + (vx0/w) + vy0*t

#initial condition
a0 = [z0, vz0]
b0 = [x0, vx0, y0]
b1 = [x0, vy0,y0]
#Differentiation
sol_z = integrate.odeint(f, a0, t)
sol_xy = integrate.odeint(g, b0, t)


fig= plt.figure()
ax = fig.add_subplot(121)
ax.set_xlabel('t', size=20)
ax.set_ylabel('y', size=20)
ax.plot(t, sol_xy[:,2],'-*', markevery=10, color = 'red', label ='Решение')
ax.plot(t,  y_an, color='blue', label = 'Аналитическое решение')
pylab.legend(loc='upper right')


ax1 = fig.add_subplot(122)
plt.axis([-5e-12, 55e-12, -10e-12, 65e-13])
ax1.set_xlabel('t', size=20)
ax1.set_ylabel('x', size=20)
ax1.plot(t,  x_an, '-*', markevery=10, color = 'red', label ='Решение')
ax1.plot(t,  x_an, color='blue', label = 'Аналитическое решение')
pylab.legend(loc='best')

plt.tight_layout()
plt.show()






