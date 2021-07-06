import numpy as np
import matplotlib.pyplot as plt
from utility import savefig, plt_reset


def gaussian_pdf(x, mean=0.0, std=1.0):
    return (1/(std*(2*np.pi)**0.5))*np.exp(-0.5*((x-mean)/std)**2)


x = np.linspace(-4, 4, 1000)
pdf = gaussian_pdf(x)
cdf = np.cumsum(pdf*np.diff(x, prepend=x[0]))

plt_reset()
figsize = (6, 3)

plt.figure(figsize=figsize)
plt.plot(x, pdf, color='C0', lw=4, label='pdf')
plt.legend()
plt.grid('on')
plt.tight_layout()
savefig('standard_gaussian_pdf.pdf')

plt.figure(figsize=figsize)
plt.plot(x, cdf, color='C1', lw=4, label='cdf')
plt.legend()
plt.grid('on')
plt.tight_layout()
savefig('standard_gaussian_cdf.pdf')

plt.figure(figsize=figsize)
plt.plot(x, pdf, color='C0', lw=4, label='pdf')
plt.plot(x, cdf, color='C1', lw=4, label='cdf')
plt.legend()
plt.grid('on')
plt.tight_layout()
savefig('standard_gaussian.pdf')
