import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, y, z = symbols('x y z')

def plot_graph(function_str, envelope=True, evolute=True):
    f = sympify(function_str)
    x_vals = np.linspace(-3, 3, 75)
    y_vals = [f.subs(x, val) for val in x_vals]

    plt.clf()
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.plot(x_vals, y_vals, color='red', linewidth=2, zorder=2)
    if envelope or evolute:
        for i in range(len(x_vals)):
            tangent_eq = diff(f, x)
            tangent_slope = tangent_eq.subs(x, x_vals[i])
            tangent_intercept = y_vals[i] - tangent_slope * x_vals[i]
            tangent_line = tangent_slope * x_vals + tangent_intercept

            if tangent_slope == 0:  # catch zero division error
                normal_slope = np.inf
            else:
                normal_slope = -1 / tangent_slope
            if evolute:
                normal_intercept = y_vals[i] - normal_slope * x_vals[i]
                normal_line = normal_slope * x_vals + normal_intercept
                plt.plot(x_vals, normal_line, color='green', alpha=0.5, zorder=1)
            if envelope:
                plt.plot(x_vals, tangent_line, color='blue', alpha=0.5, zorder=1)
    title_string = function_str.replace('**', '^')
    plt.title(f'Graph of {title_string}')
    plt.xlim(-3, 3)
    plt.ylim(-3, 5)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Input the function as a string
while True:
    function_str = input("Enter a function or press 'q' to quit: ").lower()
    if function_str == 'q':
        break
    plot_graph(function_str)