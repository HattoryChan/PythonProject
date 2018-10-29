import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft


data = np.loadtxt("cos.txt", delimiter=' ', dtype= np.float)
y = []
x = []
for f in data:
    y.append(f[0])
    
for f in data:
    x.append(f[1])
    
yf = x
xf = fft(y)

#создание окна рисунка
fig = plt.figure()

ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
#подписи осей
ax.set_xlabel("Freq")
ax.set_ylabel("Amp")

ax2.set_xlabel("Time")
ax2.set_ylabel("Amp")

p ,= ax.plot(yf, xf, 'rs-')
ax.grid()

p2 ,=ax2.plot(y, x, 'rs-')
ax2.grid()

fig.show()
plt.tight_layout()
