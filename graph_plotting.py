import numpy as np
import matplotlib.pyplot as plt

# Generate data for plotting
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y, label='Sine Wave')

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sine Wave Plot')

# Show the legend and plot
plt.legend()
plt.show()


x = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(x)
cos_values = np.cos(x)

# Plot sine and cosine waves
plt.plot(x, sin_values, label='Sine Wave')
plt.plot(x, cos_values, label='Cosine Wave')

# Adding labels and legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sine and Cosine Waves')
plt.legend()

# Show the plot
plt.show()
