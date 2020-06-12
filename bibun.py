import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def func(y,x,a):
    dydx =a*y
    return dydx

a=1
y0=1
x =np.arange(0,3,0.01)
y= odeint(func,y0,x,args=(a,))
plt.plot(x,y,label='exp')
plt.legend()
plt.show()
