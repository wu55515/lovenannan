import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
x = np.array([0,0.102,0.174,0.325,0.348,0.437,0.548,0.666,0.688,0.822,0.979,1])
y = np.array([1,0.994,1.225,0.947,1.112,0.806,0.919,0.663,0.683,0.691,1.44, 3.4])
# print(Father_list[i][j]) 判断哪个数据有问题
x_smooth = np.linspace(x.min(), x.max(), 100)
y_smooth = make_interp_spline(x, y)(x_smooth)
print(y_smooth)
plt.scatter(x_smooth,y_smooth)
plt.show()
