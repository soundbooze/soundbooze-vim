import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xar = range(0, 10)
    yar = range(0, 10)

    for i in range(len(yar)):
        yar[i] = (random.randint(0, 10))

    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=250)
plt.show()
