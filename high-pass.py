import numpy as np
from scipy.signal import freqz, butter
from matplotlib import pyplot as plt

k = 0.4
prev = 0

def my_filter(val):
    global prev
    e = val - prev
    new = prev + e * k 
    prev = new
    return val - new


data = list()
for n in range(1000):
    data.append(np.sin(0.02*n) + 0.2*np.sin(n))
plt.plot(data)


filt_data = list()
for i in range(1000):
    filt_val = my_filter(data[i])

    filt_data.append(filt_val)
plt.plot(filt_data)


plt.show()
