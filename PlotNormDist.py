import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics


x_axis = np.arange(-20, 20, 0.01)

mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
print('max is: ', max(x_axis))
print('min: ', min(x_axis))

print('mean = ', mean)
print('sd = ', sd)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()

