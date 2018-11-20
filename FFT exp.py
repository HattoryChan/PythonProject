import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

fName = "cos.txt"
delim =' '

#load the signal value from txt
data = np.loadtxt(fName, delimiter=delim, dtype= np.float)
y = []
x = []
# put it on the two list
for f in data:
    y.append(f[0])
    
for f in data:
    x.append(f[1])

num_t = int(y[-1]) #The maximum count of signal dot
#create line range of value (0, 0.001, 0.002, ... , 1) - 100 dots
t, dt = np.linspace(0, 1, num_t, endpoint=False, retstep=True)


amp = np.fft.rfft(x)  #make fft amp
freqs = np.fft.rfftfreq(t.shape[-1],dt) #make fft phase 

pl.subplot(311) #create graphics windows
pl.plot(y,x)    # add value and axes
pl.title('FFT: '+ fName) # Title name
pl.xlabel('freq')   #x axes name
pl.ylabel('amp')    #y axes name

pl.subplot(312) 
pl.plot(freqs[:60],np.sqrt(amp.real**2+amp.imag**2)[:60])
pl.title('FFT: Amp')
pl.xlabel('freq')
pl.ylabel('amp')

pl.subplot(313)
pl.plot(freqs[:60],(np.arctan2(amp.imag,amp.real))[:60])
pl.title('FFT: Freq')
pl.xlabel('phase')
pl.ylabel('freq')


pl.tight_layout(pad=0.4, w_pad=2.5, h_pad=1.0)
pl.show()



