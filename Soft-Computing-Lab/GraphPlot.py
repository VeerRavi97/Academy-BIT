# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:25:53 2018

@author: VeerRavi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x=pd.Series(np.linspace(-1,1,100))



y=pd.Series(1/(1+(x*x)))


fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y)
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.title("Graph")
plt.show()

