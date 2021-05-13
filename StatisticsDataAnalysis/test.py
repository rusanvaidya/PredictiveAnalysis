import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

# Number of experiments0
n = 10
# Probability of success
p = 0.5

# Array of probable outcomes of number of heads
x = range(0, 11)

# Get probabilities
prob = binom.pmf(x, n, p)

# Set properties of the plot
fig, binom_plot = plt.subplots(figsize=(10,8))

binom_plot.set_xlabel("Number of Heads",fontsize=16)
binom_plot.set_ylabel("Probability",fontsize=16)

binom_plot.vlines(x, 0, prob, colors='r', lw=5, alpha=0.5)

# Plot the graph
binom_plot.plot(x, prob, 'ro')
plt.show()
