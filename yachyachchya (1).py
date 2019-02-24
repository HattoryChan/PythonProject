import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import ode, odeint
from mpl_toolkits.mplot3d import Axes3D
w=1.75*10**12 #**12
w1=1.75
a=0.9
b=-1.57  #в градусах -90
m=0   #y
n=0.1  #x
E=10
B=10
DotCountStart = 0.0
DotCount = 0.01
DotCountMax = 3.0
t=np.arange(DotCountStart, DotCountMax , DotCount) 
xz = 1/w*m-a/w*np.cos(w*t+b)+t
yz = -1/w*(n-1)+a/w*np.sin(w*t+b)

#print (xz)
print (yz)


def fx(x, t):
	x1,x2= x #function name
	return [x2, w1**(2.0)-w1**(2.0)*x2] #right side of the eq.
t=np.arange( DotCountStart, DotCountMax, DotCount) #diapazone
x0=(0, 0.1) #initial condition
D= odeint(fx,x0,t) #differentiation
#print(type(D))
x1=D[:,0] #0 сама функция, 1 первая производная

#print (x1)
#print (xz)

def fy(y, t):
    y1,y2=y
    return  [y2, -((w**(2.0))*y1)]#right side of the eq.
t=np.arange(DotCountStart, DotCountMax, DotCount) #diapazone
y0=[0.0,1.0] #in€€€€itial condition
y1= odeint(fy,y0,t,mxstep = 2000) #differentiation

#plt.plot(x1,sol[:,0])
print (y1)
'''
plt.grid() #lattice
plt.ylabel("t") #signature 
plt.xlabel("x")
plt.plot(t,xz,'--',linewidth=2,label='software solution') #chart y
plt.grid() #lattice
plt.ylabel("t") #signature 
plt.xlabel("x")

'''
'''
plt.grid() #lattice
plt.ylabel("t") #signature 
plt.xlabel("x")
plt.plot(t,x1,'*r',linewidth=2,label='software solution') #chart y
plt.grid() #lattice
plt.ylabel("t") #signature 
plt.xlabel("x")
'''

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
#ax.plot(t, yz)
#ax.set_title(label = 'traektory', color='r')
ax.plot(t, y1[:,0], '*',linewidth=2,label='software solution')
ax.set_title(label = 'komp', color='r')
ax.grid(True)

'''
fig2 = plt.figure(figsize=(10,6))
ax = fig2.add_subplot(221)
ax.plot(x1, sol,'*',linewidth=2,label='software solution')
ax.set_title(label = 'komp', color='r')
ax.grid(True)
'''
'''
plt.plot(x,y1,) #chart y
plt.grid() #lattice
plt.ylabel("y") #signature 
plt.xlabel("x")
'''
plt.tight_layout()
plt.show()

print ('Скорость общая(м/с) =',E/B)
print ('Скорость движения по трохоиде(м/с) =',((n-E/B)**2+m**2)**(1/2))
