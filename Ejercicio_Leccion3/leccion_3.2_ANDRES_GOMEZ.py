'''
from numpy import sqrt, pi, exp, linspace, save
def gaussian(x, amp, cen, wid):
	return amp * exp(-(x-cen)**2 /wid)


x = linspace(-10,10)
y = gaussian(x, 2.33, 0.21, 1.51)

save("x_coord",x)
save("y_coord",y)

import matplotlib.pyplot as plt
plt.scatter(x, y)

plt.show() '''
from numpy import sqrt, pi, exp, linspace, save, random,load

import matplotlib.pyplot as plt

x=load("x_spectra.npy")
y=load("y_spectra.npy")

plt.scatter(x, y)
plt.grid()
plt.show()


def double_gaussian( x, c1, mu1, sigma1, c2, mu2, sigma2,m,b):
    
    gausum =   c1*exp(-(x-mu1)**2.0 /sigma1) + c2*exp(-(x - mu2)**2.0 /sigma2)+ m*x + b
    return gausum
    

from scipy.optimize import curve_fit
init_vals = [1.,20.,1.0,1.,5.,1.0,1,95]
best_vals, covar = curve_fit(double_gaussian, x, y, p0=init_vals)
print best_vals

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(linspace(0,100,100),double_gaussian(linspace(0,100,100),best_vals[0],best_vals[1],best_vals[2],best_vals[3],best_vals[4],best_vals[5],best_vals[6],best_vals[7]),"r-")
plt.show()



