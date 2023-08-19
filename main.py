import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
# widgets for future use
def plt_circle(r=1):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.axis('equal')
    plt.show()


def quadratic(power=2, range=2):
    x = np.linspace(-range, range, 100)
    y = x ** power
    plt.plot(x,y)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.axis('equal')
    plt.show()

