import numpy as np


def kl_divergence(x_pmf, y_pmf, base=2):
    log_diff_pmf = np.log(x_pmf/y_pmf)/np.log(base)
    return np.sum(np.multiply(x_pmf, log_diff_pmf))


x_pmf = np.array([0.4, 0.2, 0.4])
y_pmf = np.array([0.3, 0.3, 0.4])
z_pmf = np.array([0.3, 0.4, 0.3])

# Check for symmetry
lhs = kl_divergence(x_pmf, y_pmf)
rhs = kl_divergence(y_pmf, x_pmf)
if lhs == rhs:
    print('Symmetry holds')
    comp_str = '=='
else:
    print('Symmetry fails')
    comp_str = '!='
print('D(x||y) = ', lhs, comp_str, rhs, ' = D(y||x)')

# Check the triangle inequality
lhs = kl_divergence(x_pmf, z_pmf)
rhs = kl_divergence(x_pmf, y_pmf) + kl_divergence(y_pmf, z_pmf)
if lhs <= rhs:
    print('Triangle inequality holds')
    comp_str = '<='
else:
    print('Triangle inequality fails')
    comp_str = '> '
print('D(x||y) + D(y||z) = ', lhs, comp_str, rhs, ' = D(x||z)')
