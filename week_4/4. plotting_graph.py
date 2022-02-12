import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
blueline = np.exp(t)
greenline = np.exp(0.5*t)
redline = np.exp(0.1*t)

plt.plot(t,blueline,'b^')
plt.plot(t,greenline,'gs')
plt.plot(t,redline,'r--')
plt.xlim(0,5)
plt.ylim(0,100)
plt.show()



