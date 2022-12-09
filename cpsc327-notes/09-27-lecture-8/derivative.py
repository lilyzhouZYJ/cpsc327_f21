import matplotlib.pyplot as plt
import numpy as np


h = 0.0001
def deriv(f):
    return lambda x: (f(x+h)-f(x))/h

def x_squared(x):
    return x*x

def x_cubed(x):
    return x*x*x

def x_ponential(x):
    return x**x

print(x_cubed)
print(deriv(x_cubed)(5))

fig, ax = plt.subplots()
x = np.linspace(-5,5,100)
y = list(map(deriv(x_ponential), x))




ax.plot(x, y)
plt.show()

