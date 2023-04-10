import s2lidar
import time
import math
from matplotlib import pyplot as plt

s2lidar.init()
time.sleep(2)

for x in range(100):
    scan = s2lidar.get_scan()
    X = []
    Y = []
    for s in scan:
        if s[2] != 0:
            X.append(s[1] * math.cos(math.radians(s[0])))
            Y.append(s[1] * math.sin(math.radians(s[0])))
    plt.clf()
    # plt.xlim([-1, 1])
    # plt.ylim([-1, 1])
    plt.scatter(X, Y)
    plt.pause(0.01)
plt.show()

s2lidar.stop()
