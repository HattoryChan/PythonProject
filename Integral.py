from scipy import integrate
import math as m

def integ(x): #integrable function
    return m.sqrt(2*x - x*x)

def expr2(x): #analytical solution
	return 1/2*((x-1)*m.sqrt(-1*(x-2)*x)-m.asin(1-x))

I = integrate.quad(integ,0.1,1.9)
AnS = expr2(1.9) - expr2(0.1)

print("Integrable function: ", I)
print("Analitical solution: ", AnS)

    
