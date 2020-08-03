import numpy as np 
import matplotlib.pyplot as plt

X = np.array([[1,1], [2,2.5], [3, 1]])
Y = ['#93b1e2', 'red', 'blue']

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 40)

t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)


plt.show()
