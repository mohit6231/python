import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the histogram
data = np.random.randn(1000)

# Create the histogram
plt.hist(data, bins=30, color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

# Show the plot
plt.show()
