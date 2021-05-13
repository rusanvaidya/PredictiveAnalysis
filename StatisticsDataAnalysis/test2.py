import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# Generate 100 random numbers between 0 and 20
Rv = np.linspace(0.0, 20.0, 100)

#calculate the normal distribution
nd = scipy.stats.norm.pdf(Rv,Rv.mean())

# Set properties of the plot
fig, nd_plot = plt.subplots(figsize=(10,8))
nd_plot.set_xlabel("Values of Random Variable", fontsize=16)
nd_plot.set_ylabel("Normal Distribution Values", fontsize=16)

# Plot the graph
nd_plot.plot(Rv,nd)
plt.show()