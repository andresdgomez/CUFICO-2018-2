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
from numpy import sqrt, pi, exp, linspace, save, random
def gaussian(x, amp, cen, wid):
	return amp * exp(-(x-cen)**2 /wid)

x = linspace(-10,10)
y = gaussian(x, 2.33, 0.21, 1.51) + random.normal(0, 0.2, len(x))

save("x_coord_noisy",x)
save("y_coord_noisy",y)

import matplotlib.pyplot as plt

plt.scatter(x, y)

plt.show()


from numpy import sqrt, pi, exp, linspace, load

def gaussian(x, amp, cen, wid):
	return amp * exp(-(x-cen)**2 /wid)

x=load("x_coord_noisy.npy")
y=load("y_coord_noisy.npy")

from scipy.optimize import curve_fit
init_vals = [1, 0, 1]
 # for [amp, cen, wid]
best_vals, covar = curve_fit(gaussian, x, y, p0=init_vals)
print best_vals

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(linspace(-10,10,100),gaussian(linspace(-10,10,100),best_vals[0],best_vals[1],best_vals[2]),"r-")
plt.show()

