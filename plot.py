import matplotlib.pyplot as pl
import numpy as np


y = np.loadtxt('data_file.txt', unpack=True)
pl.plot(y)
pl.show()

#print(np.polyfit(x, y, 10))

