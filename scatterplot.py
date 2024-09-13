import numpy as np
import matplotlib.pyplot as plt

# Generate random data for scatter plot
x = np.random.rand(100)
y = np.random.rand(100)

# Create the scatter plot
plt.scatter(x, y, color='blue', label='Random Points')

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot of Random Points')

# Show the legend and plot
plt.legend()
plt.show()
