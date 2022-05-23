import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal
from sklearn import preprocessing

x, y = np.mgrid[-5.0:5.0:30j, -5.0:5.0:30j]
# Need an (N, 2) array of (x, y) pairs.
xy = np.column_stack([x.flat, y.flat])
mu = np.array([0.0, 0.0])

sigma = np.array([1.5, 1.5])
covariance = np.diag(sigma**2)

z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)

# Reshape back to a (30, 30) grid.
z = z.reshape(x.shape)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

z_n = preprocessing.normalize(z)
print(z_n)

ax.plot_surface(x,y,z_n)
#ax.plot_wireframe(x,y,z)

plt.show()