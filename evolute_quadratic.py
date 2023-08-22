import numpy as np
import matplotlib.pyplot as plt

# Quadratic
x = np.linspace(-2, 2, 50)
y = x ** 2
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.plot(x, y, color='red', linewidth=2, zorder=2)
# plt.axis('equal')

# Tangent code gives the tangent plot and envelopes
for i in range(len(x)):
    tangent_slope = 2 * x[i]
    tangent_intercept = y[i] - tangent_slope * x[i]
    tangent_line = tangent_slope * x + tangent_intercept

    if tangent_slope == 0:  # catch zero division error
        normal_slope = np.inf
    else:
        normal_slope = -1 / tangent_slope

    normal_intercept = y[i] - normal_slope * x[i]
    normal_line = normal_slope * x + normal_intercept

    plt.plot(x, tangent_line, color='blue', alpha=0.5, zorder=1)
    plt.plot(x, normal_line, color='green', alpha=0.5, zorder=1)

# Plot
plt.title('Evolute & Envelope of y=x^2')
plt.xlim(-2, 2)
plt.ylim(-2, 4)
plt.tight_layout()
plt.grid(True)
plt.show()
