from scipy import integrate
import math as m

def integ(x): #integrable function
    return m.sin(x**2)

def integ2(x): #integrable function
    return (m.asin(x))**(1/2)

def expr2(x): #analytical solution
	return 1/2*((x-1)*m.sqrt(-1*(x-2)*x)-m.asin(1-x))

I = integrate.quad(integ,0,(m.pi/2)**(1/2))[0] + integrate.quad(integ2,0,1)[0]
AnS = expr2(1.9) - expr2(0.1)

print("Integrable function: ", '{:.3f}'.format(I))
print("Analitical solution: ", AnS)

    
