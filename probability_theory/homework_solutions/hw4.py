import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
from utility import savefig, plt_reset


def gaussian_pdf(x, mean=0.0, std=1.0):
    return (1/(std*(2*np.pi)**0.5))*np.exp(-0.5*((x-mean)/std)**2)


# number of trials, summed components
m, n = 10000, 100

# Components
x = np.random.uniform(size=(m, n))
mean_x = 1/2
std_x = (1/12)**0.5

# Sums
s = np.sum(x, axis=1)
mean_s = n*mean_x
std_s = (n**0.5)*std_x

t = np.linspace(mean_s - 4*std_s, mean_s + 4*std_s, 1000)

# Plot
plt_reset()
plt.hist(s, density=True, bins=100, alpha=0.8, label='Samples')
plt.plot(t, gaussian_pdf(t, mean=mean_s, std=std_s), alpha=0.8, lw=4, label='CLT Gaussian')
plt.legend()
plt.tight_layout()


from scipy import stats
a, b = 45, 52.5
a_prime = (a - mean_s)/std_s
b_prime = (b - mean_s)/std_s

P = stats.norm.cdf(b_prime) - stats.norm.cdf(a_prime)
print(P)
