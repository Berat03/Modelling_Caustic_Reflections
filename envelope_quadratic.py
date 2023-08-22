import numpy as np
import matplotlib.pyplot as plt

# Quadratic
x = np.linspace(-2, 2, 50)
y = x ** 2
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.plot(x, y, color = 'red', linewidth=2, zorder=2)
#plt.axis('equal')

# Tangent
for i in range(len(x)):
    tangent_slope = 2 * x[i]
    tangent_intercept = y[i] - tangent_slope * x[i]
    tangent_line = tangent_slope * x + tangent_intercept
    plt.plot(x, tangent_line, color='blue', alpha=0.5, zorder=1)


# Plot
plt.title('Envelope of y=x^2')
plt.xlim(-2, 2)
plt.ylim(-1, 3)
plt.tight_layout()
plt.grid(True)
plt.show()
