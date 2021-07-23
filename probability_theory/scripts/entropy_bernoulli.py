import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
from utility import savefig, plt_reset


def entropy(pmf, base=2):
    # Compute the entropy of a discrete random variable with probability mass function described by the array pmf
    log_pmf = np.log(pmf)/np.log(base)
    return -np.sum(np.multiply(pmf, log_pmf))


# Number of samples
ns = 1000

# Parameter values
eps = 1e-12
ps = np.linspace(0+eps, 1-eps, ns)

# Entropies
Hs = np.zeros(ns)
for i in range(ns):
    p = ps[i]
    pmf = np.array([1 - p, p])
    Hs[i] = entropy(pmf)


plt_reset()
figsize = (6, 3)
plt.figure(figsize=figsize)
plt.plot(ps, Hs, color='C0', lw=4)
plt.xlabel('p')
plt.ylabel('Entropy')
plt.grid('on')
plt.tight_layout()
savefig('entropy_bernoulli.pdf')
plt.show()
