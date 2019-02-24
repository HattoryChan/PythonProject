import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#function for diff.eq. 1 order
def f(y, x):
	y1,y2 = y #function name
	return [y2, np.exp(-x)/x-2*y2-y1] #right side of the eq.

def analit(x): #analitic
    return np.exp(-x)*(x*(np.e-1)+x*np.log(x)+1)

def err(x):  #absolute error
    return np.abs(((analit(x)-y1))/(analit(x)))#/f_an(x)


x=np.arange( 1, 10, 1) #diapazone
y0=(1, 0) #initial condition
D=odeint(f,y0,x) #differentiation
#print(type(D))
y1=D[:,0] #0 сама функция, 1 первая производная
plt.plot(x,y1,'*',linewidth=2,label='y') #chart y
plt.grid() #lattice
plt.ylabel("y") #signature 
plt.xlabel("x")


plt.plot(x,analit(x),'-,r',linewidth=2,label='Аналитич.') #chart analit. eq.
plt.legend() #legend


graf_e=plt.figure()
plt.plot(x,err(x),'-o',linewidth=2,label='Ошибка')
plt.grid()
plt.ylabel("eps")
plt.xlabel("x")
plt.legend()
plt.show()
