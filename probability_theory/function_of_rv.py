import numpy as np
import matplotlib.pyplot as plt
from utility import savefig, plt_reset


def pdf_x(x):
    return np.where(np.logical_and(x <= np.pi, x >= -np.pi), 1/(2*np.pi), 0)


def pdf_y(y):
    return (1.0/np.pi)*(1.0/np.sqrt(1.0 - np.square(y)))


def g(X):
    return np.sin(X)


X = np.random.uniform(-np.pi, np.pi, size=2000)
Y = g(X)

plt_reset()

plt.figure()
x = np.linspace(-np.pi, np.pi, 1000)
plt.plot(x, pdf_x(x), color='C0', alpha=0.8, label='True pdf')
plt.hist(X, bins=50, density=True, color='k', alpha=0.3, label='Samples')
plt.xlabel('x')
plt.ylabel('density')
plt.legend()
plt.tight_layout()

plt.figure()
y = np.linspace(-1.0, 1.0, 1000)[1:-1]  # drop the endpoints to avoid dividing by zero
plt.plot(y, pdf_y(y), color='C0', alpha=0.8, label='True pdf')
plt.hist(Y, bins=50, density=True, color='k', alpha=0.3, label='Samples')
plt.xlabel('y')
plt.ylabel('density')
plt.legend()
plt.tight_layout()
savefig('function_of_rv.pdf')
