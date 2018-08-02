import numpy as np
from scipy.special import gamma

import matplotlib.pyplot as plt

# The Gamma function
x = np.linspace(-2, 5, 1000)
plt.plot(x, gamma(x), label='$\Gamma(x)$')



x2 = np.linspace(1,6,6)
fac = np.array([1, 1, 2, 6, 24, 120])
plt.plot(x2, fac, marker='o', markersize=12, markeredgecolor='r',
           markerfacecolor='g', ls='',c='r', label='$(x-1)!$')

plt.ylim(-20,20)
plt.xlim(-3, 10)
plt.xlabel('$x$')
plt.legend()
plt.show()
