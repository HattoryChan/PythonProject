import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

w=1.6*10**-19*10/(9.1*10**-31)
v=0.1
z=9.1*10**-31*10/(1.6*10**-19*100)       #31536000
r=1/w*np.sqrt(1+v**2)
'''
#function for diff.eq. 1 order
def f_x(t, x):
	return w*v #right side of the eq.
t=np.arange( 0, 10, 0.1) #diapazone
x0=0           #k #initial condition
D=odeint(f_x,x0,t) #differentiation
N1=D[:,0] #0 сама функция, 1 первая производнаяy
plt.plot(t, N1,'-r',linewidth=2,label='m') #chart y
plt.grid() #lattice
plt.ylabel("m") #signature 
plt.xlabel("t")
plt.legend()
'''
def f_y(t, y):
    return w
t=np.arange( 0, 10, 0.1) #diapazone
y0=0           #k #initial condition
D=odeint(f_y,y0,t) #differentiation
N2=D[:,0] #0 сама функция, 1 первая производнаяy
plt.plot(N2, t,'*',linewidth=2,label='N') #chart y
plt.grid() #lattice
plt.ylabel("y, analit") #signature 
plt.xlabel("x")
plt.show()
'''
t=np.arange( 0, 10 , 0.1) #diapazone

def analit_x(t): #analitic
    return 1/w*v-r*np.cos(w*t)+t

def analit_y(t):
    return 1/w+r*np.sin(w*t)

x=1/w*v-r*np.cos(w*t)+t
y=1/w+r*np.sin(w*t)


plt.plot(t, y,'-,r',linewidth=2,label='analit') #chart analit. eq.
plt.legend() #legend

'''
