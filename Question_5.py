import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from a normal distribution
# mean = 0, standard deviation = 1
data = np.random.normal(loc=0, scale=1, size=1000)

# X-axis: index of each point (1 to 1000)
x = np.arange(1, 1001)

# Scatter plot
plt.scatter(x, data, color="blue", s=15, alpha=0.6, edgecolors="k")

# Labels and title
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Scatter Plot of 1000 Random Numbers (Normal Distribution)")

# Show plot
plt.show()
