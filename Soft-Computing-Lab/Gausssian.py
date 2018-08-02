# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:32:30 2018

@author: VP LAB
"""

from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt


n=input("Enter the standard deviation");
window = signal.gaussian(30, std=int(n));
plt.plot(window)
plt.grid(color='g', linestyle='--', linewidth=1)
plt.title(r"Gaussian window ($\sigma$=n)")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
