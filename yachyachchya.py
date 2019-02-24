import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
w=1.75*10**12 #**12
a=0.9
b=-1.57  #в градусах -90
m=0   #y
n=0.1  #x
E=10
B=10

t=np.arange(0,3,0.1) 
xz = 1/w*m-a/w*np.cos(w*t+b)+t
yz = -1/w*(n-1)+a/w*np.sin(w*t+b)
print (xz)
print (yz)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(231)
ax.plot(xz, yz)
ax.set_title(label = 'suka', color='r')
ax.grid(True)




plt.tight_layout()
'''
plt.plot(yz, xz,'-r',linewidth=2,label='rectilinear') #chart y
plt.grid() #lattice
plt.ylabel("y") #signature 
plt.xlabel("z")
plt.legend()
'''
def fx(y, t):
	y1,y2= y #function name
	return [w+w*y1, -w*y2] #right side of the eq.
t=np.arange( 0, 4.0, 0.1) #diapazone
y0=(0, 0) #initial condition
D=odeint(fx,y0,t) #differentiation
#print(type(D))
y1=D[:,0] #0 сама функция, 1 первая производная
#print (y1)

plt.show()

print ('Скорость общая(м/с) =',E/B)
print ('Скорость движения по трохоиде(м/с) =',((n-E/B)**2+m**2)**(1/2))