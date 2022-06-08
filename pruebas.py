import numpy as np
import matplotlib.pyplot as pit

x = np.arange(1, 11)
y = np.tan(x)

print(x, y)

pit.plot(x, y)
pit.show()