import numpy as np
from scipy.stats import norm, skewnorm, gennorm
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
from utility import savefig, plt_reset


plt_reset()
figsize = (6, 4)

# Mean
fig, ax = plt.subplots(figsize=figsize)
mean_params = [1.0, -1.0]
x = np.linspace(-6, 6, 1000)
for mean_param in mean_params:
    dist = norm(loc=mean_param)
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    ax.plot(x, dist.pdf(x), lw=4, label='mean=%.3f' % mean)
fig.legend()
fig.tight_layout()
savefig('moment1_comparison.pdf')

# Variance
fig, ax = plt.subplots(figsize=figsize)
std_params = [2.0, 0.5]
x = np.linspace(-6, 6, 1000)
for std_param in std_params:
    dist = norm(scale=std_param)
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    ax.plot(x, dist.pdf(x), lw=4, label='std dev=%.3f' % var**0.5)
fig.legend()
fig.tight_layout()
savefig('moment2_comparison.pdf')

# Skewness
fig, ax = plt.subplots(figsize=figsize)
alphas = [8.0, -8.0]
x = np.linspace(-4, 4, 1000)
for alpha in alphas:
    dist = skewnorm(alpha)
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    ax.plot(x, dist.pdf(x), lw=4, label='skewness=%.3f' % skew)
fig.legend()
fig.tight_layout()
savefig('moment3_comparison.pdf')

# Kurtosis
fig, ax = plt.subplots(figsize=figsize)
betas = [1.0, 3.0]
x = np.linspace(-4, 4, 1000)
for beta in betas:
    dist = gennorm(beta)
    mean, var, skew, kurt = dist.stats(moments='mvsk')
    ax.plot(x, dist.pdf(x), lw=4, label='kurtosis=%.3f' % (kurt+3))  # add 3 to convert from excess to raw kurtosis
fig.legend()
fig.tight_layout()
savefig('moment4_comparison.pdf')

plt.show()
