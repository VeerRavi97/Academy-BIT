# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:48:40 2018

@author: VP LAB
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from scipy.integrate.quadpack import quad


def func(x):
    return np.array(2.0*x**2 - x - 4.0)

x = np.linspace(0 ,10, 100)
integral = quad(func, 1, 5)



section = np.linspace(1, 5, 20)

plt.plot(x, func(x))
plt.fill_between(section, func(section), facecolor ='g' )
