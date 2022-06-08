import numpy as np
import matplotlib.pyplot as pit

x = np.arange(0, 3*np.pi, 0.2)
y = np.tan(x)

print(x)
print(y)

pit.plot(x, y)

pit.show()