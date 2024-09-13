import numpy as np
import matplotlib.pyplot as plt

# Data for bar plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 2, 9, 4])

# Create a bar plot
plt.bar(x, y, color='green')

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Plot Example')

# Show the plot
plt.show()
